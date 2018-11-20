#
# :date: 2018-01-22
# :author: Andre Stephens
# :copyright: GPL v2 or later
#
#
#
# Example usage:
# ~ python transcribe.py gs://<bucket_name>/my_audio.flac
#


import argparse
import json
import io
import os


def writer(object, file):
    with open(file, 'w') as f:
        if '.json' in file:
            f.write(json.dumps(object))
        else:
            f.write(str(object))
    print("{} written to output directory".format(file))
    return None


def transcribe(gcs_uri, apikey, language='en-US', confidences=False):
    """Function to asynchronously translate audio file uploaded
    to Google Cloud Platform.

    Parameters
    -----------
      gcs_uri: str
        URI file path consisting of bucket name and filename
        See: https://cloud.google.com/bigquery/docs/loading-data-cloud-storage
      apikey: str 
        Path to the .json file with Google Cloud API key.
        See: https://cloud.google.com/docs/authentication/api-keys
      language: str (default: 'en-US')
        Passes language code argument to client. Many languages available.
        See: https://cloud.google.com/speech-to-text/docs/languages
      confidences: bool (default: False)
        Inserts back-to-top links below headings if True.
      
    Returns
    -----------
    cont: file
      Text file with transcription and (optionally) json file with
      transcription and confidence levels.
    """

    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = apikey
    client = speech.SpeechClient()

    # For optimal results, file sample hertz rate
    # should be at least 16000Hz
    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC, 
        language_code=language)

    operation = client.long_running_recognize(config, audio)

    print('PROCESSING...')

    response = operation.result(timeout=None)

    transcript_list = []
    result_dict = {}

    for n, result in enumerate(response.results):
        # Note that results returns alternative translations
        # with varying degrees of confidence, with the zeroth
        # alternative as the most likely.
        transcript = result.alternatives[0].transcript
        confidence = result.alternatives[0].confidence

        result_value = {
            'transcript': transcript,
            'confidence': confidence
        }

        result_key = 'result_{}'.format(n)
        result_dict[result_key] = result_value

        transcript_list.append(transcript)
    
    transcript_str = ''.join(transcript_list)

    # write files to os
    audio_name = gcs_uri.split('/')[3]
    writer(transcript_str, '{}-transcript.txt'.format(audio_name))
    if confidences:
        writer(result_dict, '{}-transcript_confidences.json'.format(audio_name))

    return None



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'gsc_uri', 
        type=str,
        help='gcs_uri for audio file to be recognized')
    parser.add_argument(
        'apikey',
        type=str,
        help='File path for .json file with gcs api key')
    parser.add_argument(
        '--language',
        '-l',
        type=str,
        help='Language of audio recording')
    parser.add_argument(
        '--confidences',
        '-c',
        action='store_true',
        help='Optionally return json file with transcription confidence levels.')
    args = parser.parse_args()
    transcribe(args.gsc_uri, 
                args.apikey,
                args.language,
                args.confidences
                )


# END.
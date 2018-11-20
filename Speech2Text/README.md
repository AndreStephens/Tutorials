transcribe
==========

transcribe.py is a Python command line script that translates audio to text using the Google Cloud Service Speech API.

**Requires:**

* [Google Cloud Service account (and API key)](https://cloud.google.com/docs/authentication/api-keys)
* [URI link to audio file on Google Cloud](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage)
* [flac or wav audio file on 1 channel (mono)]()

# Usage

You can copy the [transcribe.py](transcribe.py) file to a local directory and use it from there.

*For basic use:*


    python transcribe.py gs://myBucketName/myAudioFile.flac

## Command Line Arguments

<pre>
positional arguments:
  gsc_uri             gcs_uri for audio file to be recognized
  apikey              File path for .json file with gcs api key

optional arguments:
  -h, --help          show this help message and exit
  -l, --language      Language of audio recording
  -c, --confidences   Optionally return json file with transcription confidence levels.
</pre>

## Examples

You can specify the language of the audio file to be translated. There are [many options](https://cloud.google.com/speech-to-text/docs/languages) available.

    python transcribe.py gs://myBucketName/SpanishAudio.wav -l es-ES

Options are available for many language dialects (indicated by the code in all caps). 

    python transcribe.py gs://myBucketName/MexicanSpanishAudio.wav -l es-MX

You can choose to write a second file to your current directory with the confidence levels for chunks of translation. Note that the script only returns the most likely translation.

    python transcribe.py gs://myBucketName/EgyptianArabic.wav -l ar-EG

<br>
__For more information on the script, check out this [Speech2Text notebook](./Tutorials/Speech2Text/Speech2Text.ipynb).__
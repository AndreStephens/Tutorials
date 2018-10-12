# git Tutorial

## Install git

1. Download latest windows release from the [git website](http://git-scm.com)
2. Check installation: `git --version`

## Create directory
1. Open the Windows command prompt
2. Navigate to your working directory using `dir` to list items in directory and `cd` to change into directories
3. Make a new directory named 'GitPlay': `mkdir GitPlay`

## Create files
4. Create a new file named intro.md, writing a title to the first line: `echo #My Git Intro > intro.md` 
6. Create a new file named intro.html, writing a title to the first line: `echo ^<H1^>My Git Intro^</H1^> > intro.html`
5. Create a new file named log.txt: `echo log.txt`

## Getting started with git
5. Intialize git repo (notice the .git folder): `git init`
6. Configure git by adding name and email: `git config --global user.name "Jane Doe"` `git config --global user.email "janedoe@email.com"`

## Committing files to repo
6. Check status of directory: `git status`
7. Add file to staging: `git add intro.md`
8. Let's commit the new file with a message: `git commit -m "initial commit"`
9. Do the same for intro.html

## Ignoring file types
1. Let's ignore log.txt: `echo log.txt >> .gitignore` 
1. To ignore all text files: `echo *.txt >> .gitignore`
2. To ignore a subdirectory: `echo \subdir >> .gitignore`  

## Switching branches
1. Create a new branch (from master branch) called testing: `git branch testing`
2. Switch to testing branch: `git checkout testing`
3. Let's add a new line to some files: `echo by *Andre S.* > intro.md` `echo by ^<i^>Andre S.^</H1^> > intro.html`
4. Let's also create a new file: `echo > data.csv`
5. Add and commit all changes
6. Let's return to the master branch (notice that the changes made in testing disappear when we switch!): `git checkout master`
7. To merge testing into master, simply do: `git merge testing`

## Common git Commands
|Command | explanation|
|--- | --- |
|`git init` | initializes files |
|`git status` | check staged files |
|`git add file.txt` | stage file named file.txt |
|`git add *.csv` | stage all files with .csv extension |
|`git add .` | stage all files |
|`git rm --cached file.txt` | remove file.txt from staging |
|`git branch mybranch` | create new working branch |
|`git checkout mybranch` | switch to working branch |
|`git diff` | shows changes to be staged |
|`git log` | lists branch commit history |
|`git reset --hard [commit]` | discards all changes after specified commit |



#git Tutorial

##Install git

1. download latest windows release from the [git website](http://git-scm.com)
2. check installation: `git --version`

##Create directory
1. open the Windows command prompt
2. navigate to your working directory using `dir` to list items in directory and `cd` to change into directories
3. make a new directory named 'GitPlay': `mkdir GitPlay`

##Create files
4. create a new file named intro.md, writing a title to the first line: `echo #My Git Intro > intro.md` 
6. create a new file named intro.html, writing a title to the first line: `echo ^<H1^>My Git Intro^</H1^> > intro.html`
5. create a new file named log.txt: `echo log.txt`

##Getting started with git
5. intialize git repo (notice the .git folder): `git init`
6. configure git by adding name and email: `git config --global user.name "Jane Doe"` `git config --global user.email "janedoe@email.com"`

##Committing files to repo
6. Check status of directory: `git status`
7. Add file to staging: `git add intro.md`
8. Let's commit the new file with a message: `git commit -m "initial commit"`

## Ignoring file types
1. Let's ignore log.txt: `echo log.txt >> .gitignore` 
1. To ignore all text files: `echo *.txt >> .gitignore`
2. 1. To ignore a subdirectory: `echo \subdir >> .gitignore`  

##Switching branches
1. Create a new branch (from master) called testing: `git branch testing`
2. Switch to testing branch: `git checkout testing`
3. Let's add a new line to some files: `

##Common commands

|Command | explanation|
|--- | --- |
|`git init` | initializes files |
|`git status` |  |
|`git add file.txt` |  |
|`git add *.csv` |  |
|`git add .` |  |
|`git rm --cached` |  |
|`git branch branchname` |  |
|`git checkout branchname` |  |



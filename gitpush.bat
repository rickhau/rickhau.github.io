@echo off
REM HOW-TO
REM Reference: http://mathamy.com/migrating-to-github-pages-using-pelican.html
REM Use virtual env to install pelican, markdown
REM git clone https://github.com/getpelican/pelican-plugins.git
REM git clone https://github.com/fle/pelican-simplegrey.git
REM Above two git folders will not be pushed due to .gitignore
REM Create Article: python make_entry.py "Your Title"
REM Edit your "Your Title".md
REM Run ./gitpush.bat
REM
REM Image:
REM Put your image(test.jpg) under content/images folder
REM The path will be as following
REM ![Test Image](https://github.com/rickhau/rickhau.github.io/raw/master/images/test.png)


REM Use "source" branch to create new post under "content" folder
REM Commit and push back to remote origin/source branch
REM Travis CI will run the Makefile 
REM Makefile
REM - Run pelicanconf first (So, you have to checkout git repo in .travis.yml before here)
REM - Then, use ghp-import to push the compiled source back to master branch

REM Create source post in content folder and run the following commands
set /P GITMSG="[GIT Commit MSG]: "
IF "%GITMSG%"=="" (
set GITMSG=Update Pelican blog content
)
git pull origin source
git add .
git commit -am "%GITMSG%"
@echo Add Git commit message: [ %GITMSG% ]
git push -f origin source

# Use "source" branch to create new post under "content" folder
# Commit and push back to remote origin/source branch
# Travis CI will run the Makefile 
# Makefile
# - Run pelicanconf first (So, you have to checkout git repo in .travis.yml before here)
# - Then, use ghp-import to push the compiled source back to master branch

# Create source post in content folder and run the following commands
git pull origin source
git add .
git commit -am "Update new content to pelican blogger..."
git push -f origin source

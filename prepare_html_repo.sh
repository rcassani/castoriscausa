# Bash script, to prepare the files to update the rcassani.github.io repo
# Using Script Package for Atom, in Linux
# Run this file with Ctr-Shift-b

# dir wit the HTML repo

# Build
invoke clean
invoke preview

# Current directory
WD=`pwd`

# HTML repo in ../castoris-html
# Delete old files in HTML repo
cd ../castoris-html
ls | grep -v '.git' | xargs rm -rf
# https://unix.stackexchange.com/questions/153862/remove-all-files-directories-except-for-one-fileco

# Copy new files to repo
cd $WD
cp -a ./output/. ../castoris-html

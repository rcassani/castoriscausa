# Bash script, to prepare the files to update the rcassani.github.io repo
# Using Script Package for Atom, in Linux
# Run this file with Ctr-Shift-b

# dir wit the HTML repo

# Build
kill $(lsof -i:8000 | awk 'NR==2{print$2}')
fab build

# HTML repo in ../castoris-html
# Delete old files in HTML repo
ls ../castoris-html | grep -v '.git\|CNAME' | xargs rm -rf
# https://unix.stackexchange.com/questions/153862/remove-all-files-directories-except-for-one-fileco

# Copy new files to repo
cp -a ./output/. ../castoris-html

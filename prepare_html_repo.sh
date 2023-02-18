# Bash script, to prepare the files to update the rcassani.github.io repo
# Content dir: castoriscausa
# HMTL dir:    castoris-html

# Clean castoriscausa/output/
invoke clean
# Generate with publish settings
invoke preview

# Clean old in HTML dir
cd ../castoris-html
ls | grep -v '.git' | xargs rm -rf
# https://unix.stackexchange.com/questions/153862

# Copy new files to HTML dir
cd ../castoriscausa
cp -a ./output/. ../castoris-html

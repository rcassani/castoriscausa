# Bash script, to clean, build and serve the Pelican Website
# Using Script Package for Atom, in Linux
# Run this file with Ctr-Shift-b

kill $(lsof -i:8000 | awk 'NR==2{print$2}')
fab reserve
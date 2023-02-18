# Bash script, to clean, build and local serve the Pelican Website
# Content dir: castoriscausa

# Clean castoriscausa/output/
invoke clean
# Generate with base settings
invoke build
# Serve site at http://localhost:8000
invoke serve

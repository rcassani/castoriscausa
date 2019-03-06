# castoriscausa
Files for Static Site www.castoriscausa.com

# Generating Static website
1. Activate the Conda environment described in the environment definition file
`pelican-linux.yml`, it is Python 2.7 with Pelican and the required packages.
```
  $ activate pelican-env
```
2. Run the script `reserve.sh` to stop serving the local page (if existent), re-generate the HTML files and serve them.

3. Open [http://localhost:8000/](http://localhost:8000/) in the web browser

4. When the website is ready to be uploaded, run the script `prepare_html_repo.sh`, this will copy all the content to `..\castoris-html`

5. Just commit and push `castoris-html`

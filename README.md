# CastorisCausa
Files for static site: [https://www.castoriscausa.com/](https://www.castoriscausa.com/)

## Environment to generate static website
1. Create and activate an ([conda](https://docs.conda.io/projects/conda/en/latest/index.html)) environment with Python 3
2. Using `pip` install Pelican and some dependencies
```
  $ pip install pelican markdown typogrify bs4 invoke
```
>💡 Alternatively, create the environment from the [`pelican.yml`](pelican.yml) (March 2022)

## Pelican configuration
All the details are in [`pelicanconf.py`](pelicanconf.py)

### Theme
The Pelican theme is `pelican-kis`  
  [https://github.com/rcassani/pelican-kis](https://github.com/rcassani/pelican-kis)

### Plugins
 * tipue_search
 * sitemap
 * series
 * render_math

### Custom CSS
Custom CSS [castoris.css](/content/custom_css/castoris.css) to:
  * Set two columns 9+3 (instead of 8+4)
  * Colors
  * Fonts

### Custom JS
Custom JS [castoris.js](/content/custom_js/castoris.js) to:
  * Hide email
  * Confirmation button in publications

### Publications
Publication format is IEEE

## Build and deployment
1. To build and serve the site, run the script `reserve.sh`

2. Open [http://localhost:8000/](http://localhost:8000/) in the web browser

3. When the website is ready to be uploaded, run the script `prepare_html_repo.sh`, this will copy all the content to `..\castoris-html`

4. Just commit and push `castoris-html` to [https://github.com/rcassani/rcassani.github.io]()

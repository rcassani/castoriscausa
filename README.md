# castoriscausa
Files for Static Site www.castoriscausa.com

# Generating Static website
1. Create and activate an (conda) environment with Python 3.5+
2. Using `pip` install Pelican and some dependencies
```
  $ pip install pelican markdown typogrify bs4 invoke
```
    2.1. The environment file X wwas created on 2019-12-11

3. The Pelican theme is `pelican-bootstrap3`  
  [https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3]()
   The theme can be downloaded with [DownGit](https://minhaskamal.github.io/DownGit/#/home). And place it in `.`

   3.1. The `pelican-bootstrap3` requires the [`i18n_subsites`](https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites) plugin. Download it and place it in `.\plugins`.

4. To build and serve the site, run the script `reserve.sh`

5. Open [http://localhost:8000/](http://localhost:8000/) in the web browser

6. When the website is ready to be uploaded, run the script `prepare_html_repo.sh`, this will copy all the content to `..\castoris-html`

7. Just commit and push `castoris-html`

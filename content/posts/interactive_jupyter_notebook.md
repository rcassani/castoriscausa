Title: Interactive Jupyter Notebook in static websites [Test]
Date: 2020-04-15 18:00
Tags: Jupyter, WebDevelopment
Author: Raymundo Cassani
Slug: interactive-jupyter-notebook
Thumbnail: interact.gif

Without any question, `Jupyter Notebooks` are an amazing medium to present and share code, equations, graphics, among others. There are multiple ways to share them: as only view [in GitHub](https://help.github.com/en/github/managing-files-in-a-repository/working-with-jupyter-notebook-files-on-github) or with [nbviewer](https://nbviewer.jupyter.org/); to fully interactive in [Binder](https://mybinder.org/), where an the Notebook runs in an live environment.

In this post, I tested the embedding of an interactive `Jupyter Notebook` in to this website. The interaction is achieved by using [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) (Interactive HTML Widgets) in the Notebook. The steps to do this are described in this post:
[https://elc.github.io/posts/embed-interactive-notebooks/](https://elc.github.io/posts/embed-interactive-notebooks/).

Finally, notes at the end of this post add more details for certain steps in the process.

## Result
This is the embedded `Jupyter Notebook`. To use the widgets, click first on `Show Widgets`.

The original one can be found as a [Gist](https://gist.github.com/rcassani/a472b922fc4accb3e9551f3f16dedb76), and in [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gist/rcassani/a472b922fc4accb3e9551f3f16dedb76/master)  

<iframe src="/htmls/interactive_test.html" frameborder="0" id="iframe" onload='javascript:resizeIframe(this);'></iframe>
<script language="javascript" type="text/javascript">
  function resizeIframe(obj) {
  obj.style.height = 350 + obj.contentWindow.document.body.scrollHeight + 'px';
  }
</script>


## Notes
1. The list of requirements for the `Jupyter Notebook` can be obtained by converting the notebook to a Python script with [nbconvert](https://nbconvert.readthedocs.io/en/latest/usage.html#executable-script), and the using [pipreqs](https://github.com/bndr/pipreqs).  


		:::bash
		$ jupyter nbconvert --to script notebook_name.ipynb
		$ pipreqs .


2. An `iframe` element is used to inserting the HTML file created with [nbinteract](https://www.nbinteract.com/) to the static webpage. By default the `height` of the `iframe` element needs to be defiend before hand, however, it can be automatically adjusted to the size of its content by adding a javascript function to the `onlad` attribute of the `iframe`. As such, the HTML code to place in the static site is:  


		:::html
		<iframe src="/htmls/notebook_name.html" frameborder="0" id="iframe" onload='javascript:resizeIframe(this);'></iframe>
		<script language="javascript" type="text/javascript">
			function resizeIframe(obj) {
			obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
			}
		</script>

	The `height` of the loaded `HTML` is usually smaller than the `height` of the HTML once the widgets are loaded. Thus, the `height` may need to be further adjusted depending on the type and quantity of widgets.

3. To have a better presentation of the Notebook, I changed the the class `container` in the HTML file created with [nbinteract](https://www.nbinteract.com/) to have a `width` of `100%`.

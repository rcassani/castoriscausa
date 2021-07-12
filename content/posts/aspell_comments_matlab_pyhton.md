Title: Spellcheck Matlab and Python scripts
Date: 2021-07-11 21:00  
Tags: MATLAB, Python, Linux
Author: Raymundo Cassani
Slug: aspell-comments-matlab-pyhton
Thumbnail: spellcheck.png

<center>
<img src="/images/spellcheck.png" style="height: 250px;"/>
<div>Based on icon made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
</center>  

Good code commenting, including good syntax and spelling, is an important feature to assure the high quality of code documentation, which in turn, is vital in [development of scientific open-source software](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745). Poor spelling is not only [unprofessional](https://softwareengineering.stackexchange.com/questions/137930/how-to-find-out-if-spelling-mistakes-in-source-code-are-a-serious-issue-or-not), it can [create confusion, reduce clarity and meaning](https://www.bbc.com/worklife/article/20170807-the-true-importance-of-good-spelling), and produce embarrassing typos in the GUI, e.g. "**EGG** signal" instead of "EEG signal".

Although it's an often demanded functionality, as per July 2021, there is **not spellcheck support in Matlab Editor**. Some approaches to spellcheck the code consist in: opening the scripts in a different (text) editor, or extracting the comments from the scripts to spellcheck them with a different software, and propagate the changes back to the original files. [Link](https://www.mathworks.com/matlabcentral/answers/59119-spellcheck-functionality-in-matlab-editor).

In this post, a "simpler" way is described, i.e., configure [Aspell](http://aspell.net/) and use it to perform spellchecking only in: **comments** and **strings**.

The following command installs Aspell and English dictionaries with [pacman](https://wiki.archlinux.org/title/pacman). Similar commands should work for other package managers.

    :::bash
    # pacman -S aspell aspell-en

We need to indicate Aspell to only spellcheck text between delimiters. This is to say text between `%` and the `EOL` for **comments**; and text between `'` and `'` for **strings**.

    :::bash
    $ aspell --add-filter context --clear-context-delimiters --add-context-delimiters "% \0" --add-context-delimiters "' '" -c matlab_script.m

Although the [documentation of Aspell](http://aspell.net/0.61/man-html/Notes-on-Various-Filters-and-Filter-Modes.html) indicates that *"If more than one delimiter pair is specified by one call of add|rem-context-delimiters they have to be combined to a comma separated list."* the option `"% \0,' '"` does not work as expected, that's why the previous command has twice the `--add-context-delimiters` option.

For sake of simplicity it's possible to save such configuration as an **Aspell filter mode**, defined in a *Aspell Mode File* (`.amf`) ([Filter Modes](http://aspell.net/dev-html/Filter-Modes.html)), and make it the default mode (behaviour) for `.m` files. As such, a file `matlab.amf` file ([link](https://gist.github.com/rcassani/4e22c64819aff8caf506d33fffad9dad)) is created in the Aspell path, `/usr/lib/aspell` in my case, and it contains:

    :::text
    MODE matlab

    ASPELL >=0.60.1

    MAGIC /<noregex>/m

    DESCRIPTION mode for checking Matlab comments

    FILTER context
    OPTION clear-context-delimiters
    OPTION add-context-delimiters % \0
    OPTION add-context-delimiters ' '

Thus, to spellcheck a Matlab script, just run:

    :::bash
    $ aspell -c matlab_script.m

### Bonus content: Spellcheck in Python scripts
Several Python IDEs, such as [Spyder](https://www.spyder-ide.org/) already have spellcheck. To use Aspell in spellcheck of **comments** (which start with `#`) and **strings** (that can be between single and double quotes), in **theory** an similar approach "should" work, however, there is a  [bug with configuring `#`](https://github.com/GNUAspell/aspell/issues/505) in a `.amf` file. Fortunately, it can be worked out with this messy call to Aspell:

    :::bash
    $ aspell --add-filter context --clear-context-delimiters --add-context-delimiters "# \0" --add-context-delimiters "' '" --add-context-delimiters "\" \"" -c python_script.py

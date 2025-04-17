Title: Using PyScript with Pelican: Toy example
Date: 2023-05-13 19:00
Modified: 2025-04-16 23:00
Tags: Python, tutorial, WebDevelopment
Author: Raymundo Cassani
Slug: pyscript_toy_example
Thumbnail: pyscript_pelican.png
PyScript_JS: https://pyscript.net/releases/2023.11.2/core.js

**Updated**:

* HTML has been updated to use a specific version of PyScript (2023.11.2)
* Python code has been updated for that versions of PyScript

This post shows a simple game created using [PyScript](https://pyscript.net/) in this static website created with [Pelican](https://docs.getpelican.com/en/latest/) and [Markdown](https://en.wikipedia.org/wiki/Markdown) files.

## The game
<p></p>
<div style="border: 2px solid black;padding: 10px;">
  <script type="py" src="/scripts/guess_game.py" id="py-internal-0"></script>
  <strong><p id="game-message-txt"></p></strong>
  <input py-keydown="new_guess_event" id="new-guess-txt" class="py-input" type="text">
  <button id="new-guess-btn" class="py-button" type="submit" py-click="new_guess">
  Submit guess
  </button>
  <button id="reset-game-btn" class="py-button" type="submit" py-click="new_game">
  Reset
  </button>
</div>
<p></p>

## How it's implemented
The implementation is quite eclectic (as [Frankenstein's monster](https://en.wikipedia.org/wiki/Frankenstein%27s_monster)), it consist of 3 parts:

1. **Markdown post**: This is used by Pelican to create the post entry in the website, the code is here:
    [https://github.com/rcassani/castoriscausa/blob/master/content/posts/pyscript_toy_example.md](https://github.com/rcassani/castoriscausa/blob/master/content/posts/pyscript_toy_example.md)

    It's very important to modify the Pelican theme to add the link to PyScript in `<head>`:

        :::html
        <script defer src="https://pyscript.net/latest/pyscript.js"></script>

    I made an update in my Pelican theme to do so. The modification can be found [here](https://github.com/rcassani/pelican-kis/commit/a6d975444b47696c49b5170d06d7e659a195e4d5)


2. **An HTML block in the Markdown file**: Indicates which Python script will be used, and how it's connected to the UI elements in the page:

        :::html
        <div style="border: 2px solid black;padding: 10px;">
            <script type="py" src="/scripts/guess_game.py" id="py-internal-0"></script>
            <strong><p id="game-message-txt"></p></strong>
            <input py-keydown="new_guess_event" id="new-guess-txt" class="py-input" type="text">
            <button id="new-guess-btn" class="py-button" type="submit" py-click="new_guess">
            Submit guess
            </button>
            <button id="reset-game-btn" class="py-button" type="submit" py-click="new_game">
            Reset
            </button>
        </div>

3. **A Python script**: Gets input from the HTML elements, does the game logic and writes on the HTML

        :::python
        {!> https://raw.githubusercontent.com/rcassani/castoriscausa/master/content/scripts/guess_game.py !}

## Conclusion
This was a fun experiment, it opens the gates to do very interesting stuff with Python in my website 😎

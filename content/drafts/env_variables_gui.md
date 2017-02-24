Title: Env Var GUI
Date: 2016-12-06 19:00
Category: Blog
Tag: Template
Slug: template
Author: Ray Cassani
Lang: spa

the path for things executed with double click is defined not in ~./bashrc but in ~/.profile

for a python script there was a behaviour when called by terminal and when called with GUI (nemo)

the shortcut in the Menu has the same behaviout than the one in GUI

learned on

shebang in python scripts
env variables with ~/.bash_profile, ~/.bashrc and ~/.profile

----------
The issue can be solved changing the shebang in the file:
/usr/share/qtodotxt/bin/qtodotxt

``` Python code

#! /usr/bin/env python3

import os

print(os.environ['PATH'])
input('press ENTER ...')

```
``` bash

commands() {
	source ~/.bashrc
	#qtodotxt
	python3 python3_print_path
	#$SHELL
}

export -f commands

gnome-terminal -e "bash -c 'commands'"
```

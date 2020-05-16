Title: [Tutorial]: Making a Desklet for Cinnamon
Date: 2020-05-12 09:22
Category: Programming
Tags: tutorial
Author: Raymundo Cassani
Slug: cinnamon-desklet-development
Thumbnail: first_desklet.png

A good day I was going through the available [Desklets for Cinnamon](https://cinnamon-spices.linuxmint.com/desklets), looking for an desklet to display graphs about the current state of the system (CPU, RAM, disks, etc.), although I found the nice desklets such as [Simple monitor system](https://cinnamon-spices.linuxmint.com/desklets/view/29), [CPU Load](https://cinnamon-spices.linuxmint.com/desklets/view/44) and [Disk Space](https://cinnamon-spices.linuxmint.com/desklets/view/39), none of them quite do what I need. Thus I resolved to develop the desklet. Because the information to develop a desklet is outdated[<sup>1</sup>](https://www.erikedrosa.com/2014/12/31/hello-world-desklet-tutorial.html), I decided to document the process, this is the first part of that process. How to create a simple desklet. At the moment of writing, Cinnamon 4.4.8 on Arch Linux was used.

### 1. What is a desklet?
"Desklets are little programs which you can place on your desktop, on top of your desktop background"[<sup>2</sup>](https://cinnamon-spices.linuxmint.com/). Moreover, desklets as well as other graphical elements in Cinnamon are written in JavaScript[<sup>3</sup>](https://linuxmint-developer-guide.readthedocs.io/en/latest/technology.html#javascript), and use the Cinnamon's JavaScript interpreter (CJS)[<sup>4</sup>](https://linuxmint-developer-guide.readthedocs.io/en/latest/cinnamon.html?highlight=desklet#cjs). More information about desklets can be find in the official repository [https://github.com/linuxmint/cinnamon-spices-desklets](https://github.com/linuxmint/cinnamon-spices-desklets).

### 2. Creating a simple desklet
Ok, with the previous information in mind, here a simple desklet is created and explained. When finished, it should look like the image below. The files described in this section can be downloaded from [here](https://gist.github.com/rcassani/63bbc282efa9328302b589d3a3e06f75).

<center>
![Alt](/images/first_desklet.png)  
First desklet, it prints "Hello Desktop" and can have multiple instances
</center>  

First of all, the desklets are located at `~/.local/share/cinnamon/desklets`, where each desklet has its own directory.

1. Then, create a directory with the name `PROJECT@AUTHOR`, this is the UUID of the desklet. For example `first-desklet@rcassani`

2. A desklet requires at least two files:
  * `metadata.json`: As it names indicates, this has the metadata for the desklet and [additional options](https://github.com/linuxmint/Cinnamon/wiki/Applet,-Desklet-and-Extension-Settings-Reference#additional-options-in-metadatajson) such as `max-instances` to allow multiple instances of the desklet.

		:::json
		{
		"max-instances": "10",
		"uuid": "first-desklet@rcassani",
		"name": "First Desklet",
		"description": "This is my first desklet",
		"version": "0.1",
		"prevent-decorations": false
		}

  * `desklet.js`: Here is where the JavaScript code for the desklet is. Below there is a simple functional desklet that adds a button on the desktop.

		:::javascript
		const Desklet = imports.ui.desklet;
		const St = imports.gi.St;

		function MyDesklet(metadata, desklet_id) {
		    this._init(metadata, desklet_id);
		}

		MyDesklet.prototype = {
		    __proto__: Desklet.Desklet.prototype,

		    _init: function(metadata, desklet_id) {
		        Desklet.Desklet.prototype._init.call(this, metadata, desklet_id);
		        this.setupUI();
		    },

		    setupUI(){
		      // creates container for one child
		      this.window = new St.Bin();
		      // creates a label with test
		      this.text = new St.Label({text: "Hello Desktop"});
		      // adds label to container
		      this.window.add_actor(this.text);
		      // Sets the container as content actor of the desklet
		      this.setContent(this.window);
		    },
		};

		function main(metadata, desklet_id) {
		    return new MyDesklet(metadata, desklet_id);
		}
  <!-- __ -->

  Constants are declared with [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const), and cannot be re-declared nor changed. First, the `Desklet` class is imported from [`.ui.desklet`](https://github.com/linuxmint/cinnamon/blob/master/js/ui/desklet.js). The Shell Toolkit is imported at `imports.gi.St;`, and it is used to add elements to the desklet, St documentation can be found [here](https://gjs-docs.gnome.org/st10~1.0_api/). The `function MyDesklet` is the constructor for our desklet, it takes `metadata` (dictionary) with the metadata of the desklet, and `desklet_id` (int) which is the instance id of the desklet. Using `MyDesklet.prototype` allows us to add new methods to the object constructors. The method `setupUI()` contains the behaviour of the desklet, see comments in the code above. Note that it is called inside `_init`. Finally, the function `main` returns an instance of `MyDesklet`

### Next steps
By this point there is a working desklet. The behaviour of the desklet still needs to be coded to have all the desired features, will be documented in a future post.

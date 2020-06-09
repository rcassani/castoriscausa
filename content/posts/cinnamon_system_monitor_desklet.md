Title: Developing a Desklet for Cinnamon
Date: 2020-06-09 13:00
Category: Programming
Tags:
Author: Raymundo Cassani
Slug: system-monitor-graph-desklet
Thumbnail: sys_monitor_graph_thumb.gif

In a [previous post](/posts/2020/05/12/cinnamon-desklet-development/), the minimum code for a functional Cinnamon Desklet was provided. Based on that, I started to develop the [System monitor graph](https://cinnamon-spices.linuxmint.com/desklets/view/56) which shows graphs for the level of activity in various system variables including: CPU, memory, and disks. This post describes some of the elements that I found important during the development of such a Desklet.

<center>
![Alt](/images/sys_monitor_graph.gif)<br>
System monitor graph Desklet.
</center>  

### Setting tools
* As with many coding projects, the use of [git]() or any other version control software is desirable to track and revert changes.
* The [Developer's Tools](https://cinnamon-spices.linuxmint.com/desklets/view/17) Desklet was very helpful as it allows to restart Cinnamon with one click, display the Cinnamon console, among other actions.
* Printing in the Cinnamon console is often very useful  

		:::javascript
		global.log('Some text or variable goes here');

### Adding Settings
The ability to configure a Deskelet is very important. This is reached by creating the `settings-schema.json` file besides the `desklet.js` file. The `settings-schema.json` contains the elements in the GUI that the user can modify, these include: text labels, switches, text boxes, color choosers. More info can be found [here](https://projects.linuxmint.com/reference/git/cinnamon-tutorials/xlet-settings.html) and [here](https://projects.linuxmint.com/reference/git/cinnamon-tutorials/xlet-settings-ref.html). To connect the Settings with your Desklet:

1. Add `Settings` to the `imports`:

		:::javascript
		const Settings = imports.ui.settings;

2. Get the Setting values in the `_init` function of the Desklet,

		:::javascript
		this.settings = new Settings.DeskletSettings(this, this.metadata["uuid"], desklet_id);
		this.settings.bindProperty(Settings.BindingDirection.IN, "background-color", "background_color", this.on_setting_changed);

The arguments for `bindProperty` are: `BindingDirection.IN` changes in the settings go into the Desklet, `background-color` the element name in the `settings-schema.json`, and `background_color` name of the property to be created in the Desklet, it can be accesed as `this.background_color`.

### Adding refreshing
Most Desklets need to be updated on a fix schedule, this action can be performed by adding a timer.

1. Add `Mainloop` to the `imports`:

		:::javascript
		const Mainloop = imports.mainloop;

2. A way to use this timer is to split the `update` function of the Desklet in two:

		:::javascript
		update: function() {
				// updates the visuals in Desklet
				this.update_draw();
				// calls this.update() in refresh_interval seconds
				this.timeout = Mainloop.timeout_add_seconds(this.refresh_interval, Lang.bind(this, this.update));
		},

3. Additionally, if a update is required before the next interval, it can be forced. For example below removes the `mainloop` and intermediately calls `this.update()` when the `Settings` have been updated. Note that the timer is set again inside `this.update()`.

		:::javascript
		on_setting_changed: function() {
		Mainloop.source_remove(this.timeout);
		this.update();
		},

### Interacting with files and commands
Often a Desklet needs to read a file or execute a command. For the first, the function `get_file_contents_utf8_sync` does the trick. `Cinnamon` has to be added to the `imports`.

	:::javascript
	let mem_out = Cinnamon.get_file_contents_utf8_sync("/proc/meminfo");

To execute a program `Subprocess` can be used.

1. Add `Gio` to the `imports`:

		:::javascript
		const Gio = imports.gi.Gio;

2. Indicate the command and its arguments, and retrieve the stdout to a variable:

		:::javascript
		let subprocess = new Gio.Subprocess({
			argv: ['/bin/df', '/'],
			flags: Gio.SubprocessFlags.STDOUT_PIPE,
		});
		subprocess.init(null);
		let [, out] = subprocess.communicate_utf8(null, null);

3. If pipes are needed, it is possible call a bash shell and pass as the argument the commands with pipes, for example:

		:::javascript
		let subprocess = new Gio.Subprocess({
			argv: ['/bin/sh', '-c', '/bin/df ' + '/' + ' | grep Filesystem -w -A1'],
			flags: Gio.SubprocessFlags.STDOUT_PIPE,
		});
		subprocess.init(null);
		let [, out] = subprocess.communicate_utf8(null, null);

### Drawing
[Cairo]() was used to draw all the visuals in my Desklet. The general idea is to create a canvas with Clutter, and use this canvas to add all the visual elements for the Desklet. For a working example, see the section **// draws graph** of the `update_draw()` function in the [`desklet.js`](https://github.com/linuxmint/cinnamon-spices-desklets/blob/master/system-monitor-graph%40rcassani/files/system-monitor-graph%40rcassani/desklet.js) for my Desklet.

### Wrap-up
This was an entertaining project, and my first time using JavaScript. Some final tips that I learned from this were:
* Once more, source control
* Test any small change
* Check the Errors printed in the Cinnamon console
* Learn from other people's code, the source code for all the [Deskets in Cinnamon](https://cinnamon-spices.linuxmint.com/desklets) spices is [here](https://github.com/linuxmint/cinnamon-spices-desklets).

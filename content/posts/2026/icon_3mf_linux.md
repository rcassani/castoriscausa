Title: Set icons for 3mf files in Linux
Date: 2026-11-23 16:43
Tags: Linux
Author: Raymundo Cassani
Slug: icon-3mf-linux
Thumbnail: icon_3mf_files.png

By default the icons for files `.3mf` are shown as a standard model file, e.g. `.stl`, at least in the Papirus icon package.

<center>
	<img src="https://raw.githubusercontent.com/PapirusDevelopmentTeam/papirus-icon-theme/refs/heads/master/Papirus/48x48/mimetypes/model-stl.svg" style="width: 48px;"/>
</center>


These instructions are done to update the icon of the `.3mf` files to the [Bambu Studio](https://bambulab.com/en-ca/download/studio) icon for the Papirus icon packages.

1. First, check that the [mimetype](https://en.wikipedia.org/wiki/MIME) name for `.3mf` already exist. It should be `3mf.xml` in `/usr/share/mime/model/`

2. Find all current icons for that mimetype

```bash
cd /usr/share/icons/Papirus
find . -name 'model-3mf.*'
```

3. Update each of the found icons to be a copy of the Bambu Studio icon with the same resolution.
Note: Most icon folders in Papirus-Dark and Papirus-Light are symbolic links from the ones in Papirus

```bash
cd /usr/share/icons/Papirus
sudo cp ./16x16/apps/bambustudio.svg ./16x16/mimetypes/model-3mf.svg
sudo cp ./22x22/apps/bambustudio.svg ./22x22/mimetypes/model-3mf.svg
sudo cp ./24x24/apps/bambustudio.svg ./24x24/mimetypes/model-3mf.svg
sudo cp ./32x32/apps/bambustudio.svg ./32x32/mimetypes/model-3mf.svg
sudo cp ./48x48/apps/bambustudio.svg ./48x48/mimetypes/model-3mf.svg
sudo cp ./64x64/apps/bambustudio.svg ./64x64/mimetypes/model-3mf.svg
```

4. Lastly, update the caches.

```bash
sudo gtk-update-icon-cache /usr/share/icons/Papirus
sudo gtk-update-icon-cache /usr/share/icons/Papirus-Dark
sudo gtk-update-icon-cache /usr/share/icons/Papirus-Light
```

⚠️ Updates in the Papirus icon packages are likely to overwrite these changes, so they would need to be applied again.

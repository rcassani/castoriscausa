Title: Matlab file association in Linux
Date: 2021-06-06 17:26
Tags: Linux, Matlab
Author: Raymundo Cassani
Slug: matlab-linux-file-association
Thumbnail: matlab_linux_files.png

<center>
<img src="/images/matlab_linux_files.png" style="height: 250px;"/>
</center>  

In contrast to [Matlab](https://www.mathworks.com/products/matlab.html) for Windows and macOS, Matlab for Linux does not automatically make the associations with its related files `.m`, `.mat`, and `.fig`. This post describes the how to do the association, it includes: 1. defining [MIME types](https://en.wikipedia.org/wiki/Media_type), 2. setting icons, and 3. creating [desktop entries](https://wiki.archlinux.org/title/Desktop_entries) (`.desktop` files to define Matlab as the application for these MIME types). I'm using Cinnamon as desktop environment (thus it should work in Gnome without changes), and Arch Linux distribution.

## Matlab shortcut in main Menu and Desktop
This is not necessary for the association, but it may play useful.

1. Copy Matlab icon file from the Matlab installation directory to the shared icons

        :::bash
        # cp /usr/local/MATLAB/R2020b/bin/glnxa64/cef_resources/matlab_icon.png /usr/share/icons

2.  Create a `matlab_2020b.desktop` file at `/usr/share/applications`

        :::bash
        [Desktop Entry]
        Type=Application
        Name=MATLAB 2020b
        Icon=/usr/share/icons/matlab_icon.png
        Exec=/usr/local/MATLAB/R2020b/bin/matlab -desktop
        Categories=Development
        Terminal=false

3. Change the permissions to be executable:

        :::bash
        # chmod +x matlab_r2020b.desktop

4. For the Desktop shortcut, just copy this `matlab_2020b.desktop` to `~/Desktop`

In this post describes the how to do the association, it includes: defining [MIME types](https://en.wikipedia.org/wiki/Media_type), setting icons, and creating [desktop entries](https://wiki.archlinux.org/title/Desktop_entries) (`.desktop` files to define Matlab as the application for these MIME types). I'm using Cinnamon as desktop environment (thus it should work in Gnome without changes), and Arch Linux distribution.

## Associate `.m`, `.mat` and `.fig` files with Matlab

### 1. MIME types
The MIME type for Matlab `.m` files is part of the `freedesktop.org.xml` file which is present in `/usr/share/mime/packages/`. Thus let's create the MIME types for `.mat` and `.fig`.

1. Create the file `/usr/share/mime/packages/matlab-typemimes.xml`

        :::xml
        <mime-info xmlns='http://www.freedesktop.org/standards/shared-mime-info'>
            <mime-type type="image/x-matlab-fig">
                <comment>MATLAB figure</comment>
                <magic priority="50">
                     <match value="MATLAB" type="string" offset="0"/>
                </magic>
                <glob pattern="*.fig" weight="60"/>
                <generic-icon name="matlab-fig"/>
            </mime-type>
            <mime-type type="application/x-matlab-data">
                <comment>MATLAB data file</comment>
                <magic priority="50">
                     <match value="MATLAB" type="string" offset="0"/>
                </magic>
                <glob pattern="*.mat" weight="60"/>
                <generic-icon name="matlab-mat"/>
            </mime-type>
        </mime-info>

    This MIME definition is based on [https://lists.freedesktop.org/archives/xdg/2010-October/011673.html](https://lists.freedesktop.org/archives/xdg/2010-October/011673.html)

2. Update MIME database
        :::bash
        # update-mime-database /usr/share/mime

### 2. Icons
The icons for `.mat` and `.fig` files is set to be the same as for `.m` files. In `/usr/share/icons/`, copy all the instances of `text-x-matlab.svg` as `image-x-matlab-fig.svg` and `application-x-matlab-data.svg`. And Run `gtk-update-icon-cache` for each of the icon directories.

    :::bash
    # find /usr/share/icons -name text-x-matlab.svg -execdir echo cp {} image-x-matlab-fig.svg ';'
    # find /usr/share/icons -name text-x-matlab.svg -execdir echo cp {} application-x-matlab-data-svg ';'
    # find -maxdepth 1 -type d -execdir gtk-update-icon-cache {} ';'

### 3. Desktop entries
Different Matlab files are called in different way by MATLAB:

    :::bash
    matlab -desktop -r "edit %f;"
    matlab -desktop -r "uiimport %f;"
    matlab -desktop -r "openfig %f;"

As such, it is necessary to create a desktop entry file for each MIME type reflecting how Matlab is called to open such MIME files. These files will be created in `/usr/share/applications`

File `matlab_2020b_m.desktop`

    :::bash
    Exec=/usr/local/MATLAB/R2020b/bin/matlab -desktop -r "edit %f;"
    MimeType=text/x-matlab
    NoDisplay=true

File `matlab_2020b_mat.desktop`

    :::bash
    Exec=/usr/local/MATLAB/R2020b/bin/matlab -desktop -r "uiimport %f;"
    MimeType=application/x-matlab-data
    NoDisplay=true

File `matlab_2020b_fig.desktop`

    :::bash
    Exec=/usr/local/MATLAB/R2020b/bin/matlab -desktop -r "openfig %f;"
    MimeType=image/x-matlab-fig
    NoDisplay=true

The `NoDisplay=true` prevents that these desktop entry files appear in the main Menu.

### Conclusion
Now the different Matlab files are associated with Matlab and opening them in the file explorer creates a new instance of Matlab and opens the selected file. Opening the file occurs in a *new* instance of Matlab ([link](https://www.mathworks.com/matlabcentral/answers/393093-execute-script-from-command-line-to-existing-matlab-instance)), In the future I'll look for alternatives to open the file in the current Matlab instance.


###References
[MIME types](https://en.wikipedia.org/wiki/Media_type)  
[Desktop entries](https://wiki.archlinux.org/title/Desktop_entries)  
[Matlab MIME types](https://lists.freedesktop.org/archives/xdg/2010-October/011673.html)  
[Adding MIME types in Gnome](https://developer.gnome.org/integration-guide/stable/mime.html)  

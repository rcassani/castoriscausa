Title: Anaconda Miniconda System Python
Date: 2016-12-06 19:00
Category: Blog
Tag: Template
Slug: template
Author: Ray Cassani
Lang: spa

1. Install [Anaconda(3)](link), do NOT append Anaconda directory to PATH

2. Go to your Anaconda directory
/home/cassani/anaconda3/bin

3. Create a empty environment

$ conda create --name empty-env

4. Add the directory bin of the empty-env environment to your .bashrc file
/home/cassani/anaconda3/envs/empty-env/bin

Important
You may want to create a symbolic link in ~/miniconda3/envs/empty-env/bin for conda-env
	$ ln -s /home/cassani/miniconda3/bin/conda-env conda-en

5. This will make the conda command avaiable from any terminal ,ad keeps the system pythons (python2 and python3) as fedault python

$ which python
$ which python3

To use the python with Anaconda, you need to explicityly activate the root environment

$ source activate root
(root) user@mint ~ $
Alternatively, you can create an environment with Anaconda and python3

$ conda create --name anaconda3 python=3 anaconda
and activate it

This environment will be located at
/home/cassani/anaconda3/envs/anaconda3

Ref:
https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/opMLiGnjymE
https://conda.io/docs/using/envs.html#share-an-environment
https://github.com/conda/conda/issues/1022


Q:
https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/opMLiGnjymE




for Qtodotxt
sudo apt-get -y install python3-dateutil

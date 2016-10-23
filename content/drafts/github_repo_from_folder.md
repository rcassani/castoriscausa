# Create a GitHub repository from a local one

1. You have a directory called NiceProject where all your files are
2. You want to share it with the world, and GitHub looks like a good option

## Steps:
1. You need to have Git installed in your PC
2. Go to inside NiceProject folder
3. Create a Git repository of your Project

[code language="bash"]
$git init
[/code]

Now you have a nice looking local repo

4. Add your files and Commit your work
[code language="bash"]
$git add --all
$git commit -m "First commit"
[/code]

5.Go to your GitHub, and create a New Repository 
* A good practice will be to write down the same name that your NiceProhject folder, it's more memorable

Do not add a README.md file 
Select .gitignore according to your project, if applies Do it if NiceProject folder does not have a README.md and .gitignore file, otherwise you'll need to solve the merging issues

6. Add the remote to the local Repo
[code language="bash"]
$git remote add origin URL
[/code]
URL is in GitHub clone 


7. Now, let get the files let merge the Remote Repo with the Local
[code language="bash"]
$git pull origin master
[/code]
This will merge your local repository with the one in GitHub
Ctrl+X to exit of the MERGE-MG

8. Set the push
git push --set-upstream origin master

Introduce your GitHub credentials

9 Tip. Save credentials
git config credential.helper store

10. If you do shanges in your NiceProject, just:

1. git commit -m "commit description"
2. git push



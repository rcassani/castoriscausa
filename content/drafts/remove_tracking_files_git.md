
How to successfully untrack files and folders, and delete them from remotes

Suppose you have a local repository as follows

-> repo
   -> folder 1
   -> folder 2
   -> folder 3

   also suppose this local repository has a remote in GitHub with the same
   structure.

However you want to untrack `folder2` for any reason, and also remove it from the remote

Steps:
Add Directory to .gitignore
git commit -m "gitignore edited to ignore something"
git rm -r --cached Directory
git commit -m "removing files something"
git push origin

Note that this will cause that the deletion is propagated in other local
repositories when they perform

ref:
http://arlocarreon.com/blog/git/untrack-files-in-git-repos-without-deleting-them/

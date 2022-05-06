Title: 7 steps for contributing a GitHub project    
Date: 2020-12-28 17:17
Modified: 2022-05-05 20:00
Tags: Git, GitHub, methods
Author: Raymundo Cassani
Slug: steps-contributing-github-project
Thumbnail: bike_7.jpg

### Congratulations!

It's amazing that you're thinking into contributing to an open-source project.
Contributions usually include:

* 🪲 Solving bugs
* ⭐ Development of new features
* 🗎 Improve documentation
* etc.  

Although the task seems intimidating, it can be broken into some simple steps. **First of all**, check if the project you want to contribute to has a `CONTRIBUTING` file. If it exists, this file presents the [guidelines for repository contributors](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/setting-guidelines-for-repository-contributors) for the project.

Let's assume the you (`YOUR-USERNAME`) want to contribute to a the project `COOL-PROJECT` which repository is in the `COOL-USERNAME` GitHub account. In general the process to contribute to an open-source project can be divided into 7 simple steps. These steps are expanded with great detail in this wonderful post: [https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/).

* **STEP 0**: When contributing, please **first discuss the change** you wish to make to the owner of the repository. A way to start this dicussion can be a [GitHub issue](https://github.com/brainstorm-tools/brainstorm3/issues).

* **STEP 1**: [Fork the repository](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) from `https://github.com/COOL-USERNAME/COOL-PROJECT` to your GitHub account and clone it to your computer.

        :::bash
        $ git clone https://github.com/YOUR-USERNAME/COOL-PROJECT.git

* **STEP 2**: Create a `upstream` remote (to this repository) and sync your local copy.

        :::bash
        $ git remote add upstream https://github.com/COOL-USERNAME/COOL-PROJECT
        $ git remote -v

    At this point the `origin` remote refers to your forked repository in your account (`https://github.com/YOUR-USERNAME/COOL-PROJECT`) and `upstream` to the original repository (`https://github.com/COOL-USERNAME/COOL-PROJECT.git`). To sync your `local` and `origin` repositories to the `upstream` repository, pull from `upstream`, and push to `origin`.

        :::bash
        $ git checkout master    
        $ git pull upstream master && git push origin master

* **STEP 3**: Create a branch in your `local` repository. This branch will contain your contribution.

        :::bash
        git checkout -b fixing-something


* **STEP 4**: Perform your contribution, write[good commit messages, and commit. If your contributions solves an open issue, [close it with the proper commit message](https://github.blog/2013-01-22-closing-issues-via-commit-messages/). **NOTE:** Make ONLY ONE contribution per branch.

* **STEP 5**: Push your `local` branch to your fork in GitHub (`https://github.com/YOUR-USERNAME/COOL-PROJECT`).

        :::bash
        git push -u origin fixing-something


* **STEP 6**: On GitHub, [create a new Pull Request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork) from your fork.  
  ⚠️ For greater collaboration, select the option [Allow edits by maintainers](https://docs.github.com/en/github/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork) before creating your PR. This will allow Brainstorm maintainers to add commits to your PR branch before merging it. You can always change this


* **STEP 7**: Provide feedback about the Pull Request, and if things are correct, your Pull Request will be merged  `upstream` repository.

### Example
An example of a `CONTRIBUTING` file listing these steps in an open-source project cab be found here: [https://github.com/brainstorm-tools/brainstorm3](https://github.com/brainstorm-tools/brainstorm3)

### Git and GitHub resources
AS you could read, contributing requiers to be familiar with [Git](https://git-scm.com/) and [GitHub](https://github.com/) concepts like: ***commit, branch, push, pull, remote, fork, repository***, etc. There are plenty resources online to learn Git and GitHub, for example:

- [Git Guide](https://github.com/git-guides/)
- [GitHub Quick start](https://docs.github.com/en/get-started/quickstart)
- [GitHub guide on YouTube](https://www.youtube.com/githubguides)
- [Git and GitHub learning resources](https://docs.github.com/en/get-started/quickstart/git-and-github-learning-resources)
- [Collaborating with Pull Requests](https://docs.github.com/en/github/collaborating-with-pull-requests)
- [GitHub Documentation, guides and help topics](https://docs.github.com/en/github)
- And many more...

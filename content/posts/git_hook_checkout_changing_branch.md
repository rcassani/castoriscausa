Title: Git hook at changing branches
Date: 2022-06-05 10:30
Modified: 2023-02-12 18:00
Tags: Bash, Git, Linux
Author: Raymundo Cassani
Slug: git-hook-checkout-changing-branch
Thumbnail: git_hook_branches.png

<hr>
**Updated**: The [post-checkout hook](https://git-scm.com/docs/githooks.html#_post_checkout) the hook code below is intended to run only when changing branches, but it is invoked also when **retrieving files from the index** and  **rebasing**. Thus these two cases need to be addressed in the code. See more details below.
<hr>

Often when working on experimental Git branches, it is necessary to modify files outside of the Git repository when we change branches to properly test some of the new features. An example of this type of files would be configuration files.

Through the use of [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) it is possible to execute a program when a Git action happens, for example when checkout occurs. However, the [post-checkout hook](https://git-scm.com/docs/githooks.html#_post_checkout) is given the [SHA-1 ref](https://git-scm.com/book/en/v2/Git-Internals-Git-References) of the **old** (origin) and **new** (destination) branches, rather than their name. Thus if two branches share the same HEAD, it's not possible to distinguish the correct branch only from the ref. A [walk-around](https://stackoverflow.com/a/25590292/4859684) is to use `git reflog` to get the names of the **old** and **new** branches.

<hr>
**Updated**: Note that the [post-checkout hook](https://git-scm.com/docs/githooks.html#_post_checkout) will be invoked when **retrieving a file from the index**, thus if `checkoutType == 0` the hooks returns before doing its action. The hook is also invoked by `git rebase`. For example, being in the **new** branch and rebasing it to **old**, this is to say `git rebase old`, will invoke the hook, the name of the **old** branch will be correctly identified by `git reflog`, but the **new** branch name will be empty. Thus if any of the branches is empty the hook exits without performing its action.
<hr>

This Bash script ([available here](https://gist.github.com/rcassani/5ff18bb1520a27f72d332385aa6220f2)) is a post-checkout hook example to do "something" **if** the **new** branch name is in a give list, function `exists_in_list()`. Moreover, it checks if the **old** or **new** branch names have `ftr-` as prefix, and takes does something for the different combinations, function `starts_with()`.

    bash
    {!> https://gist.githubusercontent.com/rcassani/5ff18bb1520a27f72d332385aa6220f2/raw !}

# Git Cheat Sheet
Cheat Sheet for Git commands version control, created by [bytecurl](https://github.com/bytecurl)
Modified by Christian Toderascu.

**last update: 20231017**

last update available on [GitHub - Git CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Git%20CheatSheet.md)
[link of the source](https://github.com/bytecurl/github-cheatsheet-markdown/tree/main)


![Image](/img/screenshot_github_cheat-sheet.png "Credits: GitHub, Inc. @ www.github.com")

Git is the free and open source distributed version control system that’s responsible for everything GitHub related that happens locally on your computer. This cheat sheet features the most important and commonly used Git commands for easy reference.


## INSTALLATION & GUIS

[http://git-scm.com](http://git-scm.com)

[Learn git branching](https://learngitbranching.js.org/)



## SETUP * CONFIGURE TOOLING

**Configuring user information used across all local repositories**

    $ git config --global user.name "[firstname lastname]"
Set a name that is identifiable for credit when review version history

    $ git config --global user.email "[valid email]"
Set an email address that will be associated with each history marker

    $ git config --global color.ui auto
Set automatic command line coloring for Git for easy reviewing

[Tutorial for ssh keys management](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

## SUMMARY to do a quick push

1. git status
2. git add *
3. git commit -m "message"
4. git push

## INIT * CREATE REPOSITORIES

**A new repository can either be created locally, or an existing repository can be cloned. When a repository was initialized locally, you have to push it to GitHub afterwards.**

    $ git init
The git init command turns an existing directory into a new Git repository inside the folder you are running this command. After using the git init command, link the local repository to an empty GitHub repository using the following command:

    $ git clone [url]
Retrieve or clone (download) a repository that already exists on GitHub, including all of the files, branches, and commits

## THE .gitignore FILE

> **Sometimes it may be a good idea to exclude files from being tracked with Git. This is typically done in a special file named .gitignore. You can find helpful templates for .gitignore files at [github.com/github/gitignore](https://github.com/github/gitignore).**

## SYNCHRONIZE CHANGES

**Synchronize your local repository with the remote repository on GitHub.com**

    $ git fetch
Downloads all history from the remote tracking branches. It does not change the state of the local files !

    $ git merge
Combines remote tracking branches into current local branch

    $ git push
Uploads all local branch commits to GitHub. Add -f if you want to force the deletion of the remote folder and put instead your local folder

    $ git pull
Updates your current local working branch with all new commits from the corresponding remote branch on GitHub. git pull is a combination of git fetch and git merge

## BRANCHES

**Isolating work in branches, changing context, and integrating changes git branch list your branches. a * will appear next to the currently active branch: Branches are an important part of working with Git. Any commits you make will be made on the branch you’re currently “checked out” to. Use git status to see which branch that is.**

    $ git branch [branch-name]
Creates a new branch

    $ git branch -a
Show a list of all current branch in local and remote

    $ git checkout [branch-commit-tag]
Switch to another branch and check it out into your working directory (position of your HEAD). 
    * Add `^<num>`  after [branch] in order to go up one commit at a time, the <num> is not mandatory but indicates the number of the parent at a merged commit (if not specified it's 1)
    * Add `~<num>` after [branch] in order to go up a number of commits specified by <num>

    $ git switch -c [branch-name]
Switches to the specified branch and updates the working directory

    $ git merge [branch-name]
Merges or combines the specified branch’s history into the current branch. This is usually done in pull requests, but is an important Git operation. Usually we merge [branch] after placing ourselves on the main branch.

    $ git branch -d [branch-name]
Deletes the specified branch

    $ git branch -m [branch-name]
Renames the current branch name

    $ git branch -f [branch-name] [commit-new]
Move a branch [branch-name] to another commit [commit-new]

    $ git branch -u origin/main [branch]
Set to follow the local [branch] for the remote branch main. If you want to follow another branch than main.

## STAGE & SNAPSHOT

**Working with snapshots and the Git staging area git status show modified files in working directory, staged for your next commit**

    $ git add [file]
Add a file as it looks now to your next commit (stage), use `*` to say all files and folders content

    $ git reset [file]
Unstage a file while retaining the changes in working directory. 

    $ git rm [file]
Delete the file from project and stage the removal for commit

    $ git rm --cached [file]
Stage the delete of the file for commit without deleting it locally. (Usefull if files where added to .gitignore)

    $ git mv [existing path] [new path]
Change an existing file path and stage the move

    $ git commit -m "[descriptive message]"
Commit your staged content as a new commit snapshot

    $ git commit --amend
todo

## Tagging a version of the code

    $ git tag
list the tags of your repo

    $ git tag -a [version] [commit]
tags mark forever certain commits like "milestone" (key steps) you can refer to them like branches. If you don't specify [commit], the tag is going to be placed at your HEAD. [version] can be for instance v1 or v1.2.3 
A vim text will open and you will be able to type your description of the tag. First line should be title of the tag, the next lines are details about the version. Type `:wq` to save and exit.

    $ git tag -d [version]
delete the tag [version]

    $ git push origin --tags
Transmit local tags to remote repo
    
## Logs and inspection of modifications

**Browse and inspect the evolution of project files**

    $ git status
Check the status of your repository to see what changes have been made

    $ git log
Show all commits in the current branch’s history. Lists version history for the current branch

    $ git log --all --decorate --oneline --graph
Shows a tree of all the commits of the repo. Taken from [Pretty Git branch graphs](https://stackoverflow.com/a/35075021)

    $ git log --follow [file]
Lists version history for a file, beyond renames (works only for a single file)

    $ git log [first-branch]..[second-branch]
Show the commits on first-branch that are not on second-branch

    $ git log --stat -M
Show all commit logs with indication of any paths that moved

    $ git diff
Diff of what is changed but not staged.

    $ git diff [file]
Diff of what is changed but not staged for the file [file].

    $ git diff --staged
Diff of what is staged but not yet committed, add option --name-only to get only the names of the files
    $ git diff [first-branch]...[second-branch]
Shows content differences between two branches

    $ git show [commit]
Outputs metadata and content changes of the specified commit

    $ git show [SHA]
Show any object in Git in human-readable format

    $ git describe [branch-commit]
Shows `<tag>_<numCommits>_g<hash>`, <tag> is the most recent tag, <numCommits> is the number of commits between [branch-commit] and the most recent tag, <hash> is the identifier of [branch-commit].
 

## IGNORING PATTERNS

**Preventing unintentional staging or committing of files**

    logs/
    *.notes
    pattern*/

Save a file with desired patterns as .gitignore with either direct string matches or wildcard globs.

    $ git config --global core.excludesfile [file]
System wide ignore pattern for all local repositories

## SHARE & UPDATE

**Retrieving updates from another repository and updating local repos**

    $ git remote add origin [url]
    $ git remote set-url origin [url]
Specifies the remote repository for your local repository. The url points to a repository on GitHub like this `git@github.com:GITHUB_USERNAME/REPO_NAME.git`

    $ git fetch [alias] [branch]
Fetch down all the remote branches [branch] from the remote repository [alias]. [alias] and [branch] are not mandatory, especially if your head is already at the main branch that is setup as following a remote branch.
    * [alias] in most cases it's `origin`
    * [branch] can be replaced by [source-remote-branch-commit]:[destination-local-branch-commit]. If you don't specify a source branch, you are creating then locally a new branch named after [destination-local-branch-commit]

    $ git rebase [branch-destination] [branch-source]
Apply any commits of current branch [branch-source] ahead of specified one [branch-destination]. It has the advantage of being able to keep a linear sequence of commits compared to [branch-destination] in order to have a more clear history of the repo.
    * -i option to make it interactive and specifically choose the commits you want to include and their order.
    * [branch-source] if not specified, the current HEAD is taken
    * Usually you rebase 2 times (if you can push to main in a distant repo)
        1. git rebase main bugFix
        2. git rebase bugFix main (doesn't do any change, just moves the main branch ahead)

    $ git merge [alias]/[branch]
Merge a remote branch into your current branch to bring it up to date

    $ git push
todo

    $ git push [alias] [branch]
Transmit local branch [branch] commits to the remote repository [alias] branch [branch]. [alias] and [branch] are not mandatory, by not specifying them, it uploads all the commits from the current branch.
    * [alias] in most cases it's `origin`
    * [branch] can be replaced by [source-local-branch-commit]:[destination-remote-branch-commit]. If you don't specify a source, you are deleting the [destination-remote-branch-commit]

    $ git pull
Fetch and merge any commits from the tracking remote branch: Updates your current local working branch with all new commits from the corresponding remote branch on GitHub. `git pull` is a combination of git fetch and git merge

    $ git pull --rebase
Fetch and rebase any commits from the tracking remote branch.

    $ git cherry-pick [Commit1] [Commit2] [...]
Copies a series of commits and puts them ahead of HEAD

    $ git reset [commit]
Undoes all commits after [commit], preserving changes locally

    $ git reset --hard [commit]
Clear staging area, rewrite working tree from specified commit

    $ git revert [commit]
Undoes all commits after [commit], and creates a new commit (to use remotely)


## TEMPORARY COMMITS

**Temporarily store modified, tracked files in order to change branches**

    $ git stash
Save modified and staged changes

    $ git stash list
List stack-order of stashed file changes

    $ git stash pop
Write working from top of stash stack

    $ git stash drop
Discard the changes from top of stash stack

## Glossary

- git: an open source, distributed version-control system
- GitHub: a platform for hosting and collaborating on Git repositories
- commit: a Git object, a snapshot of your entire repository compressed into a SHA
- branch: a lightweight movable pointer to a commit
- clone: a local version of a repository, including all commits and branches
- remote: a common repository on GitHub that all team members use to exchange their changes
- fork: a copy of a repository on GitHub owned by a different user
- pull request: a place to compare and discuss the differences introduced on a branch with reviews, comments, integrated tests, and more
- HEAD: representing your current working directory, the HEAD pointer can be moved to different branches, tags, or commits when using git switch

----

© 2022 GitHub, Inc.

























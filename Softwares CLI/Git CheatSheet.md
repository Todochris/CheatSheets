# Git Cheat Sheet
Cheat Sheet for Git commands version control, created by [bytecurl](https://github.com/bytecurl)
Modified by Christian Toderascu.

**last update: 20240327**

last update available on [GitHub - Git CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Git%20CheatSheet.md)  
[link of the source](https://github.com/bytecurl/github-cheatsheet-markdown/tree/main)


## installation & learning

* [http://git-scm.com](http://git-scm.com)
* [Learn git branching](https://learngitbranching.js.org/)
* [Git guide by medium](https://medium.com/@jake.page91/the-guide-to-git-i-never-had-a89048d4703a)
* [.gitignore templates](https://github.com/github/gitignore)

## SUMMARY to do a quick push

1. git status
2. git add *
3. git commit -m "message"
4. git push

## SUMMARY to create a new repo

1. git init
2. git add *
3. git commit -m "first commit"
4. git remote add origin git@github.com:GITHUB_USERNAME/REPO_NAME.git
5. git push --set-upstream origin main

Points 4. and 5. can be raplaced by `gh rep create` and accepting the creation of the remote "origin" using the [GitHub CLI tool "gh"](https://cli.github.com/)


## Create Repositories

| command       | description   |
| :------------ | :------------ |
| git init      | turns an existing directory into a new Git repository inside the folder
| git clone [url] | retrieves or clones a repository that already exists on GitHub, including all of the files, branches, and commits

## Synchronize Changes

| command        | description    |
| :------------  | :------------  |
| git fetch   | downloads all history from the remote tracking branches
| git merge   | combines remote tracking branches into current local branch
| git rebase  | applies local commits on top of the remote tracking branch
| git push    | uploads all local branch commits to GitHub
| git pull    | updates your current local working branch with all new commits from the corresponding remote branch on GitHub
| git pull --rebase   | Fetch and rebase any commits from the tracking remote branch.
|  -------------------- | :---------------------- |
| `git revert [commit]` | Undoes all commits after [commit], and creates a new commit (to use remotely)


Details:
    * [url] On GitHub, the url that points to the repo is like this `git@github.com:GITHUB_USERNAME/REPO_NAME.git`

`git rebase` details:
    * It has the advantage of being able to keep a linear sequence of commits compared to [branch-destination] in order to have a more clear history of the repo.
    * -i option to make it interactive and specifically choose the commits you want to include and their order.
    * [branch-source] if not specified, the current HEAD is taken
    * Usually you rebase 2 times (if you can push to main in a distant repo)
        1. git rebase main bugFix
        2. git rebase bugFix main (doesn't do any change, just moves the main branch ahead)

`git fetch` details:
    * [branch] can be replaced by [source-remote-branch-commit]:[destination-local-branch-commit]. If you don't specify a source branch, you are creating then locally a new branch named after [destination-local-branch-commit]

`git push` details:
    * [branch] can be replaced by [source-local-branch-commit]:[destination-remote-branch-commit]. If you don't specify a source, you are deleting the [destination-remote-branch-commit]


## Branches and commits

### Tracking

| command       | description   |
| :------------ | :------------ |
| git branch [branch-name] | creates a new branch
| git branch -a     | shows a list of all current branches in local and remote
| git switch [commit] | switches to the specified branch/commit and updates the working directory
| git checkout [commit] | switches to another branch and checks it out into your working directory
| git checkout tags/[tag-name] | checks out the specified tag and changes the working directory
| git branch -d [branch-name] | deletes the specified branch
| git branch -m [branch-name] | renames the current branch name
| git branch -f [branch-name] [commit-new] | moves a branch to another commit
| git branch -u origin/main [branch] | sets to follow the local branch for the remote branch


### Changes

| command       | description   |
| :------------ | :------------ |
| `git rebase [branch-destination] [branch-source]` | Apply any commits ahead of specified one [branch-destination].
| `git merge [branch-source]` | Merge the specified branch [branch-source] into the current branch
| `git cherry-pick [Commit1] [Commit2] [...]` | Copies a series of commits and puts them ahead of HEAD


## Selecting a commit

[commit] can be replaced by a [branch-name], a [tag-name] or a commit with or without indications

| [commit]      | description   |
| :------------ | :------------ |
| HEAD          | the current branch you are on
| HEAD~[n]      | the nth parent of the current branch (n=1 by default)
| HEAD^[n]      | the nth parent of the current branch on merged commits branches (where there are multiple parents)

## Stage & Snapshot

| command        | description    |
| :------------  | :------------  |
| git add [file] | adds a file as it looks now to your next commit (stage)
| git reset [file/commit] | unstages a file or a commit while retaining the changes in working directory
| git rm [file] | deletes the file from project and stages the removal for commit
| git rm --cached  [file] | stages the delete of the file for commit without deleting it locally
| git rm --ignore-unmatch [file] | avoid the error message if the file is not in the directory
| git mv [existing path] [new path] | changes an existing file path and stages the move
| git commit -m "[descriptive message]" | commits your staged content as a new commit snapshot
| git commit --amend | changes the last commit with the staged changes and a new message
| `git restore [file]`  | Discard changes in file from the working directory


## Tagging a version of the code

Tagging a commit like "a milestone" (key steps) you can refer to them like branches. If you don't specify [commit], the tag is going to be placed at your HEAD. [version] can be for instance v1 or v1.2.3

| command       | description  |
| :------------ |  :------------ |
| git tag     | List tags of your repo
| git tag -a [version] [commit] | Create a new annotated tag
| git tag -d [version] | Delete a tag
| git push origin --tags | Transmit local tags to remote repo


### To change the tag from a commit to the checked-out commit

| command       | description  |
|  :------------  |  :------------  |
| `git push origin refs/tags/<tagname>` | Delete the tag on any remote before you push |
| `git tag -fa <tagname>` | Replace the tag to reference the most recent commit |
| `git push origin --tags` | Push the tag to the remote origin |

## Logs and inspection of modifications

Browse and inspect the evolution of project files

| Command               | Description             |
| :-------------------- | :---------------------- |
| `git status`          | Check changes and stage of current repo
| `git log`             | Show all commits in the current branch's history. Lists version history for the current branch
| `git log --all --decorate --oneline --graph` | Shows a tree of all the commits of the repo.
| `git log --follow [file]` | Lists version history for a file, beyond renames (works only for a single file)
| `git log [branch1]..[branch2]` | Show the commits on first-branch that are not on second-branch
| `git log --stat -M`   | Show all commit logs with indication of any paths that moved
| `git diff`            | Diff of what is changed but not staged.
| `git diff [file]`     | Diff of what is changed but not staged for the file [file].
| `git diff --staged`   | Diff of what is staged but not yet committed, add option --name-only to get only the names of the files
| `git diff [branch1]...[branch2]` | Shows content differences between two branches
| `git ls-tree --full-tree -r --name-only HEAD` | List all the files in the HEAD commit
| `git show [commit]`   | Outputs metadata and content changes of the specified commit
| `git show [SHA]`      | Show any object in Git in human-readable format
| `git describe [commit]`| shows details about commmit
| `git blame [file]`    | Shows what revision and author last modified each line of a file
| `git reflog`          | List of actions that have been taken in the repository


`git describe` format is the following : `<tag>_<numCommits>_g<hash>`
    * <tag> most recent tag
    * <numCommits> number of commits between [commit] and the most recent tag
    * <hash> identifier of [commit].

## Temporary commits

Temporarily store modified, tracked files in order to change branches

| command       | description   |
|  :------------  |  :------------  |
| `git stash`   | Save modified and staged changes |
| `git stash list` | List stack-order of stashed file changes |
| `git stash pop` | Write working from top of stash stack |
| `git stash drop` | Discard the changes from top of stash stack |

## Setup and configure tooling

### Configuring user information used across all local repositories

    $ git config --global user.name "[firstname lastname]"
Set a name that is identifiable for credit when review version history

    $ git config --global user.email "[valid email]"
Set an email address that will be associated with each history marker

    $ git config --global color.ui auto
Set automatic command line coloring for Git for easy reviewing

    $ git config --global init.defaultBranch main
Set the default branch name for new repositories to main

    $ git config --global core.excludesfile [file]
System wide ignore pattern for all local repositories


## Remote repo configuration

| command       | description   |
| :------------ | :------------ |
| `git remote add origin [url]` | Specifies the remote repository for your local repository. 
| `git remote set-url origin [url]` | Specifies the remote repository for your local repository.


[Tutorial for ssh keys management](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)



### Preventing unintentional staging or committing of files

Save a file with desired patterns as .gitignore with either direct string matches or wildcard globs.

```
    logs/
    *.notes
    pattern*/
```




## Glossary

- git: an open source, distributed version-control system
- GitHub: a platform for hosting and collaborating on Git repositories
- fetch: download changes from remote repository to local repository (but not apply them)
- pull: refresh local repository with remote repository and applies them
- commit: a Git object, a local snapshot/save of your entire repository compressed into a SHA
- push: upload local repository content to a remote repository
- branch: a lightweight movable pointer to a commit
- clone: a local version of a repository, including all commits and branches
- remote: a common repository on GitHub that all team members use to exchange their changes
- fork: a copy of a repository on GitHub owned by a different user
- pull request: a place to compare and discuss the differences introduced on a branch with reviews, comments, integrated tests, and more
- HEAD: representing your current working directory, the HEAD pointer can be moved to different branches, tags, or commits when using git switch

----

























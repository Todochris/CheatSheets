# Git Cheat Sheet
Cheat Sheet for Git commands version control, created by [bytecurl](https://github.com/bytecurl)
Modified by Christian Toderascu.

**last update: 20240327**

last update available on [GitHub - Git CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Git%20CheatSheet.md)  
[link of the source](https://github.com/bytecurl/github-cheatsheet-markdown/tree/main)


## installation & learning

* [Git project](http://git-scm.com)
* [Install git and git-gui](git-scm.com/install/)
* [Learn git branching in an interactive way](https://learngitbranching.js.org/)
* [Git guide by medium](https://medium.com/@jake.page91/the-guide-to-git-i-never-had-a89048d4703a)
* [.gitignore templates](https://github.com/github/gitignore)

## SUMMARY to do a quick push

1. git status
2. git add .
3. git commit -m "message"
4. git push

Or, use `git gui` to do all these in a graphical user interface

## SUMMARY to create a new repo

1. git init
2. git add .
3. git commit -m "first commit"
4. git branch -M main
5. git remote add origin git@github.com:GITHUB_USERNAME/REPO_NAME.git
6. git push --set-upstream origin main

Points 5. and 6. can be raplaced by `gh repo create` by "Push an existing local repository to GitHub" and accepting the creation of the remote "origin" using the [GitHub CLI tool "gh"](https://cli.github.com/)


## Create Repositories

| command       | description   |
| :------------ | :------------ |
| git init      | turns an existing directory into a new Git repository inside the folder
| git clone [url] | retrieves or clones a repository that already exists on GitHub, including all of the files, branches, and commits
| git clone --recurse-submodules [url] | retrieves a repository and its submodules (if any)

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
-----------------------

### Tracking

| command       | description   |
| :------------ | :------------ |
| git branch [branch-name] | creates a new branch locally
| git push --set-upstream origin [branch-name] | create the created branch on the remote and set up tracking
| git branch -a     | shows a list of all current branches in local and remote
| git switch [commit] | switches to the specified branch/commit and updates the working directory
| git checkout [commit] | switches to another branch and checks it out into your working directory
| git checkout tags/[tag-name] | checks out the specified tag and changes the working directory
| git branch -d [branch-name] | deletes the specified branch
| git push origin --delete [branch-name] | deletes the specified branch from remote
| git branch -m [branch-name] | renames the current branch name
| git branch -f [branch-name] [commit-new] | moves a branch to another commit
| git branch -u origin/main [branch] | sets to follow the local branch for the remote branch


### Changes

| command       | description   |
| :------------ | :------------ |
| `git rebase [branch-destination] [branch-source]` | Apply any commits ahead of specified one [branch-destination].
| `git merge [branch-source]` | Merge the specified branch [branch-source] into the current branch
| `git cherry-pick [Commit1] [Commit2] [...]` | Copies a series of commits and puts them ahead of HEAD


### Selecting a commit

[commit] can be replaced by a [branch-name], a [tag-name] or a commit with or without indications

| [commit]      | description   |
| :------------ | :------------ |
| HEAD          | the current branch you are on
| HEAD~[n]      | the nth parent of the current branch (n=1 by default)
| HEAD^[n]      | the nth parent of the current branch on merged commits branches (where there are multiple parents)

## Stage & Snapshot
-------------------

| command        | description    |
| :------------  | :------------  |
| git add [file] | adds a file as it looks now to your next commit (stage)
| gid add --dry-run . | shows what will be added to the next commit without actually adding it
| git reset [file/commit] | unstages a file or a commit while retaining the changes in working directory
| git reset [commit] | change back to the specified commit (e.g. HEAD~) without discarding file changes
| git rm [file] | deletes the file from project and stages the removal for commit
| `git rm -r \*.pyc` | removes all files in subfolders that match the globbing pattern, `\*` is necessary to pass `*` from the shell to git
| git rm --cached  [file] | stages the delete of the file for commit without deleting it locally
| git rm --ignore-unmatch [file] | avoid the error message if the file is not in the directory
| git mv [existing path] [new path] | changes an existing file path and stages the move
| git commit -m "[descriptive message]" | commits your staged content as a new commit snapshot
| git commit --amend | changes the last commit with the staged changes and a new message
| `git restore [file]`  | Discard changes in file from the working directory


## Tagging & Versioning
-----------------------

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
---------------------------------------

Browse and inspect the evolution of project files

| Command               | Description             |
| :-------------------- | :---------------------- |
| `git status`          | Check changes and stage of current repo
| `git status -u`       | List all currently untracked files, and going in each directory
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

## Other useful concepts
------------------------


## Temporary commits

Temporarily store modified, tracked files in order to change branches

| command       | description   |
|  :------------  |  :------------  |
| `git stash`   | Save modified and staged changes (usually before changing branches) |
| `git stash list` | List stack-order of stashed file changes |
| `git stash pop` | Write working from top of stash stack |
| `git stash drop` | Discard the changes from top of stash stack |


## Submodules

each submodule can be treated as a separate repository and all git commands are available for them

| command       | description   |
| :------------ | :------------ |
| git submodule add [url] <destination> | Add a submodule to the repository, destination is better if it's a new folder making it the name of the submodule
| git submodule update --remote | Update the submodules to the latest commit
| git submodule deinit <submodule> | Remove a submodule from the repository
| git push --recurse-submodules=check | Push and check the submodules if they were also pushed

## Setup and configure tooling
------------------------------

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
| `git remote remove origin`    | Disconnect the repo from original remote (usefull when you pull a public repo that you want to work on your own
| `git remote -v`               | Check remote configuration

[url] On GitHub, the url that points to the repo is like this `git@github.com:GITHUB_USERNAME/REPO_NAME.git`


[Tutorial for ssh keys management](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)



## Gitignore

[.gitignore](https://gitbug.com/gitignore) examples for different languages and tools. It prevents unintentional staging or committing of files

Save a file with desired patterns as .gitignore with either direct string matches or wildcard globs in the main forlder of your repo.

```.gitignore
# ignore all . files and . folders
.*
# Dont ignore .gitignore (this file)
!/.gitignore
# Other type of files to ignore
logs/
*.notes
pattern*/
```


## Glossary

- General Terms
- Repository Management
- Branching & Merging
- Commits & Changes
- Remote Operations
- Staging & Working Directory
- History & Navigation
- Collaboration
- Advanced Concepts


**General Terms

- git: an open source, distributed version-control system
- GitHub: a platform for hosting and collaborating on Git repositories

**Repository Management**

- repository (repo): A directory containing your project files and the entire Git history.
- clone: Create a local copy of a remote repository on your machine.
- init: Initialize a new Git repository in an existing directory.
- fork: Create a personal copy of someone else's repository on your account.
- origin: Default name for the remote repository you cloned from.
- upstream: The original repository you forked from (used to sync changes).

**Branching & Merging**

- branch: A parallel version of your repository that diverges from the main working project.
- main/master: The default primary branch where the source code is kept.
- HEAD: A pointer to the current branch reference or commit you're working on.
- checkout: Switch between different branches or restore files.
- merge: Combine changes from different branches into one branch.
- fast-Forward: A merge where the target branch can simply move forward to the source branch.
- merge conflict: Occurs when Git cannot automatically resolve differences between branches.
- rebase: Move or combine commits to a new base branch, creating a linear history.
- cherry-pick: Apply a specific commit from one branch to another.

**Commits & Changes**

- commit: A snapshot of your repository at a specific point in time with a unique identifier (SHA).
- SHA/Hash: A unique 40-character identifier for each commit (usually shortened to 7 characters).
- commit message: Description of changes made in a commit.
- amend: Modify the most recent commit (message or content).
- diff: Shows differences between commits, branches, or files.
- patch: A file containing differences that can be applied to update code.

**Remote Operations**

- remote: A version of your repository hosted on the internet or network.
- push: Upload local commits to a remote repository.
- pull: Fetch and merge/apply changes from a remote repository to your local branch.
- fetch: Download changes from remote repository without merging/applying them.
- pull request (PR): A request to merge your changes into another branch (GitHub/GitLab terminology).
- merge request (MR): Same as Pull Request but used in GitLab.

**Staging & Working Directory**

- working directory: The directory on your computer where you're currently working on files.
- staging area (index): A holding area for changes you want to include in your next commit.
- stage: Add changes to the staging area before committing.
- unstage: Remove changes from the staging area.
- stash: Temporarily save uncommitted changes without committing them.
- tracked Files: Files that Git is monitoring for changes.
- untracked Files: New files that Git isn't monitoring yet.

**History & Navigation**

- log: View the commit history of your repository.
- reflog: Record of all changes to HEAD, useful for recovering lost commits.
- tag: A marker for a specific point in history (often used for releases).
- reset: Move the current branch to a different commit, potentially discarding changes.
- revert: Create a new commit that undoes changes from a previous commit.
- blame: Show who last modified each line of a file and when.
- bisect: Binary search through commit history to find when a bug was introduced.

**Collaboration**

- contributor: Someone who has contributed code or changes to a repository.
- maintainer: Person responsible for managing and maintaining a repository.
- code review: Process of examining code changes before merging.
- conflict resolution: Process of manually fixing merge conflicts.
- protected branch: A branch with restrictions on who can push or merge to it.

**Advanced Concepts**

- detached HEAD: State where HEAD points to a specific commit instead of a branch.
- submodule: A repository embedded inside another repository.
- subtree: Alternative to submodules for including external repositories.
- hooks: Scripts that run automatically at certain points in the Git workflow.
- worktree: Multiple working directories attached to the same repository.
- bare repository: A repository without a working directory (used for sharing).
- shallow clone: A clone with limited history to save space and time.
- squash: Combine multiple commits into a single commit.
- interactive rebase: Rebase with options to modify commits (edit, reorder, squash, etc.).















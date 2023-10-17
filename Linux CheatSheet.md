# Linux CheatSheet
Cheat Sheet for Linux/Bash terminal, created by someone_todo.
Modified by Christian Toderascu.

**last update: 20231017**

last update available on [GitHub - Linux CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Linux%20CheatSheet.md)  
[link of the source](todo)


## File commands

| command       | description   |
| :------------ | :------------ |
| ls            | directory listing
| ls -al        | formatted listing with hidden files
| ls -alt       | directory listing in chronological order
| ls -R         | recursivly read all the contents of a directory
| cd dir        | change directory to dir
| cd            | change to home
| cd -P Link    | change directory to Link (a symbolic link) through the real path
| pwd           | show current directory
| mkdir dir     | create a directory dir
| rm file       | delete file
| rm -r dir     | delete directory dir
| rm -f file    | force remove file
| rm -rf dir    | force remove directory dir /!\ /!\ /!\ use with extreme caution /!\ /!\ /!\
| dir           | with a "/" at the end means the content of the directory, without it means the directory
| cp file1 file2 | copy file1 to file2
| cp -r dir1 dir2 | copy dir1 to dir2; create dir2 if it doesn't exist
| mv source destination | rename or move "source" to "destination"
| mv source1 source2 destination/ | move multiple files to destination/
| ln -s path LinkName | create symbolic link to file 
| touch file    | create or update file
| cat > file    | places standard input into file
| more file     | output the contents of file
| head file     | output the first 10 lines of file
| tail file     | output the last 10 lines of file
| tail -f file  | output the contents of file as it grows, starting with the last 10 lines
| tree          | writes all the folder with its files in a tree structure starting from the current directory in the terminal
| echo          | look for files using pattern

### commands usefull with servers

| command       | description   |
| :------------ | :------------ |
| scp /origin/file username@server.address.com:/path/to/destination | to copy a file from the local system to the remote system in the terminal of the local system
| scp -r /path/to/file username@server.address.com:/path/to/destination | to copy a folder to a remote server

* `diff -rq origin/folder dest/folder` | checks the difference in content between 2 folders
    * r : option to check folder recursivly
    * q : brief mode, not checking line by line the differences
* `rsync -avu --delete --exclude="/.*" /origin/folder/ /dest/folder` | sync the content of a folder with a folder by only adding the new elements
    * `-avu` : archive (full directory) , verbose, update (skip files that are newer on the receiver)
    * `--delete` : deleting from destination what is not present in the source, /!\ dangerous /!\
    * `--exclude="/.*"` : excluding hidden files
    * `--dry-run` : only show what are the files that are planned to be sent without sending them

## File Permissions
| command       | description   |
| :------------ | :------------ |
|chmod octal file | change the permissions of file to octal, which can be found separately for user, group, and world by adding the following numbers

* 4 : read(r)
* 2 : write (w)
* 1 : execute (x)

| Examples      | description   |
| :------------ | :------------ |
| chmod 777 | read, write, execute for all
| chmod 755 | rwx for owner, rx for group and world For more options, see man chmod.

## Compression

| command       | description   |
| :------------ | :------------ |
| tar cf file.tar files | create a tar named file.tar containing files
| tar xf file.tar | extract the files from file.tar 
| tar czf file.tar.gz files | create a tar with Gzip compression
| tar xzf file.tar.gz | extract a tar using Gzip 
| tar cjf file.tar.bz2 | create a tar with Bzip2 compression
| tar xjf file.tar.bz2 | extract a tar using Bzip2 
| gzip file     | compresses file and renames it to file.gz
| gzip -d file.gz | decompresses file.gz back to file

## Process Management

| command       | description   |
| :------------ | :------------ |
| ps            | display your currently active processes 
| top           | display all running processes in the server (see more explanations in the Application section)
| kill pid      | kill process id pid
| killall proc  | kill all processes named proc !!! use with extreme caution !!!
| bg            | lists stopped or background jobs; resume a stopped job in the background
| fg            | brings the most recent job to foreground 
| fg n          | brings job n to the foreground
| exit          | exits current apps if running, otherwise to exit the connection to the server
| `| tee f.log` | to put at the end of a command to record the outputs (stdout)
| `|& tee f.log`| to put at the end of a command to record the stdout et stderr

### Launch background job

* `at now <<!`      to launch a job
* `atq`             to see the pending jobs
* `at -c JobNumber` to see the content of the job

## SSH

| command       | description   |
| :------------ | :------------ |
| ssh user@host | connect to host as user
| ssh -p port user@host | connect to host on port port as user
| ssh-copy-id user@host | add your key to host for user to enable a keyed or passwordless login

## Searching

| command       | description   |
| :------------ | :------------ |
| grep pattern files | search for pattern in files 
| grep -r pattern dir | search recursively for pattern in dir
| command       | grep pattern | search for pattern in the output of command
| locate file   | find all instances of file
| compgen -c    | list all commands available in the terminal

## System Info

| command       | description   |
| :------------ | :------------ |
| date          | show the current date and time 
| cal           | show this month's calendar 
| uptime        | show current uptime
| w             | display who is online
| whoami        | who you are logged in as
| finger user   | display information about user 
| uname -a      | show kernel information
| cat /proc/cpuinfo | cpu information
| cat /proc/meminfo | memory information
| man command   | show the manual for command
| df            | show disk usage
| du            | show directory space usage
| free          | show memory and swap usage
| whereis app   | show possible locations of app 
| which app     | show which app will be run by default
| quota -sv     | reports the disc space a user occupies on each filesystem and his/her allotted limits

## Network

| command       | description   |
| :------------ | :------------ |
| ping host     | ping host and output results
| whois domain  | get whois information for domain 
| dig domain    | get DNS information for domain 
| dig -x host   | reverse lookup host
| wget file     | download file
| wget -c file  | continue a stopped download


## Shortcuts

| command       | description   |
| :------------ | :------------ |
| Ctrl+C        | halts the current command
| Ctrl+Z        | stops the current command, resume with fg in the foreground or bg in the background 
| Ctrl+D        | log out of current session, similar to exit 
| Ctrl+W        | erases one word in the current line 
| Ctrl+U        | erases the whole line
| Ctrl+R        | research the last command containing a string of characters
| Ctrl+A        | go to the start of the line
| Ctrl+E        | go to the end of the line
| Ctrl+|
| Ctrl + L      | clear the terminal
| !!            | repeats the last command
| exit          | log out of current session

## Applications

`&` added at the end of a command to open a GUI app lets you still access the terminal

vim file | opens file in vim terminal
xdg-open . | opens the default Linux file manager
matlab -nodisplay -r "matlab_commands" -logfile matlab_code.log

### [tmux](https://github.com/tmux/tmux/wiki)
---------------------------------------------
CheatSheet from this [website](https://tmuxcheatsheet.com), modified by Christian Toderascu.

**Terminal multiplexer**

#### Sessions management from terminal
| command       | description   |
| :------------ | :------------ |
| tmux new | Start a new session from terminal
| tmux new -s mysession | Start a new session with the name mysession
| tmux kill-session -t mysession | kill/delete session mysession
| tmux kill-session -a | kill/delete all sessions but the current
| tmux kill-session -a -t mysession | kill/delete all sessions but mysession
| tmux ls | Show all sessions
| tmux a | Attach to last session
| tmux a -t mysession | Attach to a session with the name mysession

#### Session management inside tmux
| command       | description   |
| :------------ | :------------ |
| :             | to input a command, use `:` instead of `tmux` if you are already connected to a tmux session
| Ctrl+b $      | Rename session
| Ctrl+b d      | Detach from session
| :attach -d    | Detach others on the session (Maximize window by detach other clients)
| Ctrl+b s      | Show all sessions
| Ctrl+b w      | Session and Window Preview
| Ctrl+b (      | Move to previous session
| Ctrl+b )      | Move to next session
| Ctrl+b [      | Enter scroll mode, quit with `q`


#### Windows management
| command       | description   |
| :------------ | :------------ |
| tmux new -s mysession -n mywindow | start a new session with the name mysession and window mywindow
| Ctrl+b c      | Create window
| Ctrl+b ,      | Rename current window
| Ctrl+b &      | Close current window
| Ctrl+b w      | List windows
| Ctrl+b p      | Previous window
| Ctrl+b n      | Next window
| Ctrl+b 0 ... 9| Switch/select window by number
| Ctrl+b l      | Toggle last active window
| :swap-window -s 2 -t 1 | Reorder window, swap window number 2(src) and 1(dst)
| :swap-window -t -1 | Move current window to the left by one position

#### Panes management from terminal
| command       | description   |
| :------------ | :------------ |
| Ctrl+b ;      | Toggle last active pane
| Ctrl+b %      | Split pane with horizontal layout |
| Ctrl+b "      | Split pane with vertical layout  –––
| Ctrl+b {      | Move the current pane left
| Ctrl+b }      | Move the current pane right
|===============|===============
| Ctrl+b ↑      | Switch to pane to the direction
| Ctrl+b ↓      | Switch to pane to the direction
| Ctrl+b →      | Switch to pane to the direction
| Ctrl+b ←      | Switch to pane to the direction
|===============|===============
| :setw synchronize-panes | Toggle synchronize-panes(send command to all panes)
|===============|===============
| Ctrl+b Spacebar | Toggle between pane layouts
| Ctrl+b o      | Switch to next pane
| Ctrl+b q      | Show pane numbers
| Ctrl+b q 0 ... 9 | Switch/select pane by number
| Ctrl+b z      | Toggle pane zoom
| Ctrl+b !      | Convert pane into a window
|===============|===============
| Ctrl+b+↑      | Resize current pane height(holding second key is optional)
| Ctrl+b+↓      | Resize current pane height(holding second key is optional)
| Ctrl+b+→      | Resize current pane width(holding second key is optional)
| Ctrl+b+←      | Resize current pane width(holding second key is optional)
|===============|===============
| Ctrl+b x      | Close current pane

#### configuration file
in ~/.tmux.conf
```
# Enable mouse mode (tmux 2.1 and above)
set -g mouse on

# Sets the scroll-back history limit
set-option -g history-limit 10000
```

### [top](https://ss64.com/osx/top.html)
-------
Those option can be specified either in the command line before executing `top` with the addition of a `-` at the start of each option [in MacOs](https://ss64.com/osx/top.html), or they can be typed during execution in [Linux](https://www.man7.org/linux/man-pages/man1/top.1.html) and MacOs
* `o` order the process display to sort by the input key
    * pid
    * cpu
    * mem (physical memory footprint)
    * vsize (total memory size)
* `s` order the process display to hae a certain delay in seconds between each update
* `U` only show the processes owned by the user


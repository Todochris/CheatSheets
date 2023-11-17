# Linux CheatSheet
Cheat Sheet for Linux/Bash terminal, created by someone_todo.
Modified by Christian Toderascu.

**last update: 20231017**

last update available on [GitHub - Linux CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Linux%20CheatSheet.md)  
[link of the source](todo)


## File commands

| command       | description   |
| :------------ | :------------ |
| ls            | listing directory contents
| ls -al        | listing directory contents -l for long-listing -a for hidden files
| cd dir        | change directory to dir
| cd            | change directory to home
| cd -P Link    | change directory to Link (a symbolic link) through the real path
| pwd           | show current directory
| mkdir dir     | create a directory dir
| rm file       | delete file
| unlink file   | delete only one file (prefer using it for symbolic links)
| rm file       | delete file 
| rm -r dir     | remove directory dir recursivly
| rm -i path    | ask for confirmation before removing files/directory from path
| dir           | with a "/" at the end means the content of the directory, without it means the directory
| cp file       | copy file1 to file2
| cp -R dir     | copy dir1 to dir2; create dir2 if it doesn't exist
| mv source destination | rename or move "source" to "destination"
| mv source destination/ | move source inside destination/
| ln -s path LinkName | create symbolic link to path named LinkName in the current directory. Create, prefer the use of `unlink` to delete a symbolic link
| touch file    | create or update file
| cat > file    | places standard input into file
| more file     | output the contents of file page by page
| less file     | output the contents of file, but with more options
| head file     | output the first 10 lines of file
| tail file     | output the last 10 lines of file
| tail -f file  | output the contents of file as it grows, starting with the last 10 lines
| tree          | writes all the folder with its files in a tree structure starting from the current directory in the terminal
| man command   | show the manual for command, to save the manual : `man command | col -b > command.txt` (sometimes the manual is available throuh `command --help` or `command -h`)
| env           | print all the environment variables check [User environment variables](#user-environment-variables) for explanations of some variables
| file path     | check the type of file (text, binary, etc.)
| wc file       | print the number of lines, words and bytes in file


### commands usefull with servers

| command       | description   |
| :------------ | :------------ |
| scp /origin/file username@server.address.com:/path/to/destination | copy file/directory over ssh protocol
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
`chmod [octal] [file]` 
changes the permissions of file to octal, which can be found separately for user (u), group (g), and world (o) by adding the following numbers or by specifying u, g or o and +(adding) or -(removing) and then the type of permision r, w or x instead of the octal (e.g. u+x for adding permission of execution to the user)

* 4 : read(r)
* 2 : write (w)
* 1 : execute (x)

`chown -<option> [new_owner] [file]`
change file owner and group

`ls -l <path>` shows the permission in the format `<file_type><user_permission><group_permision><world_permission>`
* fily_type
    * - : regular file
    * d : directory
    * l : symbolic link
* user_permission rwx


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
| `ps aux  | grep foo` | display the processes related to `foo`
| top           | display all running processes in the server (see more explanations in the Application section)
| kill -SIGTERM <pid>   | kill process id pid
| kill -SIGKILL <pid>   | kill process id pid forcefully
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
| ssh-keygen    | generate private/public key (`id_rsa`/`id_rsa.pub`) rsa 3072 bits key type by default
| ssh-add       | add private key identities to the authentication agent on the terminal
| ssh-add -L    | list all the public keys that are known to the authentication agent (ssh-agent)

## Searching

searching uses regex (Regular expression) to find patterns in the files

| command       | description   |
| :------------ | :------------ |
| grep [regex] files | search for regex in files 
| grep -r [regex] dir | search recursively for regex in dir
| `command | grep [regex]` | search in the output of command using regex
| find ~ -name [name] | search for all instances of file under the ~ directory
| locate [file]   | find all instances of file using the Linux Database (more of a system admin utility, needs to be updated with `sudo updatedb` before using it)
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
| less /proc/cpuinfo | cpu information (can replace less by vi, more, cat, ...)
| less /proc/meminfo | memory information
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

## Ohter commands

| command       | description   |
| :------------ | :------------ |
| history       | show the history of the commands used in the terminal
| id            | show the user id and group id
| ps $$         | show the flavour ofthe terminal or the CLI (Command Line Interpreter)
| visudo        | edit the sudoers file
| ureradd user  | add a user
| alias         | check all the commands aliases in the terminal (normally configured in the .bashrc file)
| date +%Y%m%d  | print the date in the format YYYYMMDD


## User environment variables

to get to those set variables, you just need to typ `echo $variable` in the terminal. All variables are printed with the command `env`.

| variable      | description   |
| :------------ | :------------ |
| PATH          | show your current PATH
| HOME          | show your home directory
| USER          | show your username
| SHELL         | show your current shell
| `<variable_name>=<value>` | set a new variable with the name variable_name and the value value
| `"$<variable_name>"` | to use the value of a variable in a command, use the variable name with a `$` in front of it
| command1 $(command2)    | to use the output of command2 in command1

## File globbing (named "simple pattern" in this CheatSheet)

Substitution characters interpreted by the shell to generate file names. It is not regex (Regular expression) !
| character(s)  | description   |
| :------------ | :------------ |
| `*`           | match 0 or more characters
| `?`           | match 1 character
| `[abc]`       | match one of the characters listed 
| `[!abc]`      | match any character not listed 
| `[a-z]`       | match one character in the range 
| `{t1,t2}`     | match one word in the list


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
Those option can be specified either in the command line before executing `top` with the addition of a `-` at the start of each option [in MacOs](https://ss64.com/osx/top.html), or they can be typed during execution in [Linux](https://www.man7.org/linux/man-pages/man1/top.1.html) and MacOs
* `o` order the process display to sort by the input key
    * pid
    * cpu
    * mem (physical memory footprint)
    * vsize (total memory size)
* `s` order the process display to hae a certain delay in seconds between each update
* `U` only show the processes owned by the user


## Directory structure in linux

| directory     | description   |
| :------------ | :------------ |
| /             | is called the “root directory”
| /bin:         | contains binaries of basic commands
| /sbin:        | contains binaries of advanced commands (reserved to administrators)
| /etc:         | contains the configuration files
| /home:        | that's where users have their personal files
| /var:         | data generated by the system and its applications (mainly logfiles, databases,...)
| /tmp:         | contains temporary files, all users have write access


## Bash scripting
```bash
if [condition1]
then
    # code if condition1 is true
elif [condition2]
then
    # code if condition2 is true
else
    # code if condition is false
fi
```

`bash script.sh arg1 arg2` to call a bash script with arguments
```bash
arg1 = $1 # get the first argument of the script
arg2 = $2 # get the second argument of the script
```

```bash
for i in {1..10}
do
# Modify the filename
matlab_command="startup_server('DATA/examples/simple_geo01','simple_geo_${i}')"

# Call the MATLAB script using nohup
at now <<! 
matlab -nodisplay -r "${matlab_command}"
!

done
```


##Details for commands
----------------------

### `ls -<option> <path>`
List the content of the path with the option. The path is optional and it can be a simple pattern.

| option        | description   |
| :------------ | :------------ |
| l             | long format including permissions, owner, size, last modification, and the filename
| a             | all content
| t             | time directory listing contents in chronological order of last modification
| S             | size of files order of listing
| h             | human readable file sizes (MB, GB, etc.)
| R             | recursivly read all the contents of a directory (using tree is better)

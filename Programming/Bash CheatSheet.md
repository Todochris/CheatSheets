# Bash CheatSheet
Cheat Sheet for Linux/Bash terminal.
Modified by Christian Toderascu.

**last update: 20231017**

last update available on [GitHub - Bash CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Bash%20CheatSheet.md)  


## File commands

| command       | description   |
| :------------ | :------------ |
| ls            | listing directory contents
| ls -al        | listing directory contents -l for long-listing -a for hidden files check [this section](## Details for commands) for more
| cd dir        | change directory to dir
| cd            | change directory to home
| cd -P Link    | change directory to Link (a symbolic link) through the real path
| cd ../..      | go up 2 levels
| pwd           | show current directory (print working directory)
| mkdir dir     | create a directory dir (make directory)
| touch file    | create or update file
| rm file       | delete file
| unlink file   | delete only one file (prefer using it for symbolic links)
| rm file       | delete file 
| rm -r dir     | remove directory dir recursivly
| rm -i path    | ask for confirmation before removing files/directory from path
| dir           | with a "/" at the end means the content of the directory, without it means the directory
| cp file1 file2| copy file1 to file2
| cp -R dir     | copy dir1 to dir2; create dir2 if it doesn't exist
| mv source destination | rename or move "source" to "destination"
| mv source destination/ | move source inside destination/
| ln -s path LinkName | create symbolic link to path named LinkName in the current directory. Create, prefer the use of `unlink` to delete a symbolic link
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
* `rsync -avu --delete --exclude="/.*" /origin/folder/ /dest/folder` | sync the content of a folder with a folder by only adding the new elements. More details in [this section](##Details-for-commands)
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
| find ~ -name "globing_pattern" | search for all instances of name under the ~ directory using globing pattern
| find . -type f -name "*.log" | find all the files with the extension .log in the current directory
| find . -type f -name "*.log" -exec rm -f {} \; | find all the files with the extension .log in the current directory and delete them
| sudo updatedb | update the Linux Database (used by the locate command)
| locate [file]   | find all instances of file using the Linux Database 
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

## Other commands

| command       | description   |
| :------------ | :------------ |
| history       | show the history of the commands used in the terminal
| id            | show the user id and group id
| ps $$         | show the flavour ofthe terminal or the CLI (Command Line Interpreter)
| visudo        | edit the sudoers file
| ureradd user  | add a user
| alias         | check all the commands aliases in the terminal (normally configured in the .bashrc file)
| date +%Y%m%d  | print the date in the format YYYYMMDD
| ip -c address | show the ip address of the server
| ip -c route | show the routing table of the server
| nmcli device show | show the network devices of the server
| curl https://ipinfo.io | show the public ip address behind a router
| du -sh ./* ./.* | show the size of all files and directories in the current directory


**advaced commands**

`sudo du -xh -d 1 /directory1 /directory2 | sort -h` : sorts by size all the folders in directory1 and directory2


## User environment variables

to get to those set variables, you just need to typ `echo $variable` in the terminal. All variables are printed with the command `env`.

| variable      | description   |
| :------------ | :------------ |
| PATH          | show your current PATH
| HOME          | show your home directory
| USER          | show your username
| SHELL         | show your current shell
| `variable_name=value` | set a new variable with the name variable_name and the value value, don't put spaces !
| `"$variable_name"` | to use the value of a variable in a command, use the variable name with a `$` in front of it
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
tmux new -s mysession | Start a new session with the name mysession
tmux a -t mysession | Attach to a session with the name mysession
tmus ls | list all the sessions



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
-----------------

To call a bash script with arguments arg1 and arg2 : `bash script.sh arg1 arg2`
```bash
arg1 = $1 # get the first argument of the script
arg2 = $2 # get the second argument of the script
num_args = $# # get the number of arguments
```

To use a command as a variable:
```bash
$(command)
```

To lauch a script in the background:
```bash
for i in {1..10} ; do
# Modify the filename
matlab_command="startup_server('DATA/examples/simple_geo01','simple_geo_${i}')"

# Call the MATLAB script using nohup
at now <<! 
matlab -nodisplay -r "${matlab_command}"
!

done
```

### Bash conditional expressions

```bash
if [condition1] ; then
    # code if condition1 is true
elif [condition2] ; then
    # code if condition2 is true
else
    # code if condition is false
fi
```

[condition] can be replaced either by an arithmetic expression between variables that has to be between double brackets `[[ condition ]]` (don't forget the spaces !!!)

| expression    | description   |
| :------------ | :------------ |
| -eq           | equal
| -ne           | not equal
| -lt           | less than
| -le           | less or equal
| -gt           | greater than
| -ge           | greater or equal


[codition] can also be replaced by the test command `test -[option] [target]`

| `-[option] [target]`  | description   |
| :-------------------- | :------------ |
| -f [file]             | file exists and is a regular file
| -d [file]             | file exists and is a directory




## Details for commands
----------------------

### `ls -<option> <path>`
List the content of the path with the option. The path is optional and it can be a simple pattern.

| option        | description   |
| :------------ | :------------ |
| l             | long format including permissions, owner, size, last modification, and the filename
| a             | all content
| R             | recursivly read all the contents of a directory (using tree is better)
| t             | time directory listing contents in chronological order of last modification
| S             | size of files order of listing
| h             | human readable file sizes (MB, GB, etc.)
| R             | recursivly read all the contents of a directory (using tree is better)
| 1            | list line by line


### `rsync -<option> <source_path> <destination_path>

| option        | description   |
| :------------ | :------------ |
| v             | verbose
| a             | archive mode (looking into directories, taking symlinks, permissions,...)
| u             | update (skip files that are newer on the receiver)
| h             | human-readable format for file sizes for instance
| i             | Requests a simple itemized list of the changes that are being made
              to each file, including attribute changes

**i option output string `YXcstpogz`**

* Y is replaced by the updated type
    * `<` means that a file is being transferred to the remote host (sent).
    * `>` means that a file is being transferred to the local host (received).
    * `c` means that a local change/creation is occurring for the item (such as the creation of a directory or the changing of a symlink, etc.).
    * `h` means that the item is a hard link to another item (requires --hard-links).
    * `.` means that the item is not being updated (though it might have attributes that are being modified).
* X stands for the file type
    * `f` for a file
    * `d` for a directory
    * `L` for a symlink
    * `D` for a device
    * `S` for a special file (e.g. named sockets and fifos).
* cstpogz stand for the reason of the update, 
    - if some reasons for update are not met, the letter are replaced by a `.`
    - if a newly created item, the letters are replaced with a "+", 
    - if an identical item exists, the letters are replaced with spaces\n
    * `c` means the checksum of the file is different and will be updated by the __file transfer__ (requires --checksum).
    * `s` means the size of the file is different and will be updated by the __file transfer__.
    * `t` means the modification time is different and is being updated to the sender's value (requires --times).  An alternate value of T means that the time will be set to the transfer time, which happens anytime a symlink is transferred, or when a file or device is transferred without --times.
    * `p` means the permissions are different and are being updated to the sender's value (requires --perms).
    * `o` means the owner is different and is being updated to the sender's value (requires --owner and super-user privileges).
    * `g` means the group is different and is being updated to the sender's value (requires --group and the authority to set the group).
    * `z` slot is reserved for future use.


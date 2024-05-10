# Terminal apps CheatSheet
Cheat Sheet for apps available in the terminal
Created by Christian Toderascu.

**last update: 20231220**

last update available on [GitHub - todo CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/todo%20CheatSheet.md)  
[link of the source](todo)


## Mac terminal (zsh)

`arch x86_64 <command>` at the start of the command to run apps with the x86 interpreter\n
`arch arm64 <command>` at the start of the command to run apps with the arm interpreter
`mdfind <search_keyword>` making a spotlight research



## [tmux](https://github.com/tmux/tmux/wiki)
---------------------------------------------
CheatSheet from this [website](https://tmuxcheatsheet.com), modified by Christian Toderascu.

**Terminal multiplexer**

### Sessions management from terminal
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

### Session management inside tmux
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


### Windows management
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

### Panes management from terminal
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

### configuration file
in ~/.tmux.conf
```
# Enable mouse mode (tmux 2.1 and above)
set -g mouse on

# Sets the scroll-back history limit
set-option -g history-limit 10000
```

## [top](https://ss64.com/osx/top.html)
--------

Those option can be specified either in the command line before executing `top` with the addition of a `-` at the start of each option [in MacOs](https://ss64.com/osx/top.html), or they can be typed during execution in [Linux](https://www.man7.org/linux/man-pages/man1/top.1.html) and MacOs
* `o` order the process display to sort by the input key
    * pid
    * cpu
    * mem (physical memory footprint)
    * vsize (total memory size)
* `s` order the process display to have a certain delay in seconds between each update
* `U` only show the processes owned by the user


to show only specific processes : 
```bash
top -l 1 -stats pid,command,cpu,time,th,pstate | grep -E "PID|command1|command2"
top -pid <command1_pid> -pid <command2_pid> -stats pid,command,cpu,time,th,pstate
```

## [ghostscript](https://ghostscript.readthedocs.io/en/latest/Use.html#use-html)
----------------

**Conversion of vector type files$$

gs [options] {filename 1} ... [options] {filename N} ...

**additional utilities installed**
ps2pdf, pdf2ps, ps2epsi, pdf2dsc, ps2ascii, ps2ps and ps2ps2

Convert .ps or .eps to .pdf
```bash
ps2pdf -dEPSCrop <input.ps> <output.pdf>
```

Convert all .eps files to .pdf
``` bash
ps2pdf -dEPSCrop *.eps
```

## [diskutil](https://ss64.com/osx/diskutil.html)
-------------

| command       | description   |
| :------------ | :------------ |
| diskutil list | list all disks and partitions
| diskutil info <disk> | info about a disk
| `diskutil info <disk#s#>` | info about the partition disk#s#
| diskutil eraseDisk MS-DOS "DRIVE" GPT <disk/path> | erase disk and name it DRIVE and use the partition table GPT
| diskutil eraseDisk MS-DOS "DRIVE" MBR <disk/path> | erase disk and name it DRIVE and use the partition table MBR
| diskutil eraseDisk MS-DOS "DRIVE" MBR <disk/path> | erase disk and name it DRIVE and use the default partition table (mac)



## [lynx]()

todo

## [imagemagick]()

todo

## [pandoc]()

`pandoc <input_file.ext> -o <output_file.ext>`

`pandoc --from=gfm <input_file>.md -o <output_file.ext>`


## [openshot video editor]()

todo


## [calibre]()

Commands :

* calibre
* calibre-customize
* calibre-debug
* calibre-server
* calibre-smtp
* calibredb
* ebook-convert
* ebook-edit
* **ebook-meta**
* ebook-polish
* ebook-viewer
* fetch-ebook-metadata
* lrf2lrs
* lrfviewer
* lrs2lrf
* web2disk
* ebook-device
* markdown-calibre



## [sortgs](https://github.com/WittmannF/sort-google-scholar)

```bash
sortgs "keywords" OR "KEYWORDS" --sortby "cit/year" --nresults 200
```

Other `--sortby` options are:
* `Citations` (default)
* `Rank` (given by google scholar)
* `Author`
* `Title`
* `Year`
* `Publisher`
* `Venue`
* `Source`





## [exiftool]()

to update research files (print the files to pdf if they are giving errors):
```bash
exiftool -all= *.pdf
```


## [Node.js](https://nodejs.org/en/)

```bash
npm # display help
npm ls # list all installed packages
```

## [Mermaid](https://github.com/mermaid-js/mermaid-cli)
------------

```bash
mmdc -h # display help
mmdc -i 'gantt chart.txt' -o '3D TRC M3 gantt chart.png' -w 1200
    # convert gantt chart to png (o: output, w: width)
```


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


## [yt-dlp]()

```bash
yt-dlp -F <url> # list all formats
yt-dlp -f <format_id> <url> # download the video in the format specified
```






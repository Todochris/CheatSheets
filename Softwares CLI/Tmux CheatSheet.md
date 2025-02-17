# Tmux CheatSheet
Cheat Sheet for tmux inspired by this [website](https://tmuxcheatsheet.com).
Modified by Christian Toderascu.

**last update: 20231220**

last update available on [GitHub - Tmux CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Tmux%20CheatSheet.md)  

[tmux](https://github.com/tmux/tmux/wiki) is a terminal multiplexer, allowing to create terminal sessions from which you can detach and reattach at will.

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
| Ctrl+b :             | to input a command, use `:` instead of `tmux` if you are already connected to a tmux session
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
| Ctrl+b+↑      | Resize current pane height
| Ctrl+b+↓      | Resize current pane height
| Ctrl+b+→      | Resize current pane width
| Ctrl+b+←      | Resize current pane width
| :resize-p -U 10 | Resize current pane height by 10
| :resize-p -D 10 | Resize current pane height by 10
| :resize-p -L 10 | Resize current pane width by 10
| :resize-p -R 10 | Resize current pane width by 10
| Ctrl+b Esc+↑  | Resize current pane height (for Mac terminal app)
| Ctrl+b Esc+↓  | Resize current pane height (for Mac terminal app)
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

In terminal of Mac, you will not be able to copy past to your system clipboard  
In XTerm (XQuartz), you can hold `Shift` and select text to copy, and middle click to paste.

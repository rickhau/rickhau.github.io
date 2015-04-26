---
layout: post
title: "Screen command 列表"
date: 2015-04-26 12:58:45 +0800
comments: true
categories:
---
### Screen command usage & COM port

#### Manipulate Sessions
- Open a screen session<br />
  cmd: **screen**<br />
  cmd: **screen -S sessionName** (Note: screen -S newSession)<br />
- Create a new screen session<br />
  cmd: **ctrl + a + c**
- Switch between 2 sessions (now and last)<br />
  cmd: **ctrl + a + a**
- Switch to the session number you created<br />
  cmd: **ctrl + a + 2**<br />
  (Note: 2 or other session number you created earlier)
- Session information<br />
  cmd: **ctrl + a + i**
- List all windows<br />
  cmd: **ctrl + a + w**

#### Detach/Re-attach bundle
- Detach session<br />
  cmd: **ctrl + a + d**
- Reattach session<br />
  cmd: **screen -r**

#### Robust de-attach session
- Force Deattach session<br />
  cmd: **screen -D**

#### Exit session
- Close session<br />
  cmd: **ctrl + a + k**
- Kill session<br />
  cmd: **ctrl + a + \**

##### Summary Table

|screen command     | Task
|:------------------|:-----------------------------------------------------|
|Ctrl+a c           |  Create new window
|Ctrl+a k           |  Kill the current window / session
|Ctrl+a w           |  List all windows
|Ctrl+a 0-9         | Go to a window numbered 0 9, use Ctrl+a w to see number
|Ctrl+a Ctrl+a      | Toggle / switch between the current and previous window
|Ctrl+a S           | Split terminal horizontally into regions and press
|Ctrl+a :resize     | Resize region
|Ctrl+a :fit        | Fit screen size to new terminal size. You can also hit Ctrl+a F for the the same task
|Ctrl+a :remove     |  Remove / delete region. You can also hit Ctrl+a X for the same taks
|Ctrl+a tab         | Move to next region
|Ctrl+a D (Shift-d) |  Power detach and logout
|Ctrl+a d           |   Detach but keep shell window open
|Ctrl-a Ctrl-\      |  Quit screen
|Ctrl-a ?           | Display help screen i.e. display a list of commands

#### Screen with COM port (ttyUSB0)
- Use screen command talking to COM port<br />
  cmd: **screen /dev/ttyUSB0 115200**

Usage: <br />
**screen /dev/ttySX baud_rate,cs8|cs7,ixon|-ixon,ixoff|-ixoff,istrip|-istrip**
- /dev/ttySX: serial port number
- baud_rate: 9600, 115200 or others
- cs8 or cs7: transmission of 8 or 7 bits per byte
- ixon/-ixon: Enable/disable software flow-control(CTRL-S/CTRL-Q) for sending data
- ixoff/-ixoff: Enable/disable software flow-control for receiving data
- istrip/-istrip: Clear/keep the eight bit in each received byte


#### Reference link
- http://www.cyberciti.biz/faq/unix-linux-apple-osx-bsd-screen-set-baud-rate
- http://www.cyberciti.biz/tips/linux-screen-command-howto.html

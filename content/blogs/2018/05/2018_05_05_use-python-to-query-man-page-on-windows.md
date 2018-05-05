---
title: Use python to query man page on windows
date: 2018-05-5 16:30
category: Python
comments: True
slug: use-python-to-query-man-page-on-windows
---

# Background  

因為最近常常在使用Cmder看程式碼，但在Windows上面除非裝了WSL  
不然要臨時想man某個function or library不是很方便  
所以很快的就想說來爬個文看有沒有什麼快速的方式可以寫個小程式  
就能幫我做到這件事  

# Search  

Google了很久有找到幾個方式，不過比較方便的是透過curl和sed就可以達到
這樣的話只要去parse命令式參數就可以很快的搞定了

```bash
curl -v --silent \"http://man.he.net/?topic=<command>section=all\" 2>&1 | sed -n \"/<PRE>/,/<\/PRE>/p\" | more
```

# Code Snippet  

一開始先用了`Batch`script去弄，但覺得要處理字串還是有點麻煩  
想了一下還是用`Python`來處理比較快，所以就很簡單的弄了二個版本


```bash
@echo off
setlocal enabledelayedexpansion

if "%1"=="" goto usage
echo Going to query [%1] function

curl -v --silent "http://man.he.net/?topic=%1&section=all" 2>&1 | sed -n "/<PRE>/,/<\/PRE>/p" | more

if errorlevel 0 goto end

:usage
@echo.
@echo %~n0 usage:
@echo -------------------------
@echo 1) man optarg
@echo.
@echo.
@echo This will go to the following url for man query.
@echo "http://man.he.net/?topic=<command_name>&section=all"
@echo.

:end
```

最後還是用Python寫了一個很小的程式，順手把`man`page的數字定義也查了一下  
這樣在查的時候可以看要查哪一個section  
雖然還是有一些網頁的html tag不過可以滿足我很快想查找資訊的目的
當然也可以把程式寫成去找網頁，不過這樣就要多開視窗覺得麻煩  

```Python
# man.py
import sys

def usage():
    page_num_help = """
    1     Executable programs or shell commands
    2     System calls (functions provided by the kernel)
    3     Library calls (functions within program libraries)
    4     Special files (usually found in /dev)
    5     File formats and conventions eg /etc/passwd
    6     Games
    7     Miscellaneous  (including  macro  packages and conventions), e.g. man(7), groff(7)
    8     System administration commands (usually only for root)
    9     Kernel routines

    1) man <command>
    2) man <1-9> <command>
    Ex:
       man optarg
       man 2 open
       man 3 fopen
    """
    print(page_num_help)


def call_man(cmd, section='all'):
    import os
    if section.lower() != 'all' and section.isnumeric():
        section = int(section)
        if 1 <= section <= 9:
            os.system("curl -v --silent \"http://man.he.net/?topic={0}&section={1}\" 2>&1 | sed -n \"/<PRE>/,/<\/PRE>/p\" | more".format(cmd, section))
    else:
        if cmd:
            os.system("curl -v --silent \"http://man.he.net/?topic={0}&section={1}\" 2>&1 | sed -n \"/<PRE>/,/<\/PRE>/p\" | more".format(cmd, section))

def main():
    if len(sys.argv) == 2:  # man <name>
        command = sys.argv[1]
        call_man(command, 'all')
    elif len(sys.argv) == 3:  # man 3 open
        section = sys.argv[1]   # section = 1~9 and all
        command = sys.argv[2]   # commmand = open
        call_man(command, section)
    else:
        usage()


if __name__ == "__main__":
    main()
```  

# 結果圖

最後長這樣  

![Output](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180505/man_cmder.gif)



收工
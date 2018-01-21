---
title: Configure Python Enviornment in Notepad++
date: 2018-01-20 23:44
category: Editor
comments: True
slug: configure-python-enviornment-in-notepad++
---
如何在 Notepad++ 編輯器中建立 Python 的執行環境  

透過以下簡單的步驟就可以快速的完成。 

STEP1: 按 F5 或是選擇選單中的 執行 (如下圖)  

![STEP1](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180120/01.png)  

STEP2: 接下來會跳出執行視窗會要求輸入要執行的程式  

在這邊我設定了Python 3.4的安裝路徑 C:\Python34\python.exe  
在加上參數 "$(FULL_CURRENT_PATH)"  

```dos
C:\Python34\python.exe "$(FULL_CURRENT_PATH)"
```
![STEP2](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180120/02.png)

輸入完選擇儲存

STEP3: 跳出 Shortcut 視窗後，輸入名稱 `Python` 和你想設定的熱鍵  

在這邊的例子是用 `Ctrl + Shift + A`

![STEP3](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180120/03.png)

選擇完畢後，選擇 OK

STEP4: 你可以到執行下拉選單中看到你新增的 Python 執行選項

![STEP4](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180120/04.png)

STEP5: 接下來就動手寫個簡單的 `Hello`程式囉  

```python
def hello(str):
    print("Hello, {}".format(str))

if __name__ == "__main__":
    hello("Notepad++")
    input() # 這個是為了讓執行視不要馬上結束
```

![STEP5](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180120/05.png)


STEP6: 收工


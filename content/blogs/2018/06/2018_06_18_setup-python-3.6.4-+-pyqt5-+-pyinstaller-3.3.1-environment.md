---
title: Setup Python 3.6.4 + PyQt5 + PyInstaller 3.3.1 Environment
date: 2018-06-18 19:19
category: Python
comments: True
slug: setup-python-3.6.4-+-pyqt5-+-pyinstaller-3.3.1-environment
---

# Background  

我原本的`PyQt`開發環境是  

1. Python 3.4.3(64-bit)  
2. PyQt 4.11.4  (Note: PyQt GPLv4.11.4 for Python v3.4(x64))  
3. PyInstaller 3.1.1 (安裝在C:\)  

最近剛好想試著把 `Python` 升級到 *3.6.4 (64-bit)* 就想順道把 `PyQt`升級到 5 以上  
就順便試一下新環境的打包是不是可行，也把一些過程記錄下來。  

1. Python 3.6.4(64bit)  
2. PyQt 5.10.1  
3. PyInstaller 3.3.1  

# STEPS

STEP1: 下載 [Python 3.6.4(64-bit)](https://www.python.org/downloads/release/python-364/)  

STEP2: 安裝 Python 3.6.4 到 `C:\Python36`  

STEP3: 將 `C:\Python36` 和 `C:\Python36\Scripts` 路徑加到系統環境變數 **PATH**  

STEP4: 安裝 PyQt5 (PyQt5-5.10.1)  

```DOS
python.exe -m pip install PyQt5
```  
PyQt5 安裝檔位置在 @ `C:\Python36\Lib\site-packages\PyQt5`  

STEP5: 安裝 PyQt5 的工具像是 Qt Designer  

```DOS
python.exe -m pip install PyQt5-tools  
```  
工具會安裝在 @ `C:\Python36\Lib\site-packages\pyqt5-tools`  

STEP6: 將 `C:\Python36\Lib\site-packages\pyqt5-tools` 加到系統環境變數 **PATH** 裡  

STEP7: 最後安裝 PyInstaller(3.3.1)，一樣也是透過 pip install command  

```DOS
python.exe -m pip install PyInstaller
```
或是指定版號也可以  
```DOS
python.exe -m pip install PyInstaller==3.3.1
```

# Package and Verification  

a. 寫一個 PyQt5 的 GUI 小程式  

```python
#-*- coding: utf-8 -*-
# PyQt5Sample.py

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
import sys

class SampleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 GUI Application')
        self.setGeometry(500, 500, 500, 500)
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = SampleGUI()
    myapp.show()
    sys.exit(app.exec_())
```  

b. 把上面的程式打包成 EXE 看能不能單獨執行  

```DOS
PyInstaller -F -w PyQt5Sample.py --noupx
```  

c. 執行完會出現下面的檔案與目錄  

![Output Directory](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180618/PyQt5_01.png)  

d. 打包的 EXE 檔會放在 dist 目錄裡  

![EXE](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180618/PyQt5_02.png)  

e. Double Click 執行檔  

![Output](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180618/PyQt5_03.png)  

> Note:  
> 若打包參數少了 `--noupx` 執行 EXE 會出現下面的 *Error*  
> ![ERROR](https://github.com/rickhau/rickhau.github.io/raw/master/images/20180618/PyQt5_LoadError.png)  


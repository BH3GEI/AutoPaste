# 导入所需的库
import pyperclip
from pykeyboard import PyKeyboard
import re
import sys
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def autoPaste():
    # 模拟 Ctrl+V 和回车键
    time.sleep(0.5)
    k = PyKeyboard()
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)
    k.tap_key(k.enter_key)

# 获取初始剪贴板内容
question = pyperclip.paste()

# 监控剪贴板变化
while True:
    time.sleep(0.1)
    string = pyperclip.paste()
    if string != question and string != '':
        print([string])
        question = string
        autoPaste()

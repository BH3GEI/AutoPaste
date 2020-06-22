import pyperclip
import re
import sys
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pykeyboard import PyKeyboard

question = pyperclip.paste()
while True:
    time.sleep(0.1)
    string = pyperclip.paste()
    if string != question and string != '':
        print([string])
        question = string

time.sleep(0.5)
    k = PyKeyboard()
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)

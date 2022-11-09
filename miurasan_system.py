import pyautogui
import pyperclip
import time
import webbrowser

webbrowser.open_new_tab("https://www.google.co.jp")
time.sleep(1)
pyperclip.copy("平泉町 観光")
pyautogui.keyDown("command")
pyautogui.keyDown("v")
pyautogui.keyUp("command")
pyautogui.keyUp("v")
pyautogui.press("enter")
time.sleep(1)
pyautogui.screenshot("screenshot.png")

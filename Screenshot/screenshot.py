#!/usr/bin/python3
import pyautogui, requests

im = pyautogui.screenshot()
im.save('screenshot.png', 'PNG')

url = 'http://192.168.1.80/upload_04.php'

test_files = [("screenshot", open("screenshot.png", "rb"))]

test_response = requests.post(url, files = test_files)

if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")





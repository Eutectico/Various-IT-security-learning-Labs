#!/usr/bin/python3
# pyinstaller -w -F -i "icon.ico" webcam.py
# pyinstaller --onefile -w 'webcam.py'

import cv2

webcam = cv2.VideoCapture(0)

# Drop 5 Frames for Exposure-Adjustement
for i in range(0, 5):
    worked, img = webcam.read()

# Save Image to Disk
if worked:
    cv2.imwrite("img.jpg", img)
    webcam.release()

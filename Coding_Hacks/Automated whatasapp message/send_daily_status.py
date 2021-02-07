#!/usr/bin/env python3
# import pywhatkit as kit
from dotenv import load_dotenv
import os

#! ---------------------- Send automated whatsapp message --------------------- #


def daily_status_report():
    load_dotenv()
    num = os.getenv("contact_number")
    msg = os.getenv("message")

    print(f"User: {num}\nPassword: {msg}")
    # kit.sendwhatmsg(num, msg, 23, 1)
#! ------------------------------------ EOF ----------------------------------- #

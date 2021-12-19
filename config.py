# Run This Script Before Running bot.py
import getpass
import re
import os

# Constants
WELCOME_MESSAGE = '''
  ###
   #     #    #   ####    #####    ##     ####   #####     ##    #    #
   #     ##   #  #          #     #  #   #    #  #    #   #  #   ##  ##
   #     # #  #   ####      #    #    #  #       #    #  #    #  # ## #
   #     #  # #       #     #    ######  #  ###  #####   ######  #    #
   #     #   ##  #    #     #    #    #  #    #  #   #   #    #  #    #
  ###    #    #   ####      #    #    #   ####   #    #  #    #  #    #


 #####   #    #
 #    #  ##  ##
 #    #  # ## #
 #    #  #    #
 #    #  #    #
 #####   #    #


 #####    ####    #####
 #    #  #    #     #
 #####   #    #     #
 #    #  #    #     #
 #    #  #    #     #
 #####    ####      #
'''
print(WELCOME_MESSAGE)


def validate_schedule_input(scheduling_time: str):
    if not re.match(r"\d\d:\d\d", scheduling_time):
        return False
    else:
        return True


def validate_webhook_url(webhook_url: str):
    if webhook_url.startswith("https://") or webhook_url.startswith("http://"):
        return True
    else:
        return False


username = input("Enter Your Instagram Username : ").lower()
if len(username) > 0:
    USERNAME = username
else:
    print("Invalid Username!")
    exit()
password = getpass.getpass("Enter Your Instagram Password : ")
if len(password) > 0:
    PASSWORD = password
else:
    print("Invalid Password!")
    exit()
t_username = input("Enter Target's Username : ").lower()
if len(t_username) > 0:
    TARGET_USERNAME = t_username
else:
    print("Enter Target's Username Correctly!")
    exit()
schedule_message = input("Do You Want To Schedule Message (Y/N) (Case Sensitive) : ").lower()
if schedule_message == "y":
    s_time = input("Enter Sending Time (24hr) Eg : 00:00 : ")
    if validate_schedule_input(s_time):
        SENDING_TIME = s_time
        SCHEDULE_MESSAGE = True
        DONT_SCHEDULE = False
    else:
        print("Invalid Time Format.")
        exit()
elif schedule_message == "n":
    SENDING_TIME = None
    DONT_SCHEDULE = True
    SCHEDULE_MESSAGE = False
else:
    print("Please Enter Value Correctly!")
    exit()
shutdown_pc = input("Do You Want To Shutdown PC After Sending Message (Y/N) (Case Sensitive) : ").lower()
if shutdown_pc == "y":
    SHUTDOWN = True
elif shutdown_pc == "n":
    SHUTDOWN = False
else:
    print("Please Enter Value Correctly!")
    exit()
chromedriver_path = input(
    "Enter Chrome Driver Path (Download From https://chromedriver.chromium.org/ According To Your Chrome Version) : ")
if "chromedriver" in chromedriver_path and os.path.isfile(chromedriver_path):
    CHROME_DRIVER_PATH = chromedriver_path
else:
    print("Invalid Chrome Driver Path!")
    exit()
message = input("Type Message To Send : ")
if len(message) > 0:
    MESSAGE = message
else:
    print("Please Enter Message Correctly!")
    exit()
webhook_url = input("Enter Discord Webhook URL : ")
if len(webhook_url) > 0 and validate_webhook_url(webhook_url):
    WEBHOOK_URL = webhook_url
else:
    print("Invalid Webhook URL!")
    exit()
with open("config.txt", "w") as f:
    f.write(str(USERNAME) + "\n")
    f.write(str(PASSWORD) + "\n")
    f.write(str(TARGET_USERNAME) + "\n")
    f.write(str(MESSAGE) + "\n")
    f.write(str(SHUTDOWN) + "\n")
    f.write(str(SENDING_TIME) + "\n")
    f.write(str(CHROME_DRIVER_PATH) + "\n")
    f.write(str(DONT_SCHEDULE) + "\n")
    f.write(str(SCHEDULE_MESSAGE) + "\n")
    f.write(str(WEBHOOK_URL) + "\n")
print("Done! Now Run bot.py")

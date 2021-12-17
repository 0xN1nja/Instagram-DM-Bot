# Copyright Abhimanyu Sharma, https://github.com/N1nja0p
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import discord_notifications
import datetime
# Constants
CURRENT_TIME=lambda:datetime.datetime.now().strftime("%H:%M:%S")
TEMP_TIME=lambda:datetime.datetime.now().strftime("%H:%M")
MESSAGE='''''' # Add Message To Send
TARGET_USERNAME="" # Add Target's Username
SENDING_TIME="00:00" # 24hr Format // 00:00
SHUTDOWN=False # Set This To True To Shutdown PC After Sending Message (Optional)
CHROME_DRIVER_PATH=r"" # Download Chrome Driver (https://chromedriver.chromium.org/)
CREDENTIALS={"username":"","password":""} # Add Your Credentials
chrome_options=Options()
chrome_options.add_argument("--start-maximized")
class DMBOT():
    def __init__(self,username:str,password:str):
        self.driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,options=chrome_options)
        self.driver.get("https://instagram.com")
        self.username=username
        self.password=password
    def login(self):
        try:
            WebDriverWait(self.driver,100000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username) # Username Field
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password) # Password Field
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click() # Submit Button
            WebDriverWait(self.driver,10000000000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click() # Save Info (Not Now) Button
            time.sleep(10) # Replace With 60 To Avoid Error
            self.driver.execute_script('document.querySelector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click()') # Turn On Notifications (Not Now) Button
        except:
            discord_notifications.notify("login-failed",CURRENT_TIME())
            print("Login Failed!")
        else:
            discord_notifications.notify("login-success",CURRENT_TIME())        
            print("Login Success!")
    def find_target(self):
        try:
            self.driver.get("https://www.instagram.com/direct/new/")
            WebDriverWait(self.driver,10000).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input')))
            target_username=self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input')
            time.sleep(5)
            target_username.send_keys(TARGET_USERNAME)
            WebDriverWait(self.driver,100000).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div')))
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div').click() # Checkbox
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div/button/div').click() # Next Button
            time.sleep(5)
        except:
            discord_notifications.notify("target-not-found",CURRENT_TIME(),TARGET_USERNAME)
        else:
            discord_notifications.notify("found-target",CURRENT_TIME())
            print(f"Target Found!")
    def send_message(self):
        try:
            WebDriverWait(self.driver,100000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
            message_textarea=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea') # Message Textarea
            time.sleep(5)
            message_textarea.send_keys(MESSAGE+Keys.ENTER) # Send Message And Press ENTER
            self.target_name=str(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div').get_attribute("innerHTML")) # Capture Target's Name
        except:
            self.message_sent=False
        else:
            discord_notifications.notify("message-sent",CURRENT_TIME(),self.target_name)
            print(f"Message Sent! Target Name : {self.target_name}")
            self.message_sent=True
    def shutdown_pc(self):
        discord_notifications.notify("shuttingdown-pc",CURRENT_TIME())
        print("Shutting Down PC!")
        time.sleep(10)
        with open(r"message.log","a",encoding="utf-8")as f:
            f.write(f"{CURRENT_TIME()} : Message Sent : {self.message_sent}, Target Name : {self.target_name}"+"\n")
        # Set SHUTDOWN=True If You Want To Shutdown PC After Sending Message (Optional)
        if SHUTDOWN:
            os.system("shutdown /s /t 1")
if __name__ == "__main__":
    dm_bot=DMBOT(CREDENTIALS["username"],CREDENTIALS["password"])
    dm_bot.login()
    dm_bot.find_target()
    ############################### SCHEDULED ################################
    # while True:
    #     if TEMP_TIME() == SENDING_TIME:
    #         dm_bot.send_message()
    #         break
    ############################# NON SCHEDULED ##############################
    dm_bot.send_message()
    ##########################################################################
    time.sleep(60)
    dm_bot.shutdown_pc()
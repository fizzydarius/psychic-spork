# imports
from selenium import webdriver
from time import sleep
from secrets import email, password
import os



def welcome_message():
    print ("This bot is created for spamming discord users,")
    print ("In order to use this bot, you need to be a little quick")
    print ("What services do you want to use?")
    print ("[H]oes mad , [B]itches aint shit (year) , [C]ustom Message")
    print ("Please input the letter")

class SpamBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def loginphase(self):
        self.driver.get("https://discordapp.com/login")
        sleep(2)
        email_input = self.driver.find_element_by_xpath("""//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[1]/div/input""")
        email_input.send_keys(email)
        password_input = self.driver.find_element_by_xpath("""//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[2]/div/input""")
        password_input.send_keys(password)
        login_btn = self.driver.find_element_by_xpath("""//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/button[2]""")
        login_btn.click()
        sleep(10)
        print ("Log in succesfull")
    
    def cooldown(self):
        cooldown_btn = self.driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div[2]/div[2]/div[3]/form/div[2]/button""")
        cooldown_btn.click()
    

    def hoesmad(self):
        n = int(input("How many times you want to say hoes mad?"))
        message_box = self.driver.find_element_by_xpath("""//*[@id="app-mount"]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/form/div/div/div/div[3]/div[2]""")
        for i in range(n):
            sleep(0.5)
            i = i + 1
            message_box.send_keys(f"Hoes mad x", i, "\n")

    def bitchesaintshit(self):
        print ("Warning! This can take up to 20 minutes to complete and it will be long! Please close the program or Ctrl + C if you want to exit")
        sleep(10)
        year = 2020
        message_box = self.driver.find_element_by_xpath("""//*[@id="app-mount"]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/form/div/div/div/div[3]/div[2]""")
        while year != 0:
            sleep(0.7)
            message_box.send_keys(f"Bitches aint shit ", year,"\n")
            year = year - 1

    def custom_message(self):
        custom_message = str(input("What is the custom message you want to spam?: "))
        n = int(input("How many times do you want to spam this message?"))
        message_box = self.driver.find_element_by_xpath("""//*[@id="app-mount"]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/form/div/div/div/div[3]/div[2]""")
        for n in range(n):
            message_box.send_keys(custom_message, "\n")
    
    def choice(self):
        print ("What option would you like to use? [B]itches aint shit, [C]ustom Message, [H]oes Mad")
        choice = str(input(""))
        if choice == ("b"):
            bot.bitchesaintshit()
        elif choice == ("c"):
            bot.custom_message()
        elif choice == ("h"):
            bot.hoesmad()


bot = SpamBot()
welcome_message()
bot.loginphase()
bot.choice()

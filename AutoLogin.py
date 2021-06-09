import time
import random
from selenium import webdriver
import os
from getpass import getpass


class AutoLogin:
    def __init__(self, url, hotlink):
        self.url = url
        self.createBrowser(hotlink)

    def createBrowser(self, hotlink):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.driver.get(self.url)
        self.enterCredentials(hotlink)

    def enterCredentials(self, url):
        time.sleep(2)
        user = os.environ['facebook_user']
        passW = os.environ['facebook_password']
        username = self.driver.find_element_by_id("email")
        password = self.driver.find_element_by_id("pass")
        loginButton = self.driver.find_element_by_id("loginbutton")
        username.send_keys(user)
        password.send_keys(passW)
        loginButton.submit()
        self.driver.implicitly_wait(15)
        time.sleep(random.uniform(2, 3))
        clickFriend = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div[1]/div/a/div[1]/div[2]/div[1]/div/div/div[1]/span/span/span/span")
        clickFriend.click()
        time.sleep(random.uniform(2, 3))
        textbox = self.driver.find_element_by_css_selector(".notranslate")
        textbox.send_keys(url)
        sendMessage = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/input")
        sendMessage.submit()

#AutoLogin("https://www.messenger.com/", "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
# print()

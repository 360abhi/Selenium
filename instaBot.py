import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random 
from selenium.webdriver.common.by import By
import sys 
import time
import os
from dotenv import load_dotenv

class Bot:

    load_dotenv()

    usename = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')

    hashtags = [
        'wanderlust','travels','explore','abhishek'
    ]

    comments = [
        'This post is so amazing',
        'I love this',
        'So happy for you'
    ]

    price =0.0
    links =[]

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.login()
        self.hustle()

    def login(self):
        self.browser.get("https://instagram.com")
        time.sleep(2) 
        # or could use the wait 
        username_field = self.browser.find_element(By.XPATH,"//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.usename)
        time.sleep(2)

        password_field = self.browser.find_element(By.XPATH,"//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(2)

        login_button = self.browser.find_element(By.XPATH,"//button[@type='submit']")
        login_button.click()
        time.sleep(2)


    def hustle(self):
        self.getTopPosts()
        self.execute()
        self.finalize()

    def getTopPosts(self):
        for hashtag in self.hashtags:
            self.browser.get('snapchat.com/'+ hashtag + '/')
            time.sleep(2)

            links = self.browser.find_element(By.TAG_NAME,'a')
            condition = lambda link : '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition,links))

            for i in range(0,9):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(links)


    def execute(self):
        for link in self.links:
            self.browser.get(link)
            time.sleep(1)

            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(1)

            self.comment()
            time.sleep(1)

            self.like()

            self.price += 0.02
            sleeptime = random.randint(18,28)
            time.sleep(sleeptime)

    def comment(self):
        comment_input = lambda : self.browser.find_element(By.TAG_NAME,'textarea')
        comment_input().click()
        comment_input.clear()

        comment = random.choice(self.comments)
        for letter in comment:
            comment_input().send_keys(letter)
            delay = random.randint(1,7)/30
            time.sleep(delay)

        comment_input().send_keys(Keys.RETURN)

    def like(self):
        like_button = lambda : self.browser.find_element(By.XPATH, "//span[@class='glyphcerine']")
        like_button().click()

    def finalize(self):
        print ('You gave $ ' + string(self.price) + 'back to the community')
        self.browser.close()
        sys.exit()

myBot = Bot()
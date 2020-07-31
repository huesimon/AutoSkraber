from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import sys




class AutoSkraber():
    completeList = ['not filled']
    def __init__(self):
        print('init')
        self.driver = webdriver.Chrome('./driver/chromedriver.exe')
        self.driver.set_window_size(300, 300)
        phoneNumbers = self.openCsv('phoneNumbers.csv')
        clubXtra = self.openCsv('clubXtra.csv')
        # Duplicate phonenumbers if its friday EXTRA CHANCE!!!!
        if datetime.datetime.today().weekday() == 4:
            phoneNumbers = [*phoneNumbers, *phoneNumbers]
        print(phoneNumbers, clubXtra)
        self.completeList = [*phoneNumbers, *clubXtra]
        print(self.completeList)

    def openCsv(self, fileName):
        results = []
        with open(fileName, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                results.append(row)
            return results
    def logout(self):
        sleep(1)
        self.findElement('/html/body/div[3]/div/div[1]/div/div')
        self.findElement('/html/body/div[4]/div/div[2]/div[4]/div[4]')

    def findElement(self, xpath):
        sleep(1)
        while True:
            try:
                element = WebDriverWait(self.driver, 5, 100).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                element.click()
                print("Clicked ===> ", xpath)
                break;
            except NoSuchElementException:
                print('failed')
                break;
        

    def login(self, number):
        self.driver.get('https://skrab.circlek.one/')

        self.findElement('/html/body/div[3]/div/div[2]/div/div/div[3]') #works

        slider = self.driver.find_element_by_class_name("slider-box")
        move = ActionChains(self.driver)
        move.click_and_hold(slider).move_by_offset(40, 0).release().perform()

        genderBtn = self.driver.find_element_by_class_name("button-box")
        genderBtn.click()

        # Næste knap
        self.findElement('/html/body/div[3]/div/div[2]/div/div/div[6]') 

        # TOS button
        self.findElement('/html/body/div[3]/div/div[2]/div/div[3]/div/form/div[1]/input')

        phoneNumberInput = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div/form/div[3]/input')
        phoneNumberInput.send_keys(number)

        #find start button first time
        self.findElement('/html/body/div[3]/div/div[2]/div/div[3]/div/form/input')

        self.findElement('/html/body/div[1]/div/div[2]/div/div/div[2]')
        sleep(1)
        self.findElement('/html/body/div[1]/div/div[2]/div/div/div')

        print('drawing on canvas')
        sleep(1)
        canvas = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[4]/div/div[3]/canvas")
        print(canvas)
        drawing = ActionChains(self.driver)\
            .click_and_hold(canvas)\
            .move_by_offset(0, 0)\
            .move_by_offset(50, 0)\
            .move_by_offset(0, 50)\
            .move_by_offset(0, -100)\
            .move_by_offset(-100, 0)\
            .move_by_offset(0, 100)\
            .move_by_offset(50, 0)\
            .move_by_offset(0, -100)\
            .release()
        drawing.perform()
        print('done drawing')

        self.logout()

        
    
        

autoSkraber = AutoSkraber()
print(autoSkraber.completeList)


for innerList in autoSkraber.completeList:
    for number in innerList:
        print(number)
        autoSkraber.login(number)




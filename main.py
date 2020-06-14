from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class AutoSkraber():

    def __init__(self):
        self.driver = webdriver.Chrome('driver/chromedriver.exe')

    def login(self):
        self.driver.get('https://skrab.circlek.one/')

        cookieBtn = self.driver.find_element_by_class_name("bm-button")

        cookieBtn.click()

        slider = self.driver.find_element_by_class_name("slider-box")
        move = ActionChains(self.driver)
        move.click_and_hold(slider).move_by_offset(40, 0).release().perform()

        genderBtn = self.driver.find_element_by_class_name("button-box")
        print(genderBtn)
        genderBtn.click()

        nextBtn = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[6]')
        nextBtn.click()

        tosBtn = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div/form/div[1]/input')
        tosBtn.click()

        phoneNumberInput = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div/form/div[3]/input')
        phoneNumberInput.send_keys('45127001')

        startBtn = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div/form/input')
        startBtn.click()


        continueBtn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]')
        continueBtn.click()

        sleep(3)

        welcomeBtn =  self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div")
        welcomeBtn.click()

        canvas = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[4]/div/div[3]/canvas")
        print(canvas)
        print('that was the canvas')
        sleep(1)
        drawing = ActionChains(self.driver)\
            .click_and_hold(canvas)\
            .move_by_offset(0, 0)\
            .move_by_offset(250, 0)\
            .move_by_offset(0, -250)\
            .move_by_offset(-500,0 )\
            .move_by_offset(0, 500 )\
            .move_by_offset(500, 0 )\
            .move_by_offset(0, -200 )\
            .move_by_offset(-400, 0 )\
            .release()
        drawing.perform()
        print(canvas)
        print('hello')

        
        
        sleep(500)
        

autoSkraber = AutoSkraber()

autoSkraber.login()
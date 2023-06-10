import random
import time
import os
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


import os.path

from selenium.webdriver.common.action_chains import ActionChains

# Press the green button in the gutter to run the script.
#CHANGE THE LOGIN CREDENTIALS
login='putuser@here.com'
password="PlacePasswordHere"
#CHANGE THE SOURCEFILES CREDENTIALS
raw_folder = "C:/Users/User/Desktop/Files/Raw/06/"
#edited_folder = "C:/Users/Nathan/Desktop/Voice_AI/Files/Edited/01"

c = webdriver.ChromeOptions()
#prefs = {'download.default_directory' : edited_folder}
#c.add_experimental_option('prefs', prefs)
c.add_argument("--incognito")
c.add_argument("--no sandbox")
#c.add_argument("--start maximized")
#c.add_argument("--start-fullscreen")
c.add_argument("--single-process")
c.add_argument("--disable-dev-shm-usage")
c.add_argument("--disable-blink-features=AutomationControlled")
c.add_argument("--disable-infobars")
#remove automation flags
c.add_experimental_option('useAutomationExtension', False)
c.add_experimental_option("excludeSwitches", ["enable-automation"])
#modify user agent parameters
#c.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5563.64 Safari/537.36")
driver = webdriver.Chrome(options=c)
delay = random.uniform(0.01, 0.05)  # Random delay between 100ms and 500ms
wait_time=600
def click_delay():
    return random.uniform(1.5, 5)

def login_func():



    # Navigate to the login page
    driver.get("https://podcast.adobe.com/enhance#")
    ## enter login info
    sign_in_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#root > div > div > header > div.sc-kLgnNl.dMorcd > button'))
    )
    sign_in_button.click()
    time.sleep(click_delay())

    login_field = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#EmailPage-EmailField')))
    for char in login:
        login_field.send_keys(char)

        time.sleep(delay)
    continue_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '#EmailForm > section.EmailPage__submit.mod-submit > div.ta-right > button > span'))
    )
    continue_button.click()

    # enter password
    password_field = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#PasswordPage-PasswordField')))
    for char in password:
        password_field.send_keys(char)
        time.sleep(delay)
    continue_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '#PasswordForm > section.PasswordPage__action-buttons-wrapper > div:nth-child(2) > button > span'))
    )
    continue_button.click()
def upload(path):
    wait = WebDriverWait(driver, wait_time)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#enhance-file-upload"))).send_keys(path)

def download():
    download_button = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '#root > div > div > div.sc-jYCGPb.sc-dYdCZC.fdgiSB.bhvAcN > div.sc-fSnZTl.eSqgBG > div > div.sc-hBmvmq.iqPyGB > button.sc-gKseQn.sc-bWNTWI.sc-cTkOCJ.dOkiGQ.GwrCs.spectrum-Button.spectrum-Button--fill.spectrum-Button--sizeL.spectrum-Button--accent'))
    )
    download_button.click()


def get_file_list(folder):
    return os.listdir(folder)




if __name__ == '__main__':
    login_func()
    #filename = "VOICE_001_00131.wav"
    file_list = get_file_list(raw_folder)

    for files in file_list:
        print(files)
        path = raw_folder + files
        print(path)
        upload(path)
        download()
        driver.get("https://podcast.adobe.com/enhance#")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

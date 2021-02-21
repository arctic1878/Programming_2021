from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException

import time
import os
import logging
# from selenium.webdriver.common.action_chains import ActionChains
import sys
import ssl
import csv
import unidecode
import smtplib

port = 465  # For SSL
password = "qweasd113"
sender_email = "arctic1878.programming@gmail.com"
receiver_email = "martin.stensen92@gmail.com"
minimum_requirement = 2500


# Create a secure SSL context
context = ssl.create_default_context()

# https://www.athleticsmania.com/?gotoManageAccount

logging.basicConfig(level=logging.INFO, filename="w_season_stats.log",
                    filemode='w',
                    format='%(levelname)s - %(name)s - %(message)s')


PATH = str(os.environ.get("CD_PATH"))


def nav_to_club_championship(driver):
    standings_xpath = '//*[@id="m-ui"]/div/div[4]/div[1]/div[2]/div[2]'
    click_button_xpath(driver, standings_xpath)


def log_in(driver, username, password):
    logging.info("Logging in to Athletics Mania")

    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "// *[@id='home-slide-1']/div/div[4]/div[2]/div[4]/div/div[2]/div/div[2]")))
    login.click()
    time.sleep(1)

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "UserLogin_username"))
    )
    username_field.send_keys(username)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "UserLogin_password"))
    )

    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    print(driver.title)

    time.sleep(1)


def click_button_xpath(driver, xpath, sleeptime=0):

    logging.info(f'Clicking button with xpath: {xpath}')

    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        button.click()
    except TimeoutException:
        logging.warning(f'Timed out while trying to click the button with xpath {xpath}')
        driver.quit()

    if sleeptime > 0:
        time.sleep(sleeptime)


def button_text(driver, xpath):
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    return button.text


def main():
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.athleticsmania.com/?gotoManageAccount")

    username = 'Arctic1878@gmail.com'
    password = 'qweasd113'

    if len(sys.argv) > 1:
        if sys.argv[1] == "erik" or sys.argv[1] == "Erik":
            username = 'elilleengen@hotmail.com'
            password = 'buskveien'

    log_in(driver, username, password)

    nav_to_club_championship(driver)


if __name__ == "__main__":
    main()

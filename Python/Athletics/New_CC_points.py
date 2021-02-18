from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import logging
# from selenium.webdriver.common.action_chains import ActionChains
import sys
import smtplib
import ssl
import csv
import unidecode

port = 465  # For SSL
password = "qweasd113"
sender_email = "arctic1878.programming@gmail.com"
receiver_email = "martin.stensen92@gmail.com"

# Create a secure SSL context
context = ssl.create_default_context()

# https://www.athleticsmania.com/?gotoManageAccount

logging.basicConfig(level=logging.INFO, filename="new_cc_points.log",
                    filemode='w',
                    format='%(levelname)s - %(name)s - %(message)s')


PATH = str(os.environ.get("CD_PATH"))

print(f'sys.argv length: {len(sys.argv)}')
for n in range(len(sys.argv)):
    print(f'sys.argv[{n}]: {sys.argv[n]}')


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


def nav_to_club_management(driver):
    logging.info("Navigating to club management")

    club_xpath = '//*[@id="m-ui-app"]/div[1]/div[3]/div[1]/div[2]'
    click_button_xpath(driver, club_xpath)

    club_management_xpath = '//*[@id="m-ui-app"]/div[1]/div[9]/div/div[1]/div[1]'
    click_button_xpath(driver, club_management_xpath)


def calculate_scores(driver):

    player_scores = {}

    # sort by points
    sort_xpath = '//*[@id="m-ui"]/div/div[4]/div[3]/div[1]/div[4]'
    click_button_xpath(driver, sort_xpath, 0.5)

    n_members_xpath = '//*[@id="m-ui"]/div/div[4]/div[2]/div[5]/div[2]'
    n_members = int(button_text(driver, n_members_xpath)[0:2])
    print(n_members)

    for x in range(n_members):
        member_id = x+1
        name_xpath = f'//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div/div[{member_id}]/div[3]/a/div'
        score_xpath = f'//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div/div[{member_id}]/div[5]'

        name = button_text(driver, name_xpath)
        score = button_text(driver, score_xpath)

        player_scores[name] = score

        print(f'Name: {name}, Score: {score}')

    filename = 'scores.csv'
    write_scores_to_file(filename, player_scores)


def write_scores_to_file(filename, player_scores):

    # Check if file exists
    # If the file exists, read last entry for new season calc
    # Then append data
    # If the file doesn't exist, create new file
    all_entries = []
    placement = 1
    # Reading all existing entries in points.csv to the list "all_entries"
    if os.path.isfile("./scores.csv"):
        with open('scores.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                all_entries.append(row)
    else:
        with open('scores.csv', 'w'):
            print("Creating new file: 'scores.csv'")
            pass

    with open('scores.csv', 'a', newline='') as csvfile:
        fieldnames = ['placement', 'name', 'points', 'difference', 'date', 'season', ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in player_scores:
            writer.writerow({'placement': placement, 'name': unidecode.unidecode(entry),
                             'points': player_scores[entry], 'difference': 0, 'date': '01.01.2000', 'season': '0'})
            placement += 1


def click_button_xpath(driver, xpath, sleeptime=0):

    logging.info(f'Clicking button with xpath: {xpath}')
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    button.click()

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

    # Logging in
    log_in(driver, username, password)

    nav_to_club_management(driver)

    calculate_scores(driver)

if __name__ == "__main__":
    main()
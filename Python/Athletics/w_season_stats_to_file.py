from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import logging
# from selenium.webdriver.common.action_chains import ActionChains
import sys
import ssl
import csv
import unidecode
import smtplib
from shutil import copyfile

port = 465  # For SSL
password = "qweasd113"
sender_email = "arctic1878.programming@gmail.com"
receiver_email = "martin.stensen92@gmail.com"
minimum_requirement = 2500
current_time = time.ctime(time.time()).replace(' ', '_').replace(':', '_')
cc_filename = "CC_data.csv"
cc_path = f'./{cc_filename}'
copies_path = f'./cc_points_copies/CC_data_{current_time}.csv'


# Create a secure SSL context
context = ssl.create_default_context()

# https://www.athleticsmania.com/?gotoManageAccount

logging.basicConfig(level=logging.INFO, filename="w_season_stats.log",
                    filemode='w',
                    format='%(levelname)s - %(name)s - %(message)s')


PATH = str(os.environ.get("CD_PATH"))


def write_cc_data_to_file(driver):
    league, division, club_data = collect_cc_data(driver)
    pos_idx, name_idx, members_idx, points_idx = 0, 1, 2, 3
    current_season = 0
    all_ccfile_entries = []

    # Reading all existing entries in points.csv to the list "all_entries"
    if os.path.isfile(cc_path):
        # Copy backup of file
        copyfile(cc_path, copies_path)
        with open(cc_filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                all_ccfile_entries.append(row)
    else:
        with open(cc_filename, 'w'):
            print(f'Creating new file: {cc_filename}')
            pass

    # Calculate latest season
    if len(all_ccfile_entries) > 0:
        print("Gonna calc season")

    with open(cc_filename, 'a', newline='') as csvfile:
        # Writing headers
        fieldnames = ['position', 'name', 'members', 'points', 'league', 'division']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Writing data to file
        for key in club_data:
            print(key)
            print(club_data[key][pos_idx])
            print(club_data[key][name_idx])
            print(club_data[key][members_idx])
            print(club_data[key][points_idx])
            print(league)
            print(division)
            writer.writerow({'position': club_data[key][pos_idx], 'name': club_data[key][name_idx], 'members': club_data[key][members_idx], 'points': club_data[key][points_idx], 'league': league, 'division': division})


def collect_cc_data(driver):
    club_data = {}
    
    league_xpath = '//*[@id="m-ui"]/div/div[4]/div[2]/div[1]/div[1]/div[2]'
    division_xpath = '//*[@id="m-ui"]/div/div[4]/div[2]/div[1]/div[1]/div[3]'
    league = button_text(driver, league_xpath)
    division = button_text(driver, division_xpath)
    
    # XPATHS:
    # Row x:         //*[@id="m-ui"]/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/div/div[x]
    # Club position: //*[@id="m-ui"]/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/div/div[x]/div[2]
    # Club name:     //*[@id="m-ui"]/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/div/div[x]/div[3]/div[2]
    # Club members:  //*[@id="m-ui"]/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/div/div[x]/div[4]/div[2]
    # Club points:   //*[@id="m-ui"]/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/div/div[x]/div[5]/span[2]
    for x in range(1, 11):
        club_pos_xpath = f'//*[@id="m-ui"]/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/div/div[{x}]/div[2]'
        club_pos = button_text(driver, club_pos_xpath)

        club_name_xpath = f'//*[@id="m-ui"]/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/div/div[{x}]/div[3]/div[2]'
        club_name = unidecode.unidecode(button_text(driver, club_name_xpath))

        club_members_xpath = f'//*[@id="m-ui"]/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/div/div[{x}]/div[4]/div[2]'
        club_members = button_text(driver, club_members_xpath)

        club_points_xpath = f'//*[@id="m-ui"]/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/div/div[{x}]/div[5]/span[2]'
        club_points = button_text(driver, club_points_xpath)

        club_data[x] = [club_pos, club_name, club_members, club_points]

    return league, division, club_data


def nav_to_club_championship(driver):

    # test_id = 'map-artefact-area-1-2-0'
    # click_button_id(driver, test_id, 'test')
    # driver.switch_to.frame(driver.find_element_by_id(test_id))

    standings_xpath = '//*[@id="map-artefact-area-1-2-0"]'
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, standings_xpath)))
    ActionChains(driver).context_click(element).perform()
    time.sleep(2)

    actual_standings_xpath = '//*[@id="m-ui"]/div/div[4]/div[1]/div[2]/div[2]'
    click_button_xpath(driver, actual_standings_xpath, 'standings')
    time.sleep(2)


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


def click_button_xpath(driver, xpath, name='', sleeptime=0):

    logging.info(f'Clicking button with xpath: {xpath}')

    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        print(button.text)
        button.click()
    except TimeoutException:
        print("Something went wrong, read log file (TimeoutException)")
        logging.warning(f'Timed out while trying to click the button {name} with xpath {xpath}')

        driver.quit()
    except ElementClickInterceptedException:
        print("Something went wrong, read log file (ElementClickInterceptedException)")
        logging.warning(
            f'ElementClickInterceptedException while trying to click the button {name} with xpath {xpath}')

        driver.quit()

    if sleeptime > 0:
        time.sleep(sleeptime)


def click_button_id(driver, id, name='', sleeptime=0):
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, id))
    )

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

    driver.maximize_window()

    log_in(driver, username, password)

    nav_to_club_championship(driver)

    write_cc_data_to_file(driver)


if __name__ == "__main__":
    main()

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


# https://www.athleticsmania.com/?gotoManageAccount
# Arctic1878@gmail.com
# qweasd113
player_names = []
player_points = []
player_info = []

logging.basicConfig(level=logging.INFO, filename="open_gp.log",
                    filemode='w',
                    format='%(levelname)s - %(name)s - %(message)s')


PATH = str(os.environ.get("CD_PATH"))
# print (f"PATH: {PATH}")

print(f'sys.argv length: {len(sys.argv)}')

for n in range(len(sys.argv)):
    print(f'sys.argv[{n}]: {sys.argv[n]}')


def click_button_xpath(driver, xpath):

    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        button.click()
    except:
        logging.warning(f'Couldnt click button with xpath: {xpath}')


def button_text(driver, xpath):
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    return button.text


def log_in(driver, username, password):
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


def navigate_to_gp_page(driver):
    gp_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="m-ui-app"]/div[1]/div[3]/div[1]/div[3]')))
    gp_button.click()


def open_gp(driver, gp_xpath, gp_type):

    click_button_xpath(driver, gp_xpath)

    # Cone 1
    cone_one_xpath = '//*[@id="m-ui"]/div/div[4]/div[7]/div[1]'
    try:
        click_button_xpath(driver, cone_one_xpath)
        logging.info("Clicked cone one")
    except:
        logging.warning("Couldn't click cone one")
        return

    # Cone 2
    cone_two_xpath = '//*[@id="m-ui"]/div/div[4]/div[7]/div[2]'
    try:
        click_button_xpath(driver, cone_two_xpath)
        logging.info("Clicked cone two")
    except:
        logging.warning("Couldn't click cone two")
        return

    if gp_type == "gold" or gp_type == "diamond":
        # Pick rewards up later
        pickup_later_xpath = '//*[@id="m-ui"]/div/div[4]/div[9]/div[3]/div[1]'
        try:
            click_button_xpath(driver, pickup_later_xpath)
            logging.info("Picking up rewards later")
        except:
            logging.warning("Couldn't press the pick up rewards later button")

        return

    # Commercial break
    time.sleep(0.5)
    watch_ad_xpath = '//*[@id="m-ui"]/div/div[4]/div[8]/div[1]/div[2]/div[1]'
    click_button_xpath(driver, watch_ad_xpath)
    time.sleep(30)

    # Cone 3
    cone_three_xpath = '//*[@id="m-ui"]/div/div[4]/div[7]/div[3]'
    try:
        click_button_xpath(driver, cone_three_xpath)
        logging.info("Clicked cone three")
    except:
        logging.warning("Couldn't click cone three")
        return

    # Cone 4
    cone_four_xpath = '//*[@id="m-ui"]/div/div[4]/div[7]/div[4]'
    try:
        click_button_xpath(driver, cone_four_xpath)
        logging.info("Clicked cone four")
    except:
        logging.warning("Couldn't click cone four")
        return

    # Pick rewards up later
    pickup_later_xpath = '//*[@id="m-ui"]/div/div[4]/div[9]/div[3]/div[1]'
    try:
        click_button_xpath(driver, pickup_later_xpath)
        logging.info("Picking up rewards later")
    except:
        logging.warning("Couldn't press the pick up rewards later button")


def main():
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.athleticsmania.com/?gotoManageAccount")

    basic_id = 1
    bronze_id = 2
    silver_id = 3
    gold_id = 4
    diamond_id = 5

    username = 'Arctic1878@gmail.com'
    password = 'qweasd113'

    if len(sys.argv) > 1:
        if sys.argv[1] == "erik" or sys.argv[1] == "Erik":
            username = 'buskveien9@hotmail.com'
            password = 'buskveien9'

    try:
        log_in(driver, username, password)
        time.sleep(2)
    except:
        logging.warning("Couldn't log in")
        driver.quit()

    try:
        navigate_to_gp_page(driver)
    except:
        logging.warning("Couldn't navigate to GP page")

    # Opening the basic GP's
    n_basic = button_text(
            driver, f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{basic_id}]/div[1]')
    logging.info(f'Number of basic GPs: {n_basic}')

    if n_basic == '':
        logging.info("There are no basic GPs available")
        n_basic = 0

    if len(sys.argv) >= 7:
        n_basic = sys.argv[2]

    basic_xpath = f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{basic_id}]/div[6]/div[1]/div'
    for x in range(int(n_basic)):
        logging.info(f'Opening the {x}th basic reward')
        try:
            open_gp(driver, basic_xpath, "basic")
        except:
            logging.warning("Couldn't open basic GP")

    # Opening the bronze GP's
    n_bronze = button_text(
        driver, f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{bronze_id}]/div[1]')
    logging.info(f'Number of bronze GPs: {n_bronze}')

    if n_bronze == '':
        logging.info("There are no bronze GPs available")
        n_bronze = 0

    if len(sys.argv) >= 7:
        n_bronze = sys.argv[3]

    bronze_xpath = f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{bronze_id}]/div[6]/div[1]/div'
    for x in range(int(n_bronze)):
        logging.info(f'Opening the {x}th bronze reward')
        try:
            open_gp(driver, bronze_xpath, "bronze")
        except:
            logging.warning("Couldn't open bronze GP")

    # Opening the silver GP's
    n_silver = button_text(
        driver, f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{silver_id}]/div[1]')
    logging.info(f'Number of silver GPs: {n_silver}')

    if n_silver == '':
        logging.info("There are no silver GPs available")
        n_silver = 0

    if len(sys.argv) >= 7:
        n_silver = sys.argv[4]

    silver_xpath = f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{silver_id}]/div[6]/div[1]/div'
    for x in range(int(n_silver)):
        logging.info(f'Opening the {x}th silver reward')
        try:
            open_gp(driver, silver_xpath, "silver")
        except:
            logging.warning("Couldn't open silver GP")

    # Opening the gold GP's
    n_gold = button_text(
        driver, f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{gold_id}]/div[1]')
    logging.info(f'Number of gold GPs: {n_gold}')

    if n_gold == '':
        logging.info("There are no gold GPs available")
        n_gold = 0

    if len(sys.argv) >= 7:
        n_gold = sys.argv[5]

    gold_xpath = f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{gold_id}]/div[6]/div[1]/div'
    for x in range(int(n_gold)):
        logging.info(f'Opening the {x}th gold reward')
        try:
            open_gp(driver, gold_xpath, "gold")
        except:
            logging.warning("Couldn't open gold GP")

    # Opening the diamond GP's
    n_diamond = button_text(
        driver, f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{diamond_id}]/div[1]')
    logging.info(f'Number of diamond GPs: {n_diamond}')

    if n_diamond == '':
        logging.info("There are no diamond GPs available")
        n_diamond = 0

    if len(sys.argv) >= 7:
        n_diamond = sys.argv[6]

    diamond_xpath = f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{diamond_id}]/div[6]/div[1]/div'
    for x in range(int(n_diamond)):
        logging.info(f'Opening the {x}th diamond reward')
        try:
            open_gp(driver, diamond_xpath, "diamond")
        except:
            logging.warning("Couldn't open diamond GP")

    driver.quit()


if __name__ == "__main__":
    main()

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

port = 465  # For SSL
password = "qweasd113"
sender_email = "arctic1878.programming@gmail.com"
receiver_email = "martin.stensen92@gmail.com"

# Create a secure SSL context
context = ssl.create_default_context()

# https://www.athleticsmania.com/?gotoManageAccount

logging.basicConfig(level=logging.INFO, filename="open_gp.log",
                    filemode='w',
                    format='%(levelname)s - %(name)s - %(message)s')


PATH = str(os.environ.get("CD_PATH"))

print(f'sys.argv length: {len(sys.argv)}')
for n in range(len(sys.argv)):
    print(f'sys.argv[{n}]: {sys.argv[n]}')


def click_button_xpath(driver, xpath):

    logging.info(f'Clicking button with xpath: {xpath}')
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    button.click()


def button_text(driver, xpath):
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    return button.text


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


def navigate_to_gp_page(driver):
    logging.info("Navigating to the GP page")

    gp_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="m-ui-app"]/div[1]/div[3]/div[1]/div[3]')))
    gp_button.click()


def open_gp(driver, gp_xpath, gp_type):

    click_button_xpath(driver, gp_xpath)

    # Cone 1
    cone_one_xpath = '//*[@id="m-ui"]/div/div[4]/div[7]/div[1]'
    click_button_xpath(driver, cone_one_xpath)
    logging.info("Clicked cone one")
    time.sleep(0.5)
    # Cone 2
    cone_two_xpath = '//*[@id="m-ui"]/div/div[4]/div[7]/div[2]'
    click_button_xpath(driver, cone_two_xpath)
    logging.info("Clicked cone two")
    time.sleep(0.5)

    if gp_type == "gold" or gp_type == "diamond":
        # Pick rewards up later
        pickup_later_xpath = '//*[@id="m-ui"]/div/div[4]/div[9]/div[3]/div[1]'
        click_button_xpath(driver, pickup_later_xpath)
        logging.info("Picking up rewards later")

        return

    # Commercial break
    time.sleep(0.5)
    watch_ad_xpath = '//*[@id="m-ui"]/div/div[4]/div[8]/div[1]/div[2]/div[1]'
    click_button_xpath(driver, watch_ad_xpath)
    time.sleep(35)

    # Cone 3
    cone_three_xpath = '//*[@id="m-ui"]/div/div[4]/div[7]/div[3]'
    click_button_xpath(driver, cone_three_xpath)
    logging.info("Clicked cone three")
    time.sleep(0.5)

    # Cone 4
    cone_four_xpath = '//*[@id="m-ui"]/div/div[4]/div[7]/div[4]'
    click_button_xpath(driver, cone_four_xpath)
    logging.info("Clicked cone four")
    time.sleep(0.5)

    # Pick rewards up later
    pickup_later_xpath = '//*[@id="m-ui"]/div/div[4]/div[9]/div[3]/div[1]'
    click_button_xpath(driver, pickup_later_xpath)
    logging.info("Picking up rewards later")
    time.sleep(0.5)


def main():
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.athleticsmania.com/?gotoManageAccount")

    basic_id, bronze_id, silver_id, gold_id, diamond_id = 1, 2, 3, 4, 5
    basic_opened, bronze_opened, silver_opened, gold_opened, diamond_opened = 0, 0, 0, 0, 0

    username = 'Arctic1878@gmail.com'
    password = 'qweasd113'

    if len(sys.argv) > 1:
        if sys.argv[1] == "erik" or sys.argv[1] == "Erik":
            username = 'elilleengen@hotmail.com'
            password = 'buskveien'

    # Logging in
    log_in(driver, username, password)

    # Navigating to the GP page
    navigate_to_gp_page(driver)

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
        open_gp(driver, basic_xpath, "basic")
        basic_opened += 1

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
        open_gp(driver, bronze_xpath, "bronze")
        bronze_opened += 1

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
        open_gp(driver, silver_xpath, "silver")
        silver_opened += 1

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
        open_gp(driver, gold_xpath, "gold")
        gold_opened += 1

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
        open_gp(driver, diamond_xpath, "diamond")
        diamond_opened += 1

    logging.info("Sending confirmation email")

    message = f'Subject: Done opening GPs\n\nOpened {basic_opened} basic, {bronze_opened} bronze, {silver_opened} silver, {gold_opened} gold and {diamond_opened} diamond GPs.' 
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    logging.info("Done, quitting driver")
    driver.quit()


if __name__ == "__main__":
    main()

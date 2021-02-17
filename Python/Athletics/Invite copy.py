from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import unidecode
import os
import logging
import re
from selenium.webdriver.common.action_chains import ActionChains


# https://www.athleticsmania.com/?gotoManageAccount
# Arctic1878@gmail.com
# qweasd113
player_names = []
player_points = []
player_info = []

logging.basicConfig(level=logging.INFO, filename="ccpoints.log",
                    filemode='w', format='%(levelname)s - %(name)s - %(message)s')


PATH = str(os.environ.get("CD_PATH"))
# print (f"PATH: {PATH}")



def log_in(driver):
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "// *[@id='home-slide-1']/div/div[4]/div[2]/div[4]/div/div[2]/div/div[2]")))
    login.click()
    time.sleep(1)

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "UserLogin_username"))
    )
    username.send_keys("Arctic1878@gmail.com")

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "UserLogin_password"))
    )

    password.send_keys("qweasd113")
    password.send_keys(Keys.RETURN)

    print(driver.title)

def navigate_to_player_page(driver):
    club = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "player-club"))
    )

    try:
        club.click()
    except:
        logging.warning("Couldn't click club button")
        

    club_management = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "m-ui-clubs-bottom-box-main-settings"))
    )

    try:
        club_management.click()
    except:
        logging.warning("Couldn't click club management button")


    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players[1].click()
    except:
        logging.warning("Couldn't click search_players button")

def search_all(driver):

    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[1]'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(2)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )
    
    try:
        search_players.click()
        logging.info("Click the 'search players' button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the 'search players' button")
        return

def search_26_30(driver):
    #Search 26-30

    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[7]'))
    )

    #age_buttons = WebDriverWait(driver, 10).until(
    #    EC.presence_of_all_elements_located(
    #        (By.CLASS_NAME, 'custom-select-item'))
    #)
    
    #for button in age_buttons:
    #    print (f'{button.text} - {button}')
    #    if button.text == "26-30":
    #        logging.info(f'Changing age button - {button.text} - {button}')
    #        age_button = button

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(1)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players.click()
        logging.info("Clicked the'search players'button")
    except:
        logging.warning("Something went wrong, couldn't click the 'search players' button")
        return

def search_31_35(driver):
    
    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[8]'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(1)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players.click()
        logging.info("Clicked the'search players'button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the 'search players' button")
        return
def search_36_40(driver):

    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[9]'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(1)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players.click()
        logging.info("Clicked the'search players'button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the 'search players' button")
        return
def search_41_45(driver):

    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[1]'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(1)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players.click()
        logging.info("Clicked the'search players'button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the 'search players' button")
        return
def search_46_50(driver):

    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[11]'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(1)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players.click()
        logging.info("Clicked the'search players'button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the 'search players' button")
        return
def search_51_55(driver):

    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[12]'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(1)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players.click()
        logging.info("Clicked the'search players'button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the 'search players' button")
        return
def search_56_60(driver):

    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[13]'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(1)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players.click()
        logging.info("Clicked the'search players'button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the 'search players' button")
        return
def search_61_65(driver):

    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[14]'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(1)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players.click()
        logging.info("Clicked the'search players'button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the 'search players' button")
        return
def search_66_70(driver):

    age_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[15]'))
    )

    actions = ActionChains(driver)
    actions.move_to_element(age_button)
    actions.perform()

    try:
        age_button.click()
        logging.info("Clicked the age button")
    except:
        logging.warning("Something went wrong, couldn't click the age button")
        return

    time.sleep(1)

    search_players = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-green"))
    )

    try:
        search_players.click()
        logging.info("Clicked the'search players'button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the 'search players' button")
        return


def invite_all_on_page(driver):
        #find all people that can be invited
    all_invitables = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "btn-orange"))
    )

    #delete the home button from list of people (list with all orange buttons)
    logging.info(f'Deleting all_invitables[0] ({all_invitables[0].text})')
    del all_invitables[0]

    print(f'Number of invitables: {len(all_invitables)}')
    logging.info(f'Number of invitables: {len(all_invitables)}')

    #invite every player on the home invitation screen
    if len(all_invitables) > 0:
        for item in all_invitables:
            try:
                print(f'Clicking item - {item.text} - {item}')
                #item.click()
            except:
                print(f'Couldnt click item - {item.text} - {item}')
            time.sleep(0.1)

def click_filter_button(driver):
        #filter stuff
    filter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "filter"))
    )

    try:
        filter_button.click()
        logging.info("Clicked the filter button")
    except:
        logging.warning("Couldn't click filter button")
        return
    time.sleep(3)

    level_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[1]'))
    )

    try:
        level_filter.click()
        logging.info("Clicked level filter")

    except:
        logging.warning("Couldn't click the level filter")
        return

def invite(driver):

    try:
        navigate_to_player_page(driver)
        time.sleep(3)
        logging.info("-- Completed navigate to player page --")
    except:
        logging.warning("!! Couldn't complete 'navigate_to_player_page !!")
        return
    
    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    # Clicking the filter button in order to select a new category
    try:
        click_filter_button(driver)
        time.sleep(3)
        logging.info("-- Completed click filter button --")
    except:
        logging.warning("!! Couldn't complete 'click_filter_button' !!")
        return

    # Setting the category to all players
    try:
        search_all(driver)
        time.sleep(3)
        logging.info("-- Completed search all --")
    except:
        logging.warning("!! Couldn't complete 'search_all' !!")
        return

    # Inviting everyone on the current page
    try:
        invite_all_on_page(driver)
        time.sleep(3)
        logging.info("-- Completed invite all on page --")
    except:
        logging.warning("!! Couldn't complete 'invite_all_on_page !!")
        driver.quit()
        return

    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    # Clicking the filter button to select a new category 
    try:
        click_filter_button(driver)
        time.sleep(3)
        logging.info("-- Completed click filter button --")
    except:
        logging.warning("!! Couldn't complete 'click_filter_button' !!")
        return
    
    # Setting the category to ages 26-30
    try:
        search_26_30(driver)
        time.sleep(3)
        logging.info("-- Completed search 26-30 --")
    except:
        logging.warning("!! Couldn't complete 'search_26_30' !!")
        return

    # Inviting everyone on the current page
    try:
        invite_all_on_page(driver)
        time.sleep(3)
        logging.info("-- Completed invite all on page --")
    except:
        logging.warning("!! Couldn't complete 'invite_all_on_page !!")
        driver.quit()
        return

    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---




def main():

    driver = webdriver.Chrome(PATH)
    

    driver.get("https://www.athleticsmania.com/?gotoManageAccount")

    #self.driver = webdriver.Chrome(executable_path='/Users/${userName}/Drivers/chromedriver', chrome_options=options)

    try:

        #Logging in
        try:
            log_in(driver)
            time.sleep(3)
        except:
            logging.warning("Couldn't log in")
            driver.quit()

        try:
            invite(driver)
        except:
            logging.warning("Something went wrong during invite")
            driver.quit()




    finally:
        logging.info("Done, quitting driver")
        driver.quit()


if __name__ == "__main__":
    main()

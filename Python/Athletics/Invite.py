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
import sys


# https://www.athleticsmania.com/?gotoManageAccount
# Arctic1878@gmail.com
# qweasd113
player_names = []
player_points = []
player_info = []

logging.basicConfig(level=logging.INFO, filename="invite.log",
                    filemode='w', format='%(levelname)s - %(name)s - %(message)s')


PATH = str(os.environ.get("CD_PATH"))
# print (f"PATH: {PATH}")

print (f'sys.argv length: {len(sys.argv)}')
print (f'sys argv 0 : {sys.argv[0]}')

total_invited = 0


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
    # sets country to all

    country_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[1]/div[2]/div/div[1]'))
    )

    try:
        country_menu.click()
        logging.info("Clicked the country menu button")
    except:
        logging.warning(
            "Something went wrong, couldn't click the country menu button")
        return

    
    all_countries = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/div[1]'))
    )

    try:
        ActionChains(driver).move_to_element(all_countries).click(all_countries).perform()
        logging.info(f'Clicked the all countries button')
    except:
        logging.warning(f'Couldnt click the all countries button')
    time.sleep(1)
     
    #clicking filter button
    # filter_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, ''))
    # )
    # ActionChains(driver).move_to_element(
    #     filter_button).click(filter_button).perform()


    # sets age to all
    lvl_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[1]'))
    )

    logging.info(f'LVL BUTTON: {lvl_button.text}')

    try:
        ActionChains(driver).move_to_element(
            lvl_button).click(lvl_button).perform()
        logging.info("Clicked the lvl button")
    except:
        logging.warning("Something went wrong, couldn't click the lvl button")
        return

    all_levels = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[1]'))
    )

    try:
        ActionChains(driver).move_to_element(
            all_levels).click(all_levels).perform()
        logging.info(f'Clicked the all levels button')
    except:
        logging.warning(f'Couldnt click the all levels button')



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

def xpath_switch(min_max):
    switch = {
        "26_30": '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[7]',
        "31_35": '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[8]',
        "36_40": '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[9]',
        "41_45": '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[10]',
        "46_50": '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[11]',
        "51_55": '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[12]',
        "56_60": '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[13]',
        "61_65": '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[14]',
        "66_70": '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[15]'
    }
    
    logging.info(f'Returning xpath for {min_max} : {switch.get(min_max, "error")}')
    return switch.get(min_max, "error")

def country_switch(country):
    switch = {
        "Country": "Country_id"
  
    }

    logging.info(f'Returning country_id for {country} : {switch.get(country, "error")}')
    return switch.get(country, "error")

def search_age(driver, min_max):

    xpath = xpath_switch(min_max)
    if xpath == "error":
        logging.warning("Wrong age category, Xpath entry does not exist")
        return

    logging.info(f'xpath returned: {xpath}')

    try:
        age_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, str(xpath)))
        )
        logging.info(f'age button: {age_button}')
    except:
        logging.warning("Couldn't find the age button")


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
        logging.info(f'Clicked the age button ({min_max})')
    except:
        logging.warning(f'Something went wrong, couldnt click the age button ({min_max})')
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

def invite_all_on_page(driver):
    global total_invited
        #find all people that can be invited
    all_invitables = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "btn-orange"))
    )

    #delete the home button from list of people (list with all orange buttons)
    logging.info(f'Deleting all_invitables[0] ({all_invitables[0].text})')
    del all_invitables[0]

    #print(f'Number of invitables: {len(all_invitables)}')
    logging.info(f'Number of invitables: {len(all_invitables)}')

    #invite every player on the home invitation screen
    if len(all_invitables) > 0:
        for item in all_invitables:
            try:
                logging.info(f'Clicking item - {item.text} - {item}')
                actions = ActionChains(driver)
                actions.move_to_element(item)
                actions.perform()

                if len(sys.argv) >= 5 and sys.argv[4] == "test":
                    continue
                item.click()
                total_invited += 1


                confirm_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div/div[3]/button'))
                )

                confirm_button.click()
            

            except:
                logging.info(f'Couldnt click item - {item.text} - {item}')
            #time.sleep(0.05)

def invite_selected_people_on_page(driver, min_level):
    global total_invited
    #//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div[10] box
    #//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div[10]/div[1]/div[1] level
    #//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div[10]/div[1]/div[2] level number
    #//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div[10]/div[2]/div[2] name

    #//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div[10]/div[5] invite button
    #//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div[10]/div[5] invitation sent

    # class_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME, "btn-orange"))
    # )

    # xpath_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div/div[3]/button'))
    # )

    time.sleep(2)    

   
    players = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "m-ui-clubs-players-main-box"))
    )

    n_players = len(players)
    logging.info (f'Num players on page: {n_players}')
    n = 1

    for p in players:
        level_xpath = f'//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div[{n}]/div[1]/div[2]'
        name_xpath = f'//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div[{n}]/div[2]/div[2]'
        inv_button_xpath = f'//*[@id="m-ui"]/div/div[4]/div[3]/div[2]/div[4]/div/div/div[{n}]/div[5]'

        name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, name_xpath))
        )

        level = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, level_xpath))
        )

        invite_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, inv_button_xpath))
        )

        if int(level.text) >= min_level and invite_button.text == "INVITE":
            logging.info (f'Inviting {name.text}, Level: {level.text}, Invite: {invite_button.text}')
            
            if len(sys.argv) >= 5 and sys.argv[4] == "test":
                    n += 1
                    continue

            try:    
                ActionChains(driver).move_to_element(
                    invite_button).click(invite_button).perform()
                logging.info(f'Clicked the invite button')
            except:
                logging.warning(f'Couldnt click the invite button')

            try:
                confirm_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div/div[3]/button'))
                )

                confirm_button.click()
                logging.info(f'Clicked the confirm button')
            except:
                logging.warning(f'Couldnt click the confirm button')

            total_invited += 1
            

        n += 1

    logging.info("Done inviting selected people on page")


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

def invite_age(driver):
    global total_invited

    try:
        navigate_to_player_page(driver)
        time.sleep(0.5)
        logging.info("-- Completed navigate to player page --")
    except:
        logging.warning("!! Couldn't complete 'navigate_to_player_page !!")
        return
    
    #if len(sys.argv) == 2 and sys.argv[1] == "countries":
    #    logging.info(f'country test')
    #    print("country test")
    #    return
    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

    # Clicking the filter button in order to select a new category
    try:
        click_filter_button(driver)
        time.sleep(0.5)
        logging.info("-- Completed click filter button --")
    except:
        logging.warning("!! Couldn't complete 'click_filter_button' !!")
        return


    # Setting the category to all players
    try:
        search_all(driver)
        time.sleep(0.5)
        logging.info("-- Completed search all --")
    except:
        logging.warning("!! Couldn't complete 'search_all' !!")
        return

    # Inviting everyone on the current page
    try:
        invite_all_on_page(driver)
        time.sleep(0.5)
        logging.info("-- Completed invite all on page --")
    except:
        logging.warning("!! Couldn't complete 'invite_all_on_page !!")
        driver.quit()
        return

    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    
    # Going through the different level categories

    min_level = 31
    max_level = min_level+4
    logging.info(f'Setting min level to {min_level}')
    logging.info(f'Setting max_level to {max_level}')

    min_max = ""
    level_limit = 70

    if len(sys.argv) >= 3:
        min_level = int(sys.argv[1])
        max_level = min_level+4
        logging.info(f'Setting min level to {min_level}')
        logging.info(f'Setting max_level to {max_level}')
        level_limit = int(sys.argv[2])
        logging.info(f'Setting level limit to {level_limit}')
    
    while max_level <= level_limit:
        min_max = f'{min_level}_{max_level}' 
        logging.info(f'min_max: {min_max}' )
        
        # Clicking the filter button to select a new category
        time.sleep(1)
        try:
            click_filter_button(driver)
            time.sleep(0.5)
            logging.info("-- Completed click filter button --")
        except:
            logging.warning("!! Couldn't complete 'click_filter_button' !!")
            return

        # Setting the category to ages min_max
        try:
            search_age(driver, min_max)
            time.sleep(0.5)
            logging.info(f'-- Completed search_age {min_max} --')
        except:
            logging.warning(f'!! Couldnt complete search_age {min_max} !!')
            return

        # Inviting everyone on the current page
        try:
            invite_all_on_page(driver)
            time.sleep(0.5)
            logging.info("-- Completed invite all on page --")
        except:
            logging.warning("!! Couldn't complete 'invite_all_on_page !!")
            driver.quit()
            return

        min_level = min_level + 5
        max_level = min_level + 4

    print(f'Total invited people: {total_invited}')
    logging.info(f'Total invited people: {total_invited}')

    # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

def invite_countries(driver, min_level):
    
    logging.info("Starting to invite countries")

    # 1 Click filter button
    # 2 Set age to all
    # 3 Loop trough countries
    # 4 if few invitables, skip country

    # 1 Clicking the filter button in order to select a new category
    try:
        click_filter_button(driver)
        time.sleep(0.5)
        logging.info("-- Completed click filter button --")
    except:
        logging.warning("!! Couldn't complete 'click_filter_button' !!")
        return

    # 2 Setting age to all ages

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

    # 3 Looping through countries
    country_id = 2
    xpath = ""
    country = ""

    logging.info(f'Entering country loop')

    time.sleep(2)
    while country_id <= 226:
        xpath = f'//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[4]/div/div/div[{country_id}]'

        logging.info(f'country id: {country_id}, xpath: {xpath}')
        
        country_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[4]/div[2]/div[2]/div[1]/div[2]/div/div[1]'))
        )

        try:
            country_menu.click()
            logging.info("Clicked the country menu button")
        except:
            logging.warning("Something went wrong, couldn't click the country menu button")
            return

        try:
            country_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, xpath))
            )

            country = country_button.text
            logging.info(f'Country: {country}')

        except:
            logging.warning(f'Something went wrong while finding the country button')
            return

        #print(f'Sleeping. Country: {country_button.text}')
        #time.sleep(2)

        try:
            ActionChains(driver).move_to_element(country_button).click(country_button).perform()
            logging.info("Clicked the country button")
        except:
            logging.warning("Something went wrong, couldn't click the country button")
            return

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

        #---- Check if there are people that can be invited ----
        time.sleep(1)
        all_invitables = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "btn-orange"))
                )

        if len(all_invitables) > 0:
            del all_invitables[0]

        if len(all_invitables) < 2:
            logging.info(f'Couldnt find any invitables in {country}')
            country_id += 1

            # Clicking the filter button in order to select a new category
            try:
                click_filter_button(driver)
                time.sleep(0.5)
                logging.info("-- Completed click filter button --")
            except:
                logging.warning("!! Couldn't complete 'click_filter_button' !!")
                return

            continue
    
        else:
            logging.info(f'Number of invitables in {country}: {len(all_invitables)}')

        #--------------------------------------------------------

        # Inviting selected people on the current page
        try:
            logging.info(f'Starting to invite selected people on page ({country})')
            invite_selected_people_on_page(driver, min_level)
            time.sleep(0.5)
            logging.info("-- Completed invite selected people on page --")
            print(f'Total invited people: {total_invited}')
            logging.info(f'Total invited people: {total_invited}')
        except:
            logging.warning(f'!! Couldnt complete invite selected people on page !! ({country})')
            driver.quit()
            return

        #--------------------------------------------------------
        # Clicking the filter button in order to select a new category
        try:
            click_filter_button(driver)
            time.sleep(0.5)
            logging.info("-- Completed click filter button --")
        except:
            logging.warning("!! Couldn't complete 'click_filter_button' !!")
            return

        country_id += 1


def main():
    global total_invited
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
            invite_age(driver)
        except:
            logging.warning("Something went wrong during invite age")
            driver.quit()

        if len(sys.argv) >= 4:
            try:
                min_level = int(sys.argv[1])
                logging.info(f'Minimum Level: {min_level}')
                invite_countries(driver, min_level )
            except:
                logging.warning("Something went wrong during invite countries")
                driver.quit()


    except:
        logging.warning("Something went wrong during execution of program")

    finally:
        logging.info(f'Total invited people: {total_invited}')
        logging.info("Done, quitting driver")
        driver.quit()


if __name__ == "__main__":
    main()

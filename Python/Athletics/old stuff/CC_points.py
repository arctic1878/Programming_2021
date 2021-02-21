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


# https://www.athleticsmania.com/?gotoManageAccount
# Arctic1878@gmail.com
# qweasd113
player_names = []
player_points = []
player_info = []

logging.basicConfig(level=logging.INFO, filename="new_ccpoints.log",
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

def fetch_points(driver):
    club = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "player-club"))
    )

    club.click()

    players = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, "club-players"))
         )

    players.click()

    all_players = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "name-text"))
        )

    # appending all the names in the table to the list "player_names"
    for player in all_players:
        player_names.append(unidecode.unidecode(player.text))

    all_points = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "m-ui-clubs-main-rightbox-table-box-points"))
    )

    # appending all the points in the table to the list "player_points"
    for point in all_points:
        player_points.append(point.text.replace(',', ''))

    # merging every name and corresponding point to tuples into the list "player_info", then sorts the list by points total
    player_info = list(zip(player_names, player_points))
    print(player_info)
    player_info = sorted(
        player_info, key=lambda x: int(x[1]), reverse=True)
    
    return player_info


def calculate_time(driver):
    time_left_secs = 0

    # NEW SEASON TEST FIX
    try:
        logging.info("refreshing")
        driver.back()
        logging.info("getting ranking page")
        driver.get("https://www.athleticsmania.com#/clubs/matches")
        time.sleep(1)

        ranking = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[1]/div[2]/div[2]'))
        )
        logging.info("Clicking on ranking")
        ranking.click()
        logging.info("Done clicking on ranking")

        timeout = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="m-ui"]/div/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div'))
        )
        
        #timelist = re.findall(r'\d+', timeout.text)

        timelist = timeout.text.split("\n")

        
        t1 = (int(timelist[0]), timelist[1])
        
        if len(timelist) > 2:
            t2 = (int(timelist[2]), timelist[3])

        if t1[1] == "d":
            time_left_secs += (t1[0]*24*60*60)
        elif t1[1] == "h":
            time_left_secs += (t1[0]*60*60)

        if len(timelist) > 2:
            if t2[1] == "h":
                time_left_secs += (t2[0]*60*60)
            elif t2[1] == "m":
                time_left_secs += (t2[0]*60)


        #THEY CHANGED THE CODE, THISE USED TO WORK WITH SPLIT ON SPACE BEFORE
        # for t in timelist:
        #     print(f"t[-1] = {t[-1]}, t = {t}")
        #     if t[-1] == "d":
        #         t = int(re.findall(r'\d+', t)[0])
        #         time_left_secs += (t*24*60*60)
        #         print(f"Adding {t}*24*60*60 seconds. time_left_secs = {time_left_secs}")
        #     elif t[-1] == "h":
        #         t = int(re.findall(r'\d+', t)[0])
        #         time_left_secs += (t*60*60)
        #         print(
        #             f"Adding {t}*60*60 seconds. time_left_secs = {time_left_secs}")
        #     elif t[-1] == "m":
        #         t = int(re.findall(r'\d+', t)[0])
        #         time_left_secs += (t*60)
        #         print(
        #             f"Adding {t}*60 seconds. time_left_secs = {time_left_secs}")

        print (f"Time left of season: {time_left_secs}")
        return time_left_secs

    except:
        print("Couldn't fetch time left")
        logging.warning("Couldn't fetch time left")
        driver.quit()

def main():
    current_time = time.ctime()
    time_epoch = time.time()
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    all_entries = []
    most_recent_point = 0
    difference = 0
    most_recent_season = 1
    season_count = 1
    new_season = False
    time_left_secs = 0
    prev_tls = 0
    biggest_difference = 0
    best_contributor = ""


    driver = webdriver.Chrome(PATH)
   
    driver.get("https://www.athleticsmania.com/?gotoManageAccount")

    #self.driver = webdriver.Chrome(executable_path='/Users/${userName}/Drivers/chromedriver', chrome_options=options)

    try:

        #Logging in
        try:
            log_in(driver)
        except:
            logging.warning("Couldn't log in")
            driver.quit()

        #Fetching points
        try:
            player_info = fetch_points(driver)
        except:
            logging.warning("Couldn't fetch points")
            driver.quit()


        # Reading all existing entries in points.csv to the list "all_entries"
        if os.path.isfile("./CC_points.csv"):
            with open('CC_points.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    all_entries.append(row)
        else:
            with open('CC_points.csv', 'w'):
                print ("Creating new file: 'CC_points.csv'")
                pass

        if len(all_entries) > 0:
            prev_tls = int(all_entries[-1][0])
 

        time_left_secs = calculate_time(driver)           
  

        if time_left_secs > prev_tls:
            print("new season!!")
            new_season = True
        else:
            print("Same season as last run")

        try:
            #add new data to the points file
            with open('CC_points.csv', 'a', newline='') as csvfile:
                fieldnames = ['time_left', 'epoch', 'date', 'season', 'name', 'points', 'difference']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                # player_info is a list with the current table [(name, point), (name, point), (name, point)....])
                # all_entries is a list with all the entries in "points.csv"
                for player in player_info:
                    
                    #if file alreade exist
                    if len(all_entries) > 0:
                        for entry in all_entries:
                            if player[0] in entry:
                                most_recent_point = int(entry[len(entry)-2])
                                #print(f"len entry: {len(entry)}")
                                if len(entry) >= 5:
                                    most_recent_season = int(entry[3])
                    else:
                        most_recent_point = 0
                        most_recent_season = 0

                    point = int(player[1])

                    if point >= most_recent_point and new_season == False:
                        difference = point-most_recent_point

                    if difference > 0:
                        print(f"{player[0]} has competed in the club championship ({difference} points)")
                    
                    if difference > biggest_difference:
                        biggest_difference = difference
                        best_contributor = player[0]

                    if new_season:
                        season_count = most_recent_season+1
                    else:
                        season_count = most_recent_season

                    writer.writerow({'time_left': time_left_secs, 'epoch': time_epoch, 'date': current_time, 'season': season_count,
                                    'name': player[0], 'points': player[1], 'difference': difference})

                if biggest_difference > 0:
                    print (f"\nBest contributor since last run: {best_contributor} with {biggest_difference} points")
                else: 
                    print ("No one has contributed since last run...")
        except:
            logging.warning("Couldn't write to file")
            print ("Couldn't write to file")
    except:
        driver.quit()

    finally:
        logging.info("finally, quitting driver")
        driver.quit()


if __name__ == "__main__":
    main()

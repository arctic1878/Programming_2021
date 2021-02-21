import time
import os
import logging
import csv
from shutil import copyfile


port = 465  # For SSL
password = "qweasd113"
sender_email = "arctic1878.programming@gmail.com"
receiver_email = "martin.stensen92@gmail.com"
minimum_requirement = 2500
scores_fname = "scores.csv"
end_scores_fname = "end_scores.csv"
end_scores_fname_v2 = "end_scores"

logging.basicConfig(level=logging.INFO, filename="w_final_scores.log",
                    filemode='w',
                    format='%(levelname)s - %(name)s - %(message)s')


PATH = str(os.environ.get("CD_PATH"))


def write_scores_to_file():

    # Check if file exists
    # If the file exists, read last entry for new season calc
    # Then append data
    # If the file doesn't exist, create new file
    all_score_entries = []
    all_final_score_entries = []
    all_seasons = []
    current_season_score = []
    current_season = 1
    current_time = time.ctime(time.time())
    current_time_v2 = current_time.replace(' ', '_').replace(':', '_')
    idx_placement, idx_name, idx_points, idx_date, idx_season = 0, 1, 2, 4, 5
    score_path = f'./{scores_fname}'
    final_score_path = f'./{end_scores_fname}'
    prev_entry_season = ''
    dst = f'./end_scores_copies/{end_scores_fname_v2}_{current_time_v2}.csv'

    # Reading all existing entries in scores.csv to the list "all_score_entries"
    if os.path.isfile(score_path):
        with open(scores_fname, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                all_score_entries.append(row)
    else:
        logging.info(f'File {scores_fname} doesnt exist, exiting')
        return

    # Checking how many seasons there has been
    for entry in all_score_entries:
        if entry[idx_season] not in all_seasons:
            if entry[idx_season][0] != 's':
                all_seasons.append(entry[idx_season])

    for season in all_seasons:
        current_season = int(season)
        next_season = current_season+1
        print(f'current: {current_season}, next: {next_season}')

        # put all current season in list
        # only keep the latest

        for entry in all_score_entries:
            if prev_entry_season == 'season' and entry[idx_season] == str(current_season):
                current_season_score = []

            if entry[idx_season] == str(current_season):
                current_season_score.append(entry)

            prev_entry_season = entry[idx_season]

        for entry in current_season_score:
            all_final_score_entries.append(entry)
        all_final_score_entries.append(['placement', 'name', 'points', ' ', 'date', 'season'])

        current_season_score = []

    print("ALL FINAL SCORE ENTRIES:")
    for entry in all_final_score_entries:
        print(entry)

    # Done, writing the final scores to file
    if os.path.isfile(final_score_path):
        logging.info(f'File {end_scores_fname} exists, making a copy.')
        copyfile(final_score_path, dst)

    with open(end_scores_fname, 'w', newline='') as csvfile:
        logging.info(f'Creating new file: {end_scores_fname}')

        fieldnames = ['placement', 'name', 'points', ' ', 'date', 'season']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in all_final_score_entries:
            print(f'writing entry to file, Entry: {entry[idx_name]}')
            writer.writerow({'placement': entry[idx_placement], 'name': entry[idx_name],
                            'points': entry[idx_points], ' ': ' ', 'date': entry[idx_date], 'season': entry[idx_season]})


def main():
    write_scores_to_file()


if __name__ == "__main__":
    main()

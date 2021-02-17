import os
import csv

def main():
    all_entries = []
    all_players = {}
    sorted_all_players = {}
    current_members = []
    left_us = {}
    newest_epoch = 0
    precent = False

    if os.path.isfile("./CC_points.csv"):
        with open('CC_points.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                all_entries.append(row)

    for entry in all_entries:
        name = entry[4]
        if name not in all_players and name != 'name':
            all_players[name] = 0

    for n in all_players:
        seasons = 1
        tmp_s = 0
        for entry in all_entries:
            if entry[4] == n:
                tmp_s = entry[3]
                break
        
        for entry in all_entries:
            if entry[4] == n:
                if entry[3] != tmp_s:
                    seasons += 1
                    tmp_s = entry[3]
        all_players[n] = seasons
        #print (f"{seasons} seasons <-- {n}")

    #print players and season
    sorted_all_players = sorted(all_players.items(), key=lambda x: x[1], reverse=True)



    #calc current members
    for entry in all_entries:
        newest_epoch = entry[1]
    
    for entry in all_entries:
        if entry[1] == newest_epoch:
            current_members.append(entry[4])
    
    for player in all_players:
        precent = False
        for member in current_members:
            if player == member:
                precent = True
        
        if precent == False:
            for entry in all_entries:
                if entry[4] == player:
                    left_us[player] = entry[2]


    for p in sorted_all_players:
        if p[0] in current_members:
            print (f"{p[1]} - {p[0]}")

    print ("\nNot with us anymore:\n")
    for n in sorted(left_us, key=lambda x: x[1]):
        print (f"{left_us[n]} - {n}")
    print ()
    
    

if __name__ == "__main__":
    main()

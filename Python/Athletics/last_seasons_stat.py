
def main():
    average_scores = {}
    entries = {}
    statfile = "last_seasons.txt"
    with open(statfile, "r") as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    for player in content:
        # print(player)
        name_points = player.split(": ")
        name = name_points[0]
        if name_points[1][0] == 'x' or name_points[1][0] == '(':
            continue
        points = name_points[1].split(", ")

        points_total = 0
        n_entries = 0
        for p in points:
            if p[0] == 'x' or p[0] == '(':
                continue
            p = p.replace(')', '')
            n_entries += 1
            points_total += int(p)

        entries[name] = n_entries
        points_avg = points_total/n_entries
        # print(name)
        # print(len(points))
        # print(points)
        # print(points_total)
        # print(points_avg)
        # print("\n")

        average_scores[name] = points_avg

    average_scores = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)
    print(average_scores)

    n = 1
    with open("average_scores.txt", "w") as f:
        for entry in average_scores:
            f.write(f'{n}. {entry[0]}:{entry[1]} ({entries[entry[0]]} entries)\n')
            n += 1


if __name__ == "__main__":
    print("Running main")
    main()

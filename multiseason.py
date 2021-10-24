import matplotlib.pyplot as plt
import csv
from pandas import DataFrame
from basketball_reference_scraper.players import get_stats
import numpy as np
if True:
    f = open('manipulate.csv')
    csv_f = csv.reader(f)
    datalist = list(csv_f)
    # Indexing guide: datalist[row][entrystat 1 being season]
    replacelist = []
    numteams = 1
    dupcheck = False
    for number in range(1, len(datalist)):
        if dupcheck == False and datalist[number][1] == datalist[number - 1][1]:
            replacelist.append(datalist[number - 1])
            numteams+=1
            dupcheck = True
            for entry in range(1, len(datalist[number])):
                if entry >= 7:
                    datalist[number][entry] = round((float(datalist[number - 1][entry]) + float(datalist[number][entry])),4)
                elif entry == 5 or entry == 6:
                    datalist[number][entry] = round(float(datalist[number-1][entry]) + float(datalist[number][entry]), 4)
                elif entry in (0, 2):
                    datalist[number][entry] = str(datalist[number][entry]) + "," + str(datalist[number - 1][entry])
                else:
                    continue
        elif (dupcheck == True and datalist[number][1] != datalist[number - 1][1]):
            for entry in range(7, len(datalist[number])):
                datalist[number-1][entry] = round((float(datalist[number-1][entry])/numteams), 4)
            for entry in range(5, len(datalist[number])):
                datalist[number][entry] = float(datalist[number][entry])
            numteams = 1
            dupcheck = False
        elif dupcheck == True and number == len(datalist)-1:
            replacelist.append(datalist[number-1])
            numteams+=1
            dupcheck = False
            for entry in range(1, len(datalist[number])):
                if entry >= 7:
                    datalist[number][entry] = round((float(datalist[number - 1][entry])+float(datalist[number][entry]))/numteams, 4)
                elif entry == 5 or entry == 6:
                    datalist[number][entry] = float(datalist[number-1][entry]) + float(datalist[number][entry])
                elif entry in (0, 2):
                    datalist[number][entry] = str(datalist[number][entry]) + "," + str(datalist[number-1][entry])
                else:
                    continue
        elif datalist[number][1] == datalist[number - 1][1]:
            replacelist.append(datalist[number - 1])
            numteams += 1
            for entry in range(1, len(datalist[number])):
                if entry >= 7:
                    datalist[number][entry] = round((float(datalist[number - 1][entry]) + float(datalist[number][entry])),4)
                elif entry == 5 or entry == 6:
                    datalist[number][entry] = float(datalist[number-1][entry]) + float(datalist[number][entry])
                elif entry in (0, 2):
                    datalist[number][entry] = str(datalist[number][entry]) + "," + str(datalist[number - 1][entry])
                else:
                    continue
        else:
            for entry in range(5, len(datalist[number])):
                datalist[number][entry] = float(datalist[number][entry])
            numteams = 1
            dupcheck = False
    for item in replacelist:
        datalist.remove(item)
    stattuple = tuple(['Season', 'Age', 'Team', 'Lg', 'Pos', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P',
                 '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'])
    statnums = tuple([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                27, 28, 29])
    statdict = dict(zip(stattuple, statnums))
    temparr = np.array(datalist)
    transpose = temparr.T
    datalist = transpose.tolist()
    regnumpy = np.asarray(datalist[statdict['FG%']][1:], dtype=)
    print(regnumpy)
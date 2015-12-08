import csv

with open('relatesBOTH.csv', 'w', newline='') as b:
    writer = csv.writer(b)

    with open('relatesCH.csv', 'r') as f:
        CH = csv.reader(f)

        with open('relatesLJ.csv', 'r') as a:
            LJ = csv.reader(a)

            for edge in CH:
                for a_row in LJ:
                    if str(edge) in LJ:
                        print(edge)

import csv

with open('lyrics.csv', 'r', encoding='utf-8') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    with open('clean_data.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, ['Genre', 'Lyrics'])
        writer.writeheader()
        genre_set = set()
        genre_dict = dict()
        for row in csvReader:
            csv_dict = dict()
            if row[4] != 'Not Available' and row[4] != 'Other':
                if row[5] != '':
                    genre_set.add(row[4])
                    csv_dict = {'Genre': row[4], 'Lyrics': row[5]}
                    if row[4] in genre_dict:
                        genre_dict[row[4]] += 1
                    else:
                        genre_dict[row[4]] = 1
                    writer.writerow(csv_dict)



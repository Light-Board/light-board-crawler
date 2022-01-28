import csv


def make_csv(file_name, col, data_list: list):
    with open(f'{file_name}.csv','w', encoding='utf-8') as csv_file :
        write = csv.writer(csv_file)
        write.writerow(col)
        for data in data_list:
            write.writerow(data)
# csv 파일 읽어오기

import csv

path = 'C:/YYS/Python/human_Python/Day03/'
file = input('파일명 : ')
file = path + file   


with open(file, 'r', newline='', encoding='UTF-8') as file:
    # csv 파일 객체
    csv_reader = csv.reader(file, delimiter=',', quotechar="'")
    for line in csv_reader:
        # print(type(line))
        for item in line:
            print('{} '.format(item), end='')
        # print(line)
        print()
        
    
# from django.test import TestCase
import csv
korean_dir = list()
japan_dir = list()
america_dir = list()
etc_dir = list()
snack_dir = list()
buffet_dir = list()
china_dir = list()
allist = list()

f = open('seocho.csv', 'r', encoding='cp949')
rdr = csv.reader(f)

for line in rdr:
    if line[5] == '한식':
        korean_dir.append(line[0:2])
    elif line[5] == '일식':
        japan_dir.append(line[0:2])
    elif line[5] == '양식':
        america_dir.append(line[0:2])
    elif line[5] == '기타':
        etc_dir.append(line[0:2])
    elif line[5] == '중식':
        china_dir.append(line[0:2])
    elif line[5] == '분식':
        snack_dir.append(line[0:2])
    elif line[5] == '뷔페식':
        buffet_dir.append(line[0:2])
    else:
        pass

f.close()

f = open('seocho.csv', 'r', encoding='cp949')
rdr = csv.reader(f)
for line in rdr:
    allist.append(line[0] + " " + line[1])
f.close()


f = open('txt/korealist.txt', 'w', encoding='cp949')
for line in korean_dir:
    f.write(line[0] + " " + line[1] + "\n")
f.close()

f = open('txt/japanlist.txt', 'w', encoding='cp949')
for line in japan_dir:
    f.write(line[0] + " " + line[1] + "\n")
f.close()

f = open('txt/americalist.txt', 'w', encoding='cp949')
for line in america_dir:
    f.write(line[0] + " " + line[1] + "\n")
f.close()

f = open('txt/etc.txt', 'w', encoding='cp949')
for line in etc_dir:
    f.write(line[0] + " " + line[1] + "\n")
f.close()

f = open('txt/snack_list.txt', 'w', encoding='cp949')
for line in snack_dir:
    f.write(line[0] + " " + line[1] + "\n")
f.close()

f = open('txt/buttetlist.txt', 'w', encoding='cp949')
for line in buffet_dir:
    f.write(line[0] + " " + line[1] + "\n")
f.close()

f = open('txt/chinalist.txt', 'w', encoding='cp949')
for line in china_dir:
    f.write(line[0] + " " + line[1] + "\n")
f.close()

f = open('txt/allist.txt', 'w', encoding='cp949')
for line in allist:
    f.write(line[0:3] + " " + line[3:] + "\n")
f.close()
print(allist)
from django.test import TestCase
import csv

f = open('*/seocho.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    print(line[0])
f.close()
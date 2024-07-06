import csv

re = csv.reader(open ('tee.csv','r'))
print(re)

for line in re :
    print(line)
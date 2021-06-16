import csv

inputpath = r'<<input>>'
outputpath = r'<<output>>'
substring = 'Test'

f = open(inputpath, newline='\n')
csv_f = csv.reader(f, delimiter=";")
w = open(outputpath, 'w', newline='\n')
with w:
    writer = csv.writer(w, delimiter=";")
    for row in csv_f:
        if(next((s for s in row if substring.lower() in s.lower()), None) != None):
            writer.writerow(row)
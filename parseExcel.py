import codecs
import csv
import json
import xlrd

print 'hell0'
book = xlrd.open_workbook('se_assignment_users.csv.xlsx')
print 'getsheet'
sheet = book.sheets()[0]
header = []
nrows = sheet.nrows
ncols = sheet.ncols
result = []
for i in range(0, ncols):
    header.append(sheet.cell(0,i).value)
    print header
for row in range(1,nrows):
    dict = {}
    for col in range(1, ncols):
        val = sheet.cell(row, col).value
        dict[header[col]] = val
    result.append(dict)
    print dict
    print json.dumps(dict, skipkeys=True)
a = json.dumps(result, ensure_ascii=False)
print a
file = codecs.open("customerjs", "w", 'utf-8')
file.write(a)
file.close()

import codecs
import csv
import json
import requests
import xlrd

book = xlrd.open_workbook('se_assignment_users.csv.xlsx')
sheet = book.sheets()[0]
header = []
nrows = sheet.nrows
ncols = sheet.ncols
result = []
for i in range(0, ncols):
    header.append(sheet.cell(0,i).value)
for row in range(1,5):
    dict = {}
    for col in range(1, ncols):
        val = sheet.cell(row, col).value
        dict[header[col]] = val
    #print json.dumps(dict)
    result.append(json.dumps(dict))
print result
file = codecs.open("customerjsraw", "w", 'utf-8')
file.write(result)
file.close()
jsons = json.dumps(result, ensure_ascii=False)
file = codecs.open("customerjs", "w", 'utf-8')
file.write(jsons)
file.close()

headers = {'content-type': 'application-json', 'X-API-KEY': ''}
for i in range(0, len(jsons)):
    #print jsons[i]
    r = requests.post('http://localhost:9000', data=jsons[i], headers=headers)
for i in range(0, ceil(len(jsons)/50)):
    left = i*50
    right = min(i*50+49,len(jsons))
    print str(left) + (':') + str(right)
    r = request.post("http://localhost:3999", data=jsons[left:right], headers=headers)

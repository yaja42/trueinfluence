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
    print header
for row in range(1,nrows):
    dict = {}
    for col in range(1, ncols):
        val = sheet.cell(row, col).value
        dict[header[col]] = val
    result.append(dict)
jsons = json.dumps(result, ensure_ascii=False)
file = codecs.open("customerjs", "w", 'utf-8')
file.write(jsons)
file.close()

headers = {'content-type': 'application-json', 'X-API-KEY': ''}
for i = range(0, len(jsons)):
    r = requests.post(singleUrl, data=result[i], headers=headers)
for i = range(0: ceil(len(jsons)/50)):
    left = i*50
    right = min(i*50+49,len(jsons))
    r = request.post(batchUrl, data=[left,right], headers=headers)

import codecs
import csv
import json
import math
import requests
import sys
import xlrd

def parse(file_path):
    book = xlrd.open_workbook(file_path)
    sheet = book.sheets()[0]
    csv_header = []
    int_header = ['totalTomatoOrders', 'daysSinceLastOrder', 'zip', 'age']
    nrows = sheet.nrows
    ncols = sheet.ncols
    result = []
    for i in range(0, ncols):
        csv_header.append(sheet.cell(0,i).value)
    for row in range(1,nrows):
        dict = {}
        for col in range(1, ncols):
            if csv_header[col] in int_header:
                val = int(sheet.cell(row, col).value)
            else:
                val = sheet.cell(row, col).value
            dict[csv_header[col]] = val
        result.append(json.dumps(dict))

    # extra - just to save to a file
    jsons = json.dumps(result, ensure_ascii=False)
    file = codecs.open("customer_json", "w", 'utf-8')
    file.write(jsons)
    file.close()

    return result

def userUpdate(baseUrl, user_json):
    headers = {'content-type': 'application-json', 'X-API-KEY': ''}
    print json.dumps(user_json)
    r = requests.post(baseUrl + '/api/users/update', data=json.dumps(user_json), headers=headers)

def bulkUserUpdate(baseUrl, users_json):
    headers = {'content-type': 'application-json', 'X-API-KEY': ''}
    print json.dumps(users_json)
    r = requests.post(baseUrl + '/api/users/bulkUpdate', data=json.dumps(users_json), headers=headers)

def main():
    file_path = sys.argv[1]
    baseUrl = sys.argv[2]
    parsed_data = parse(file_path)

    #test single Update
    #for i in range(0,len(parsed_data)):
        #userUpdate(baseUrl, parsed_data[i])
    for i in range(0, -(-len(parsed_data)//50)):
        left = i*50
        right = min(i*50+49,len(parsed_data))
        bulkUserUpdate(baseUrl, parsed_data[left:right])

if __name__ == '__main__':
    main()

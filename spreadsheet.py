import gspread
from oauth2client.service_account import ServiceAccountCredentials
from internet_test import get_internet_speed_info
from time import sleep

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
flag = True
row = 1

while flag is True:
    client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
    sheet = client.open("Internet Speeds").sheet1
    row += 1
    column = 1
    results = get_internet_speed_info()
    for result in results:
        sheet.update_cell(row, column, str(result))
        column += 1
    sleep(900)

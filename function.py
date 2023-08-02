import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from constants import *


credentials = ServiceAccountCredentials.from_json_keyfile_name(
	CREDENTIALS_FILE,
	['https://www.googleapis.com/auth/spreadsheets',
	'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


def table1():  #-->Функция для создания шапки таблицы для учета Даты
	service.spreadsheets().values().batchUpdate(
	spreadsheetId=spreadsheet_id,
	body = {
	'valueInputOption': 'USER_ENTERED',
	'data': [
		{'range': 'Лист2!A1:C1',
		'majorDimension': 'ROWS',
		'values': [['ФИО/Название подрядчика',
					'Уникальный номер размещения',
					'Дата учета оказания услуг']]}
		]}).execute()


def table2():  #-->Функция для создания шапки таблицы для учета Месяца
	service.spreadsheets().values().batchUpdate(
	spreadsheetId=spreadsheet_id,
	body = {
	'valueInputOption': 'USER_ENTERED',
	'data': [
		{'range': 'Лист3!A1:C1',
		'majorDimension': 'ROWS',
		'values': [['ФИО/Название подрядчика',
					'Уникальный номер размещения',
					'Месяц учета оказания услуг']]}
		]}).execute()


def table3():  #-->Функция для записи значений из основной таблицы в таблицу для учета Даты
	values = service.spreadsheets().values().get(
	spreadsheetId=spreadsheet_id,
	range = 'A2:D10',
	majorDimension='ROWS').execute()
	count = 1
	for i in values['values']:
		count += 1
		service.spreadsheets().values().batchUpdate(
		spreadsheetId=spreadsheet_id,
		body = {
		'valueInputOption': 'USER_ENTERED',
		'data': [
			{'range': f'Лист2!A{count}:C{count}',
			'majorDimension': 'ROWS',
			'values': [[f'{i[0]}', f'{i[3]}', f'{i[1]}']]}
			]}).execute()


def table4():  #-->Функция номер 2 для записи значений из основной таблицы в таблицу для учета Месяца
	values = service.spreadsheets().values().get(
	spreadsheetId=spreadsheet_id,
	range = 'A2:D10',
	majorDimension='ROWS').execute()
	count = 1
	for i in values['values']:
		count += 1
		service.spreadsheets().values().batchUpdate(
		spreadsheetId=spreadsheet_id,
		body = {
		'valueInputOption': 'USER_ENTERED',
		'data': [
			{'range': f'Лист3!A{count}:C{count}',
			'majorDimension': 'ROWS',
			'values': [[f'{i[0]}', f'{i[3]}', f'{i[2]}']]}
			]}).execute()


def table5(par):  #--> Функция для проверки изменений в основной таблицы и записи этих изменений в таблице учета Даты
	service.spreadsheets().values().update(
	spreadsheetId=spreadsheet_id,
	range = f'Лист2!{par}1',
	valueInputOption= 'RAW',
	body={'values': [[f'Проверка {time}']]}).execute()

	values = service.spreadsheets().values().get(
	spreadsheetId=spreadsheet_id,
	range = 'A2:D10',
	majorDimension='ROWS').execute()

	values2 = service.spreadsheets().values().get(
	spreadsheetId=spreadsheet_id,
	range = 'Лист2!A2:C10',
	majorDimension='ROWS'
	).execute()
	count = -1

	for name in values['values']:
		count += 1
		for data2 in values2['values'][count]:
			if data2 in name:
				service.spreadsheets().values().update(
				spreadsheetId=spreadsheet_id,
				range = f'Лист2!{par}{count + 2}',
				valueInputOption= 'RAW',
				body={'values': [['Изменений не обнаружено']]}).execute()
			else:
				if len(data2) == len(name[1]):
					if name[1].count('.') == data2.count('.'):
						service.spreadsheets().values().update(
						spreadsheetId=spreadsheet_id,
						range = f'Лист2!{par}{count + 2}',
						valueInputOption= 'RAW',
						body={'values': [[f'{name[1]}']]}).execute()


def table6(par):  #--> Функция для проверки изменений в основной таблицы и записи этих изменений в таблице учета Месяца
	service.spreadsheets().values().update(
	spreadsheetId=spreadsheet_id,
	range = f'Лист3!{par}1',
	valueInputOption= 'RAW',
	body={'values': [[f'Проверка {time}']]}).execute()

	values = service.spreadsheets().values().get(
	spreadsheetId=spreadsheet_id,
	range = 'A2:D10',
	majorDimension='ROWS').execute()

	values2 = service.spreadsheets().values().get(
	spreadsheetId=spreadsheet_id,
	range = 'Лист3!A2:C10',
	majorDimension='ROWS'
	).execute()
	count = -1

	for name in values['values']:
		count += 1
		for data2 in values2['values'][count]:
			if data2 in name:
				service.spreadsheets().values().update(
				spreadsheetId=spreadsheet_id,
				range = f'Лист3!{par}{count + 2}',
				valueInputOption= 'RAW',
				body={'values': [['Изменений не обнаружено']]}).execute()
			else:
				if name[2].lower() in months:
					service.spreadsheets().values().update(
					spreadsheetId=spreadsheet_id,
					range = f'Лист3!{par}{count + 2}',
					valueInputOption= 'RAW',
					body={'values': [[f'{name[2].lower()}']]}).execute()


def proverca1(par):  #--> Функция для проверки корректного ввода названия столбца в google таблице
	if len(par) == 1:
		if par.upper() in simvol:
			return True
	else:
		print(bad)
		return False

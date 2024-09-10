import re
import time

def cleanString(string):
	try:
		data = string.replace('CVV2', ' ')
		data = re.sub(r'[\r|\n]', ' ', string)
		data = re.sub(r'[^0-9]', ' ', data)
		data = re.sub(r'\s+', ' ', data)
	except AttributeError:
		data = ''
	
	return data.strip()
	

def validateYear(year):
	if len(year) == 2:
		year = '20' + year
	if int(year) <= time.localtime().tm_year + 5 and int(year) >= time.localtime().tm_year:
		return True
	else:
		return False
		
def validateMonth(month):
	if int(month) > 0 and int(month) <= 12:
		return True
	else:
		return False

def parseData(string):
	data = cleanString(string)

	# not supported format data default 
	result = {}

	for i in data.split(' '):
		if len(i) == 16 or len(i) == 15:
			result['ccnum'] = i
		elif len(i) == 4 or len(i) == 2 and validateYear(i):
			if validateYear(i):
				result['year'] = i
		elif len(i) == 2 and validateMonth(i):
			if validateMonth(i):
				result['month'] = i
		elif len(i) == 3 or len(i) == 4 and not validateYear(i) and not validateMonth(i):
			result['cvv'] = i

		if len(result) < 4:
			if len(i) == 16 or len(i) == 15:
				result['ccnum'] = i
			if len(i) == 4:
				if validateYear(i[-2:]) and validateMonth(i[:-2]):
					result['year'] = i[-2:]
					result['month'] = i[:-2]
				elif validateYear(i[:-2]) and validateMonth(i[-2:]):
					result['year'] = i[:-2]
					result['month'] = i[-2:]
			elif len(i) == 3 or len(i) == 4 and not validateYear(i) and not validateMonth(i):
				result['cvv'] = i

	if len(result) == 4:
		result['success'] = True

	if len(result) < 4:
		return {'success': False,'error': 'Not enough data to parse'}

	return {"success": True, "ccnum": result['ccnum'], "year": result['year'], "month": result['month'], "cvv": result['cvv']}
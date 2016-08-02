# Test post
import requests
import json

def testpost():
	data = {'temperature':'24.3'}
	data_json = json.dumps(data)
	payload = {'json_payload': data_json, 'apikey': 'TODO: MAKE A VALIDATION SYSTEM'}
	r = requests.get('http://localhost:8000/doorlogger/logevent', data=payload)

testpost();
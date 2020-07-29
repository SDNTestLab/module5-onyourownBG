#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
import pprint

USER = "devnetuser"
PASS = "Cisco123!"
URL = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"

headers = {'Content-Type': 'application/json'}

response = requests.post(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

token = response.json()['Token']

URL2 = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

getHeader = {'Accept': 'application/json', 'X-auth-token': token}

getResponse = requests.get(URL2, headers=getHeader, verify=False)

devices = getResponse.json() ["response"]
for device in devices:
	oak = device["type"]
	pine = device["hostname"]
	maple = device["macAddress"]
	birch = device["managementIpAddress"]
	cherry = device["role"]
	pprint.pprint(" The Device Type is: " + str(oak))
	pprint.pprint(" The Device Name is: " + str(pine))
	pprint.pprint(" The Device MACAddress is: " + str(maple))
	pprint.pprint(" The Device IP Address is: " + str(birch))
	pprint.pprint(" The Device Role is: " + str(cherry))


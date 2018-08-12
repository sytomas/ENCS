import sys
import json
import requests

encsip = input("Enter IP address: ")

headers = {
	    'Content-Type': "application/vnd.yang.data+json",
	    'Accept': "application/vnd.yang.data+json",
	    'Authorization': "Basic YWRtaW46Q2lzY28xMjMj",
	    'Cache-Control': "no-cache",
	    'Postman-Token': "093f5aac-e8b2-46c7-9d4e-0b7715c45cda"
	    }


def system_settings():
	#url = "https://172.16.10.200/api/operational/system/settings-native"
	url = "https://" + encsip + "/api/operational/system/settings-native"
	response = requests.request("GET", url, headers=headers, verify=False)
	#parse the output
	hostname=response.json()['system:settings-native']['hostname']
	wanipaddress=response.json()['system:settings-native']['wan']['ip-info']['ipv4_address']
	gwipaddress=response.json()['system:settings-native']['gateway']['ipv4_address']
	domain=response.json()['system:settings-native']['domain']
	dns1=response.json()['system:settings-native']['dns']['nameserver1']
	dns2=response.json()['system:settings-native']['dns']['nameserver2']
	#parse the data from response
	print ("")
	print ("="*14)
	print ('Host Name: '+ hostname)
	print ('WAN IP Address: ' + wanipaddress)
	print ('IPv4 Gateway Address: ' + gwipaddress)
	print ('Domain: ' + domain)
	print ('Name Server 01: ' + dns1)
	print ('Name Server 02: ' + dns2)
	print ("="*14)
	print ("")
def showvlan():
	url = "https:" + encsip + "/api/config/system/settings/wan/vlan"
	response = requests.request("GET", url, headers=headers, verify=False)
	#parse the ouptput
	print ("*"* 24)
	#
	print ("*"* 24)
	print (" ")


whatselect = input("> ")
if whatselect == "a":
    system_settings()
elif whatselect == "b":
    showvlan()
else:
    print("invalid selection")

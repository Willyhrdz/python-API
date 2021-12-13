import requests
import json
url = "https://webexapis.com/v1/messages"
token = <token>
room_id = <room_id>
payload = {
"roomId": room_id,
"text": "¡Hola desde Python!"
}
data = json.dumps(payload)
headers = {
"Authorization": "Bearer NTdhNjRmODgtZjhjZC00ZjVkLWE2YmItMWU2MDM2ODBhODZhNDhkMGUxODUtM2Ri_PF84_2a001399-4e85-4adc-b568-32f8032f2ae7" ,
"Content-Type": "application/json"
}
response = requests.post(url, headers=headers, data=data)
print(response.text)
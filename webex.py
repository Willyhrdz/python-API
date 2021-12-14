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
"Authorization": "Bearer " + os.environ["WEBEX_TEAMS_ACCESS_TOKEN"] ,
"Content-Type": "application/json"
}
response = requests.post(url, headers=headers, data=data)
print(response.text)
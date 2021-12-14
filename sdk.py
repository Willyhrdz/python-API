from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token="NTc4OGM1YTUtMDNlYy00MjE0LWI3YzEtYTEyOTk5ODYwZGUxODE5Mjg5MzEtYTc1_PF84_2a001399-4e85-4adc-b568-32f8032f2ae7")
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

api.messages.create(roomId = room_id, text = "Enviado desde el SDK de Python")
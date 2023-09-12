import requests
import json
import os

#check if it doesn't exist then make it
if not os.path.exists("json_files"):
	os.mkdir("json_files")


access_point="https://api.github.com"
f =open("token", "r")
token=f.read()
f.close()

github_session=requests.Secssion()
githun_session.auth =("EParviziCherri","token")

response_text=requests.get(access_point+"/rate_limit").text

print(json.loads(response_text))

user_id= "erinata"
response_text=github_session.get(access_point + "/users"+ user_id).text


json_text = json.loads(response_text)


file_name = "json_files/" + user_id + ".json"
f = open(file_name, "w")
f.write(json.dumps(json_text))
f.close()
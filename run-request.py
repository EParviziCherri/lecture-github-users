import requests
import json
import os
import pandas
import time 
#check if it doesn't exist then make it
if not os.path.exists("json_files"):
	os.mkdir("json_files")


access_point="https://api.github.com"
f =open("token", "r")
token=f.read()
f.close()

id_list = pandas.read_csv("seed.csv")
id_list =id_list['ghid']

github_session=requests.Session()
github_session.auth =("EParviziCherri",token)

response_text=requests.get(access_point+"/rate_limit").text
print(json.loads(response_text))


for user_id in id_list:

	#user_id= "erinata"
	print(user_id)
	response_text=github_session.get(access_point + "/users"+ user_id).text


	json_text = json.loads(response_text)


	file_name = "json_files/" + user_id + ".json"
	f = open(file_name, "w")
	f.write(json.dumps(json_text))
	f.close()
	time.sleep(1)

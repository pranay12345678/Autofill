import requests
url="https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/formResponse"
for i in range(100):	
	submission={"entry.1156409":"Pranay Agarwal",
				"entry.210055283":190623,
				"entry.192452008":"Yes",
				"entry.446099277":"https://github.com/pranay12345678/Autofill.git"}
	result=requests.post(url,data=submission)
	print (result)
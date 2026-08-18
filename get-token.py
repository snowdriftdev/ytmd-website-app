import requests


debug = False

appID="ytm-webapp"
appName="My Website Application"
appVersion="0.0.1-dev"

# gets an initial code
codeRequest = requests.post("http://localhost:9863/api/v1/auth/requestcode",json={"appId": appID,"appName": appName,"appVersion": appVersion})
if debug:(print(codeRequest.json()))

# uses the temp code to get a token authorized
tokenRequest = requests.post("http://localhost:9863/api/v1/auth/request", json={"appId": appID, "code": str(codeRequest.json()["code"])})
if debug:(print(tokenRequest.json()))

print(f"New Token: {tokenRequest.json()["token"]}")
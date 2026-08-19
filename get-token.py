import requests
import os
from dotenv import load_dotenv, set_key
load_dotenv()

debug = os.environ.get("DEBUG")

appID="ytm-webapp"
appName="My Website Application"
appVersion="0.0.1-dev"

# gets an initial code
codeRequest = requests.post("http://localhost:9863/api/v1/auth/requestcode",json={"appId": appID,"appName": appName,"appVersion": appVersion})
if debug:(print(codeRequest.json()))

# uses the temp code to get a token authorized
tokenRequest = requests.post("http://localhost:9863/api/v1/auth/request", json={"appId": appID, "code": str(codeRequest.json()["code"])})
if debug:(print(tokenRequest.json()))

print(f"New Token saved to .env: {tokenRequest.json()["token"]}")
set_key(dotenv_path=".env", key_to_set="YTMD_APP_TOKEN", value_to_set=tokenRequest.json()["token"])
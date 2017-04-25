import os
import json
"""
  "account_sid": "",
  "auth_token":"",
  "twilio_number":"+",
  "proxy":"",
  "weather_api_key":"",
  "zipcode":"",
   "to_phone_number",
"""
# constants for the account.json file
account_sid = "account_sid"
auth_token = "auth_token"
twilio_number = "twilio_number"
proxy ="proxy"
weather_api_key = "weather_api_key"
zipcode = "zipcode"
to_phone_number = "to_phone_number"

def get_input():
    inp = input()
    return inp.strip()

outfilepath = "account.json"
outfile = None

if os.path.isfile("account.json"):


    print("Account file found would you like to over write? (y/n)")

    option = get_input()

    if option.strip().lower() == "y":
        # erases file
        outfile = open(outfilepath, 'w')
    else:
        print("exiting...")
        exit()


print("The following can be found at: https://www.twilio.com/console")
print("Please enter your Twillio account sid:")

sid = get_input()

print("Please enter your Twilio AUTH Token:")

twilio_autho = get_input()

print("Please enter your Twillio Phone number found here (https://www.twilio.com/console/phone-numbers/incoming):")

twilio_num = get_input()

print("Please enter your wunderground API key:")

weather = get_input()
print("Please enter your zipcode:")

zip = get_input()

print("Please enter the phone number you would like to recieve these Texts on:")

to_num = get_input()


data = {}
data[account_sid] = sid
data[auth_token] = twilio_autho
data[twilio_number] = twilio_num
data[proxy] = "False"
data[weather_api_key] = weather
data[zipcode] = zip
data[to_phone_number] = to_num


output = json.dumps(data, indent=4, separators=(',',': '), ensure_ascii=False)

outfile.write(output)

outfile.close()
import os

"""
  "account_sid": "",
  "auth_token":"",
  "twilio_number":"+",
  "proxy":"",
  "weather_api_key":"",
  "zipcode":""
"""


outfilepath = "account.json"
outfile = None
if os.path.isfile("account.json"):


    print("Account file found would you like to over write? (y/n)")

    option = input()

    if option.strip().lower() == "y":
        # erases file
        outfile = open(outfilepath, 'w')
    else:
        print("exiting...")
        exit()


print("The following can be found at: https://www.twilio.com/console")
print("Please enter your Twillio account sid:")

sid = input()

print("Please enter your Twilio AUTH Token:")

twilio_autho = input()

print("Please enter your Twillio Phone number found here (https://www.twilio.com/console/phone-numbers/incoming):")

twilio_num = input()


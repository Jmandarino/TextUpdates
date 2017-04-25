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

    if option.lower() == "y":
        # erases file
        outfile = open(outfilepath, 'w')
    else:
        print("exiting...")
        exit()





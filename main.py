# python 3.5
# twilio 5.7.0 because I can't find proxy support for 6.0.0
from twilio.rest import TwilioRestClient
from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_SOCKS4
from twilio.rest.resources.connection import PROXY_TYPE_HTTP
import json
import os
#custom python files
import weather

account_sid  = None
auth_token = None
twilio_number = None
proxy = False
weather_api_key = None

def str_to_bool(s):
    if s == "True" or s == "true":
        return True
    else:
        return False

def get_settings():

    if os.path.isfile("account.json"):
        json_data = open("account.json").read()
        data = json.loads(json_data)
    else:
        Exception("No 'account.json' file found")

    if data["proxy"]:
        global proxy
        proxy = str_to_bool(data["proxy"])

    if data["weather_api_key"]:
        global weather_api_key
        weather_api_key = data["weather_api_key"]

    if data['account_sid'] and data['auth_token'] and data['twilio_number']:
        global account_sid
        global auth_token
        global twilio_number
        account_sid = data['account_sid']
        auth_token = data['auth_token']
        twilio_number = data['twilio_number']
    else:
        Exception("Missing Arguments in 'account.json,' please include account_sid, auth_token, and twilio_number")


if __name__ == "__main__":
    get_settings()

    conditions = weather.Weather(weather_api_key, "11756")

    conditions.weather_lookup()


    print(account_sid, auth_token, twilio_number)
    if proxy:
        print(proxy)


    print(proxy)

    # this works just not on a proxy
    exit()
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+15166528691",from_=twilio_number, body="test")


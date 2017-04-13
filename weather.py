import urllib.request
import json
import re


"""
Weather object,

Created with the intent to expand and add more features at a later time.

intial version just init, weather_lookup and variables.


current weather variable:
    weather [returns weather conditions]
    temp_f [returns temperature in degrees Farenheight]
    temp_c [returns temperature in degrees Celius]
    feelslike_f [returns feels like temperature in Farenheight]
    feelslike_c [returns feels like temperature in Celius]
    

"""
class Weather:
    zipReg = re.compile(r"\d{5}")
    def __init__(self, api_key, zipcode, units="f"):
        self.api_key = api_key
        self.zipcode = zipcode

        #set defaults
        self.weather = None
        self.temp_f = None
        self.feelslike_f = None
        self.temp_c = None
        self.feelslike_c = None

    def weather_lookup(self):
        if not self.zipReg.match(self.zipcode):
            Exception("Zipcode wasn't valid")

        lookup = "http://api.wunderground.com/api/" + self.api_key + "/conditions/q/" + self.zipcode + ".json"

        print(lookup)
        """
        proxy = urllib.request.ProxyHandler({"http":"http:webproxy.itginc.com:8080"})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
        """

        f = urllib.request.urlopen(lookup)
        output = f.read()
        # don't need this anymore
        f.close()
        json_data = json.loads(output)

        self.weather = json_data["current_observation"]["weather"]
        self.temp_f = json_data["current_observation"]["temp_f"]
        self.feelslike_f = json_data["current_observation"]["feelslike_f"]

        self.temp_c = json_data["current_observation"]["temp_c"]
        self.feelslike_c = json_data["current_observation"]["feelslike_c"]








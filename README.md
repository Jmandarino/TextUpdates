# Purpose:

To send a text to the user every morning informing them if their train is delayed and the current weather in their area. Thus making part of your commute automated.

## About:

This program makes use of Twilio, Weather Underground API, and the LIRR API in order to send an update on the current weather and train times for a user.


## What is needed:

You must create your own twilio account, weather underground API key and LIRR datamine API key.

 Accounts can be created here:
    * <https://www.twilio.com/try-twilio>
    * <https://www.wunderground.com/weather/api/>
    * <http://datamine.mta.info/user/register>

## How to run

#### Using the set up file:

run the set up file to quickly set up the "accounts.json" that is used to store your account information. Below is an example of the file:

```
{
  "account_sid": "",
  "auth_token":"",
  "twilio_number":"+",
  "proxy":"",
  "weather_api_key":"",
  "zipcode":""
}
```



# Python Client for Hyphenate Services

The Python Client for Hyphenate Services is for use in server applications on a proxy server, aka, your developer server. Client library serves as a wrapper layer on top of raw REST APIs that allows you to deploy on your server and make APIs requests. [See Hyphenate APIs](http://docs.hyphenate.io/docs/server-overview).

## Support

This library is open source. We encourage you to contribute to make the code base better! If you encountered any bug or feature suggestion, please [submit an issue](https://github.io.hyphenateInc/hyphenate-server-client-python/issues) or email support@hyphenate.io for urgent fixes.


## Requirement

- Hyphenate API key. [learn more](https://docs.hyphenate.io/docs/getting-started) or [create one](https://console.hyphenate.io).
- Java 1.7 or later. Latest version of the [Java](http://java.sun.com/javase/downloads/index.jsp).


## Installation


## Configurations

Update Hyphenate app configurations in `configs.py` under `hyphenateserver` folder.
```bash
api_host = 'https://api.hyphenate.io'
app_key = 'hyphenatedemo#demo'
app_credentials = {
    'client_id': 'YXA68E7DkM4uEeaPwTPbScypMA',
    'client_secret': 'YXA63_RZdbtXQB9QZsizSCgMC70_4Rs'
}
```

## Dependencies
- [Python Requests library ](http://docs.python-requests.org/en/latest/)
- [Python Requests library installation](http://docs.python-requests.org/en/latest/user/install/)

### Generate keystore

[Keystore Generation with public site certificate](https://docs.hyphenate.io/docs/keystore-generation-with-public-cer)

## REST APIs Documentation

[Usage](https://api-docs.hyphenate.io)

### Rate Limiting

By default, requests are sent at the expected rate limits for each web service, typically 30 queries per second for free users.  
Each IP address is limited to 30 requests per second. Requests beyond this limit will receive a 429 or 503 error. If you received this error, please reduce the request frequency and try again.
Please contact Hyphenate info@hyphenate.io if you need higher request rate.

## Install Python IDE

You can use Atom or any Python IDE you prefer to the run the project.


## Unit Testing Setups

We're using Python unit testing framework `unittest`. [learn more](https://docs.python.org/2/library/unittest.html)

```bash
$ python -m unittest discover
```

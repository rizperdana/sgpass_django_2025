Django 2024
===========

## How To

1. Set up virtualenv

```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

2. Migrate DB

```shell
python3 manage.py runserver
```

3. Runserver

```shell
python3 manage.py runserver 3001
````


4. Go to `http://localhost:3001/auth` and open the link given

```json
{
    "auth_url": "https://test.api.myinfo.gov.sg/com/v4/authorize?client_id=STG-...",
    "state": "K6GdQlfpQzAdM1yn"
}
```

5. copy and open the auth_url in your browser, it will redirect to Singpass Mock pass login
6. click login
7. click Agree, and then it will redirect to callback endoint

8. To run tests
```shell
python3 manage.py test
```


## Overview

Use the existing code provided (or roll your own as you see fit), build a web application powered by Django REST Framework APIs
to demonstrate the integration with [MyInfo v4 APIs](https://api.singpass.gov.sg/library/myinfo/developers/overview).
Kindly refer to the [MyInfo Demo App](https://github.com/singpass/myinfo-demo-app-v4) from [Tutorial 2: End-to-End Integration with Myinfo v4 APIs](https://api.singpass.gov.sg/library/myinfo/developers/tutorial2) provided by Singapore Government Technology Agency (GovTech)

You only need to build backend APIs and Django views.
No need to implement the frontend at all.

## Evaluation Criteria

We will look at your project and assess it for:

1. Extensibility - separation of concerns.
2. Simplicity - aim for the simplest solution that gets the job done whilst remaining
readable, extensible and testable.
3. Test Coverage - breaking changes should break your tests.
4. Robustness - should handle and report errors.

If you have any questions about these criteria, please ask.

## Specifications

1. Include a README with (accurate) usage instructions.


## Submission

GitHub is the preferred option (a public repo is fine), but we will also accept a .zip file if
necessary. Email your solution to gordon@abnk.ai.


## MyInfo Python API Usage

Set up virtualenv

```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

In Python shell

```python
from myinfo.client import MyInfoPersonalClientV4
from django.utils.crypto import get_random_string

oauth_state = get_random_string(length=16)
callback_url = "http://localhost:3001/callback"

client = MyInfoPersonalClientV4()

client.get_authorise_url(oauth_state, callback_url)

# Open up this SingPass Authorise URL and follow instructions
# After clicking on the "I Agree" button, you'll be redirected back to a callback URL like this
# http://localhost:3001/callback?code=myinfo-com-NlZPurlLUH79euT2I0xT6dFnY0lbf5oNVAhNVo8U


# Getting access token and getting person data
# Note: paste the auth code from the above callback
auth_code = "myinfo-com-NlZPurlLUH79euT2I0xT6dFnY0lbf5oNVAhNVo8U"
person_data = MyInfoPersonalClientV4().retrieve_resource(auth_code, oauth_state, callback_url)
print(person_data)
```

To run unit tests

```shell
python -m pytest
```

## Reference

You may refer to the following screen recording of a Sample React Native app powered by Django REST Framework APIs
https://drive.google.com/file/d/1Lj6hFGjuC2R3AXSTDvVWBAnW4bNRLl1j/view?usp=sharing for reference.

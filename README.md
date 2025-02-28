# README ASSIGNMENT

This code is basically not modify of the code provided by the instructor. Just add simple folder apps called `myinfo_instruction` so the code provieded by instuctor is still same, it's in the initial commit.

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


4. Open browser, go to ` browser`, go to `http://localhost:3001/auth`, it will give response for example like this

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
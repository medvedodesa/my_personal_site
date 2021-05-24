# landing-page

## Configuring

- Create virtual environment and install `requirements.txt`
```
$ virtualenv -p python3 env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
```

- `config.py` file is required, should look like:
```
DEBUG = True # or False
HOST = ["0.0.0.0"] # or []
```


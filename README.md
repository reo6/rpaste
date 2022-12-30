# rpaste

Simple paste service, written in 6 hours.

## Setting up

First, let [Poetry](https://python-poetry.org/) create a virtual environment and install dependencies for you:

```
poetry install
```

_Optional_: Create an account at HCaptcha and get your site key and secret key. You don't need to do this if you don't want captcha. Just disable it from [``rpaste/settings.py``](https://github.com/ramazanemreosmanoglu/rpaste/blob/main/rpaste/settings.py).

```
export HCAPTCHA_SITE_KEY="<your_site_key>"
export HCAPTCHA_SECRET_KEY="<your_secret_key>"
```

Run the development server:

```
poetry run flask --app rpaste.app run
```

Visit http://127.0.0.1:5000/ and you'll be good to go!

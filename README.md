# skyhack

This is my first Django application.

This project is still on working,
I'll try to keep developing and add more and more features in the near future.


## how to run locally
```
$ git clone git@github.com:posaune0423/skyhack.git

$ cd skyhack/skyhack
$ cp local_settings_sample.py local_settings.py

$ python manage.py migrate

$ python manage.py runserver
```

## how to deploy to Heroku
This application is supposed to work on Heroku.

In order to do it, please run following commands
```
$ heroku create <your app name>

$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku config:set CLOUD_NAME=<your cloud_name>
$ heroku config:set API_KEY=<your api_key>
$ heroku config:set API_SECRET=<your api secret>

$ git push heroku main

$ heroku run python manage.py migrate

$ heroku addons:create scheduler:standard
```

At last, to keep dyno server turn on, set schedular running the command below every 10 minutes.

`curl -I https://arcane-woodland-83940.herokuapp.com`
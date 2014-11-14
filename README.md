Remind Me YO
=========

Running Web Server Locally (on MacOS)

Prerequisites:
	Python
	Pip
	Postgresql

```sh
git clone https://github.com/chunky123/RemindMeYo.git
cd RemindMeYo
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt --allow-all-external
foreman start web
```

Your app should now be running on localhost:5000


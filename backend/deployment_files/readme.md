### django
Add prod_key to setting<br>
activate venv
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
```


### gunicorn
copy gunicorn.service to /etc/systemd/system/ folder <br>
run `sudo systemctl start gunicorn`<br>
then `sudo systemctl enable gunicorn`<br>
check socket file<br>
reload gunicorn (after file change) 
```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```


### nginx
copy default to /etc/nginx/sites-enabled folder <br>
run `sudo service nginx restart`

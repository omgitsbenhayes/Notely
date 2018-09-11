# Notely
## A bootstrap-enabled Django web application for storing notes/cards with tagging features in a NoSQL database

### Dependencies:
* Django (version 1.4 or greater)
* PHP (version 5.7 or greater
* CouchDB (version 0.9 or greater)

### Installation:

1. In notely/notely/settings.py: **update line 11** to add an administrator. You must add 1 but can add more if needed.
2. In notely/notely/settings.py: **update line 90** with your own secret key. This value is equivalent to a salt and should remain private.
3. In notely/notely/settings.py: **update line 118** with the path to your application template directly. In most cases, replace 'USER' with your username is sufficient.
4. In notely/notes/media_files/index.php: **update line 8** with your author name.
5. In notely/notes/media_files/index.php: **update line 188** with the path to your CouchDB database. Ensure the domain/IP, port number, and database name are correct.
6. In your apache config (/etc/apache2/apache2.conf): **add the following directive** to link the Django/WSGI application to your Apache web server. Replace USER with the appropriate path.

```
<Directory /home/USER/Documents/Python/django_projects/notely/notely>
<Files wsgi.py>
Order deny,allow
Allow from all
</Files>
</Directory>

WSGIDaemonProcess notely python-path=/home/USER/Documents/Python/django_projects/notely
WSGIScriptAlias /notely /home/USER/Documents/Python/django_projects/notely/notely/wsgi.py process-group=notely application-group=%{GLOBAL}
```

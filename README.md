# memory-game-api
The API is designed as the backend of the music-memory-game.

Dependencies: (pip install those)
djangorestframework
psycopg2
Pillow
django-cors-headers

## URLs

### Admin

**admin/login/**

### Category API

**category/get-all/\<str:api_key>**

### Category Admin

**category/add/**

**category/update/\<int:id>/**

**category/delete/\<int:id>/**

### Playlist API

### Playlist Admin

### Quiz API

### Quiz Admin

## BUGS AND ISSUES

### Issue #1
<details><summary>When deleting models, files reamain undeleted</summary>
My first approach putting code inside view classes that handle the DELETE method.
This method has been proved anadequate, because it did not include the PUT method and the CASCADE policy.

### SOLUTION

- 1. Create a script that will delete all unused files
- 2. Upon deleting unused files, override the delete and save methods on the model classes. Let the delete and save methods remove the files from the filesystem prior to updating the model and saving the new files.

<details>





## AUTOMATED TESTS
The testing creates a database for testing purposes, which is destroyed at the end of the testing.
In order for that to work, you need to make sure that the user account for the database has the 
required privellege. Either in SQL: ALTER USER db_username CREATEDB;
Or in the DB-Management tool. I did it with pgAdmin.

All automated tests are defined in test.py of each app.

### game_admin app

<details><summary>login</summary>

| View class      | URL pattern | Tested case     |
| :---        |    :----:   |          ---: |
| **UserLoginView** | **admin/login/** | login with valid credentials |
| | | login with invalid credentials |

</details>

## category app

<details><summary>Access with an API key</summary>

| View class      | URL pattern | Tested case     |
| :---        |    :----:   |         :--- |
| CategoryGetAllView | category/get-all/<str:api_key> | get data with a valid api-key |
| | | get data with an invalid api-key |

</details>

<details><summary>Access as admin</summary>

| View class      | URL pattern | Tested case     |
| :---        |    :----:   |         :--- |
| CategoryAddView | category/add/ | access is authorized and the data is valid |
| | | access is authorized but the data is invalid 
| | | unauthorized access |
| CategoryUpdateView | category/update/\<int:id>/ | access is authorized and the data is valid | 
| | | access is authorized but the data is invalid 
| | | unauthorized access |
| CategoryDeleteView | category/delete/\<int:id>/ | access is authorized and the id of the dataset is valid |
| | | access is authorized but the id of the dataset is invalid |

</details>

## playlist app

<details><summary>Access with an API key</summary>

| View class      | URL pattern | Tested case     |
| :---        |    :----:   |         :--- |
| PlaylistGetAllView | playlist/category/get-all/\<str:filter>/\<str:api_key> | get data with a valid api key |
| | | get data with an invalid api key |

</details>


<details><summary>Access as admin</summary>

| View class      | URL pattern | Tested case     |
| :---        |    :----:   |         :--- |
| PlaylistAddView | playlist/add/ | adding a playlist valid data and authorization |
| | | unauthorized access |
| | | access is authorized but the data is invalid |
| PlaylistUpdateItemView | playlist/update/\<int:id>/ | access authorized and data is valid |
| | | access is authorized but data is invalid |
| | | unauthorized access |
| PlaylistDeleteItemView | playlist/delete/\<int:id>/ | access authorized and the id of the dataset is valid |
| | | unauthorized access |
| | | invalid id |

</details>

## quiz app

<details><summary>Access with an API key</summary>

| View class      | URL pattern | Tested case     |
| :---        |    :----:   |         :--- |
| QuizListView | quiz/get-all/\<str:filter>/\<str:api_key> | get all quizes with a valid api key |
| | | try to get all quizes with a invalid api key |

</details>

## Deployment

### Preparation

I decided to deploy this API on a VPS \(Ubuntu \/ appache2 Webserver)

<details><summary>0. Installing a new SSL certifacate</summary>

After obtaining the certifacte file and ssl private key from my provider I had to install them into the virtual hosts that are 
intended to use them.

Alter the file : **/etc/apache2/sites-available/default-ssl.conf**

Add these lines to the virtual host:

\<VirtualHost *:443>

		ServerName dte-apps.com		
		ServerAlias www.dte-apps.com

		SSLEngine on
		SSLCertificateFile /opt/ssl/dteapps.cer
		SSLCertificateKeyFile /opt/ssl/key1.key

        ...
        
\</VirtualHost>

[website I used to find out how to install them on an apache2 webserver](https://www.ssldragon.com/how-to/install-ssl-certificate/ubuntu/#install-ubuntu)

</details>

<details><summary>1. Changing settings.py</summary>

The localhost was using a relative path, now I need to alter the code to use an absolute path on the server.

Alter the location of env.py:

<code>

    # Import environment variables

    if os.path.exists("/opt/gameapi/memory_game_api/env.py"):
        from .env import *
</code>

Add my host to ALLOWED_HOSTS:

<code>

    ALLOWED_HOSTS = [
        "dte-apps.com",
    ]


</code>

Add code to settings.py as:

<code>


    # Set this flag to True, when deploying to production
    DEPLOYED = False

    if not DEPLOYED:
        STATIC_URL = "static/"
    else:
        STATIC_URL = "gameapi/static/"

    if not DEPLOYED:
        MEDIA_URL = '/media/'
    else:
        MEDIA_URL = 'gameapi/media/'

</code>

Set the DEPLOYED flag to True, once deployed.

</details>

<details><summary>2. Create virtual environment inside the folder on the webserver</summary>

In PUTTy navigate to the folder where you want to trasfer the project to.

The command for createing a virtual environment folder: 

<code>    
    virtualenv venv
</code>

The command for activating the virtual envronment : 
<code>
    source venv/bin/activate
</code>

Now intall the dependencies:

<code>

    pip install djangorestframework

    pip install markdown       # Markdown support for the browsable API.

    pip install django-filter  # Filtering support

    pip install psycopg2

    pip install Pillow

    pip install django-cors-headers
</code>

Deactivate the virtual environment:
<code>
    deactivate
</code>

</details>

<details><summary>3. Copy the folder to the server</summary>

Copy all the contents of the folder, except for the .env (virutal environment folder), to the folder that was created for the application on the server.

</details>

<details><summary>4. Create config file for apache2 webserver</summary>

In /etc/apache2/conf-enabled/gameapi.conf

<code>
    WSGIDaemonProcess gameapi_app processes=1 threads=25 python-home=/opt/gameapi/venv lang='en_US.UTF-8' locale='en_US.UTF-8'
    WSGIScriptAlias /gameapi /opt/gameapi/memory_game_api/wsgi.py

    <Directory /opt/gameapi/memory_game_api>
        WSGIProcessGroup gameapi_app 
        WSGIApplicationGroup %{GLOBAL}   
        Require all granted
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    <VirtualHost *:80>
	    ServerName gameapi_media

	    Alias /gameapi/media/ /opt/gameapi/media/	

	    <Directory /opt/gameapi/media>
		    Require all granted
	    </Directory>	
    </VirtualHost>

</code>

Now it is necessary to change the owner of the media folder to the user and user-group that is asociated with apache2.
To see which user it is run the command :

<code>
    apache2ctl -S
</code>

On my system it is www-data:wwww:data

So now I need to change the owner of the media folder:

<code>
    chown -R www-data:www-data media
</code>

</detials>
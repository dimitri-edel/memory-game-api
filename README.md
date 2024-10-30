# memory-game-api
The API is designed as the backend of the music-memory-game.

Dependencies: (pip install those)
psycopg2
Pillow

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

<details><summary>Installing a new SSL certifacate</summary>

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

<details><summary>Changing settings.py</summary>

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



</details>
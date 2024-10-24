# memory-game-api
The API is designed as the backend of the music-memory-game.

Dependencies: (pip install those)
psycopg2
Pillow

## URLs

### Admin

**admin/login/**

### Category API

**category/get-all/<str:api_key>**

### Category Admin

**category/add/**

**category/update/<int:id>/**

**category/delete/<int:id>/**

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
| CategoryGetAllView | get-all/<str:api_key> | get data with a valid api-key |
| | | get data with an invalid api-key |

</details>

<details><summary>Access as admin</summary>

| View class      | URL pattern | Tested case     |
| :---        |    :----:   |         :--- |
| CategoryAddView | add/ | access is authorized and the data is valid |
| | | access is authorized but the data is invalid 
| | | unauthorized access |
| CategoryUpdateView | update/<int:id>/ | access is authorized and the data is valid | 
| | | access is authorized but the data is invalid 
| | | unauthorized access |
| CategoryDeleteView | delete/<int:id>/ | access is authorized and the id of the dataset is valid |
| | | access is authorized but the id of the dataset is invalid |

</details>
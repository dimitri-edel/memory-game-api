# memory-game-api
The API is designed as the backend of the music-memory-game.

Dependencies: (pip install those)
psycopg2
Pillow

## URLs

<details>
    <summary>List of URLs</summary>

    - admin/login/
    - category/get-all/<str:api_key>
    - category/add/
    - category/update/<int:id>/
    - category/delete/<int:id>/
    
</details>

## AUTOMATED TESTS
The testing creates a database for testing purposes, which is destroyed at the end of the testing.
In order for that to work, you need to make sure that the user account for the database has the 
required privellege. Either in SQL: ALTER USER db_username CREATEDB;
Or in the DB-Management tool. I did it with pgAdmin.

All automated tests are defined in test.py of each app.

### Tested views


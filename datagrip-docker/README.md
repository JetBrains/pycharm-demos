# DataGrip in PyCharm with Docker/PostgreSQL and Flask

This is in support of a November 2019 webinar Max is doing with PyCharm. 

## PostgreSQL Setup

1. Accept the PyCharm prompt to use Docker services

2. Open `Services` tab

3. Click `Play`

4. Open `docker-compose.yml`

5. Click play

6. Make a database connection to `jdbc:postgresql://localhost:54333/sakila` with the username/password from the `.env` file

7. Right-click on `sampledata/postgres-sakila-schema.sql` and run it

8. Same for `sampledata/postgres-sakila-insert-data.sql`

## Python Setup

1. Make a virtual environment

2. pip install -r requirements.txt

3. Make a Flask run configuration:

    - Set `Target:` to `app`
    
    - Set `Application:` to `app`
    
4. Run the config and go to `http://127.0.0.1:5000/actors/1`
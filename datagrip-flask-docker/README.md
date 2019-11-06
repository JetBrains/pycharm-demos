# Flask/DataGrip/PostgreSQL/Docker Demo

This demo is in support of a PyCharm-DataGrip webinar in November 2019.

## Demo

1. Show the repo page at GitHub
2. Review how I set things up:
    - Launched the container from docker-compose.yml
    - Connected to the database
    - Ran the two .sql files
    - Made an interpreter with requirements.txt
    - Set the template language to Jinja2
    - Marked the folder as a templates folder
    - Made a Flask Server run config
3. Open app.py
4. Run the app, look in browser
5. Language Injection
6. Autocomplete SQL grammar, table name, column name
7. Expand wildcard to column names
8. Navigation: Cmd-B to datasource, F4 to open table
9. Execute a query that includes a parameter
10. Refactoring, e.g. change a column name

## Cleanup

If you have a previous run of this, you’ll need to do some Docker and PyCharm:

1. Shut down and remove any Docker containers with:
   ```shell script
    $ docker-compose stop pg12 && docker-compose rm --force pg12
    $ docker container stop <container_id>
    $ docker rm <container_id>
    ```
2. Close the PyCharm project
3. Delete it from the projects list
4. Delete the virtual environment
5. Delete the `.idea` directory

## Open Demo Directory In PyCharm

Don’t open the *repo*, open one of the examples in the repo. E.g. this directory.

## Launch PG Container

1. Open `docker-compose.yml`
2. Click the green play button beside pg12
3. This uses values in the .env file

## Make a Database Connection

1. Open the Database Tool
2. Add a PostgreSQL connection (install JDBC driver if needed
    - Copy the jdbc connection string from the docker-compose.yml file
    - Username and password from the values in the .env file
    - Click the Test connection button
    - Click OK

## Populate the schema and sample data

1. Right-click on sample `load-sakila-schema.sql`
2. Choose Run
3. Click checkbox for execution target
4. Click OK
5. Same for `load-sakilia-data.sql`

## Make a Project Interpreter

1. Settings -> Project -> Project Interpreter -> Gear symbol -> Add -> New environment
2. Open `requirements.txt` and click Install Requirements link at the top

## Configure PyCharm

1. Right-click on templates and Mark Director As…Template Folder
2. Make a Flask run configuration:
    - Set `Target:` to `app`
    - Set `Application:` to `app`
3. Click the Flask Debug checkbox

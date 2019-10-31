# Flask/DataGrip/PostgreSQL/Docker Demo

This demo is in support of a PyCharm-DataGrip webinar in November 2019.

## Cleanup

If you have a previous run of this, you’ll need to do some Docker and PyCharm:

1. Shut down and remove any Docker containers with:
   ```shell script
    $ docker container ls -a
    $ docker container stop <container_id>
    $ docker rm <container_id>
    ```
2. Close the PyCharm project
3. Delete it from the projects list
4. Delete the virtual environment
5. Delete the `.idea` directory

## Open Demo Directory In PyCharm

Don’t open the repo, open one of the examples in the repo. E.g. this directory.

## Launch PG Container

Do this:

1. docker-compose up -d pg_12.X

Not:
1. Open docker-compose.yml
2. Click the green play button beside pg_12.X
3. This uses values in the .env file

## Make a Database Connection

1. Open the Database Tool
2. Add a PostgreSQL connection (install JDBC driver if needed
    - Copy the jdbc connection string from the docker-compose.yml file
    - Username and password from the values in the .env file
    - Click the Test connection button
    - Click OK

## Populate the schema and sample data

1. Right-click on sample load-sakila-schema.sql
2. Choose Run
3. Click checkbox for execution target
4. Click OK

## Make a Project Interpreter

1. Settings -> Project -> Project Interpreter -> Gear symbol -> Add -> New environment
2. Open requirements.txt and click Install Requirements

## Configure PyCharm

1. Right-click on templates and Mark Director As…Template Folder
2. Make a Flask run configuration:
    - Set `Target:` to `app`
    - Set `Application:` to `app`
3. - Click the Flask Debug checkbox

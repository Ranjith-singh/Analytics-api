Analytics Api :
    tools :
        fastApi :
            perform cred operatios
        python
        timescale :
            postgres database with added flexible duration based querying
            Used to provide timescale range to the cred operations methods
        note : ready to use timescale in github for working with fastApi
    it uses sql model along with timescale model to query the database and generate aggregated data from the extracted data
    cmd for creating a virtual env :
        python(version) venv venv
    activate venv :
        ./venv/scripts/activate
    tools required :
        fastApi==(if version required)
        uvicorn : for network communication b/w server and client
        gunicorn :  multiple worker processes to handle concurrent requests
        timescaledb : similar to postgres with included time range mod
        sqlmodel : interacting with sql databases
        pydantic : improve data visulaization
        sqlalchemy : access and manage sql databases with pydantic domain language

    run using fastapi or uvicorn
 
    Docker image :
        it is a static image of the code, requirements and other software to run a application
        it is like a class : blueprint
    Docker container :  
        it is a running environment created from the configurations in the docker image
        instance of docker image
    Docker file :
        to create a container of our application for available for running
        we can even control os for which it has to run
        instructions to build a docker image that is eventually used to create a docker container

    `docker build -t analytics-api:v1 -f Dockerfile.web`
    `docker run analytics-api:v1`

    docker compose :
        define and run multiple containers
        import or create docker images
        docker compose up --watch
        docker compose down or docker compose down -v (to remove volumes)
        docker compose run app python or docker compose run app /bin/bash

    note :
        be sure to change [CRLF] to [LF] in vscode while buiding a docker image
        because when you build image the end of each line in run.sh gets added with /r(windows style) instead of /n(linux style)
        so it is not recognised by linux as a cmd
        while importing the modules be sure to use . instead of / like :
                api.events.Routing
        key error :
            check endpoint method

    usage :
        defining rust api's :
            define in the main.py or any custom module from the src path(/api/events) and import those in  main.py
            event based routing
            while importing the modules be sure to use . instead of / like :
                api.events.Routing
            jupyter notebook to test the endpoints
            use pydantic to enforce the types of data to return or else it would just be a hint
            calling complete module to import all like * only those in the __all__ gets imported
            list cannot be passed as path argument only :
                int, str, float




# microservice-demo

This is a template application for an API based micro services.

The example service used to handle translations of coded values
is implemented in a separate python module 'codes.py',
and is then included in the main app as 'codes_router'.

This demo application also includes a YAML based configuration file,
and round logging files are used for info and debug logging.

Asyncio is used to run the python code in async mode.

## Installation

    # On Linux:
    git clone https://github.com/sharkdata/microservice-demo.git
    cd microservice-demo
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # On Windows (with example path to Python).
    git clone https://github.com/sharkdata/microservice-demo.git
    cd codes
    C:\Python39\python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Run from command line

Example for Windows:

    # Go to directory:
    cd microservice-demo
    # Activate the virtual environment for Python:
    venv\Scripts\activate
    
    # Run:
    python demoapi_start.py

Start a web browser and connect with the address:

    http://localhost:8000/

The OpenAPI 3 window can be found here:

    http://localhost:8000/docs

## Contact

shark@smhi.se

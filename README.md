# Appointment scheduler

## Overview
This a simple service to help users schedule appointments.
The service has these requirements:
all appointments must start and end on the hour or half hour
all appointments are exactly 30 minutes long
a user can only have 1 appointment on a calendar date

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/mmarrari/scheduler/1.0.0/ui/
```

The API documentation is doc folder in the root directory:

```
documentation: index.html
openapi 3.0 spec: openapi3.yaml
```
To make a request to the api you could import the openapi3.yaml file in programs like insomnia / postman to already have the collection generated

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t appointment_scheduler .

# starting up a container
docker run -p 8080:8080 appointment_scheduler
```
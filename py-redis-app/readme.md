# Redis Demo App Python
This is a basic python web application to store and retreive values against key from Redis. 

## Deployment
To use the application, you must have [Docker and Docker Compose](https://www.docker.com/) installed. <br>
First you ned to pull the redis image. <br>
> ``` docker-compose pull``` 
>
Build the app
> ``` docker-compose build``` 
>
Start services
> ``` docker-compose up -d``` 
>
See services status
> ``` docker-compose ps``` 
>
See services logs
> ``` docker-compose logs -f``` 
>

## Python App
Web application is using Flask and built on top of latest version of python. `app.py` contains two endpoints, one for POST and one for GET calls.  


## Test
To test POST and GET endpoints for project curl commands suffice otherwise open [Postman](https://www.postman.com/) and send POST, GET curls to the application. 

### POST data 
> ` curl -X POST http://localhost:9001/
   -H 'Content-Type: application/json'
   -d '{"key":"mykey","value":"myval"}' `
>


### GET data
> ``` curl http://localhost:9001/<key>```
>
Simple API app, using tortoise-ORM and FastAPi framework
Supports 2 kind of requests:
- POST to create order
- GET to obtain data on exact date

POST router: 'http://<your_domain>/order'
POST required fields:
- animal_name
- room_number
- breed_name
- dogsitter_name

GET router 'http://<your_domain>/{date}'
- GET required parametr: date   - string, YY-mm-dd

Starting app:

cd src
fastapi dev main.py

NB!
uvicorn is used

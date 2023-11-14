### Clone repo
`git clone git@github.com:dbads/ghibli-project.git`

### Setup secrests
create a `.env` file in the root of folder parallel to manage.py file and put following secrets in it

`API_KEY=apikey` <br>
`REDIS_HOST=localhost`

### Create a virtual environment
`python -m venv venv`

### Activate env
`source venv/bin/activate`

### Running server
`python manage.py runserver`

### Running tests
`python manage.py test`

#### To test the endpoint, hit the following url
`localhost:8000/films?id=2baf70d1-42bb-4437-b551-e5fed5a87abe&API-KEY=apikey`

can change film id for different films

NOTE:
if requesting film with same id within 1 minute then the data will be fetched from cache not the db
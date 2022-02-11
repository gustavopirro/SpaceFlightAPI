# Back-end Challenge 🏅 2021 - Space Flight News

### API REST Created as a challenge by Coodesh
#### Features
✅Token Auth<br>
✅Pagination<br>
✅Session Auth<br>
✅Unit tests<br>
✅Read Only mode for non-authenticated Users<br>
✅OOP Code Based<br>
✅Django-admin Interface<br>

## Endpoints
```
http://127.0.0.1:8000/articles - Return list with all API articles - Accepts GET/POST Method
http://127.0.0.1:8000/articles/<id>/ - Return article with given id - Accepts GET/PUT/DELETE Method
```
## Port
```
Default port is 8000, but can be changed on server run (Description below).
```

## Params
| Name   |      Type      |  Description | Required
|:----------:|:-------------:|:----------:|:------:|
| Id |  Int | Id of desired article | No


## How to use

## - Run project with Docker

### Clone the repository
```
git clone https://github.com/gustavopirro/SpaceFlightAPI.git
```

### Enter the project folder
```
cd path/of/project
```

### Create and run docker containers
```
docker compose up
```

### Inside the docker container run the command to populate your database with Space Flight News API Articles
```
python manage.py updatedatabase # This will loop through Space Flight News API Articles and save it in your local Database, you can acess the saved data in localhost:8000/articles endpoint
```


## - Run project without Docker

### Clone the repository
```
git clone https://github.com/gustavopirro/SpaceFlightAPI.git
```
### Enter the project folder
```
cd path/of/project
```

### Create virtual enviroment
```
python -m venv venv
```

### Activate virtual enviroment
```
venv/scripts/activate
```

### Download and install dependencies
```
pip install -r requirements.txt
```

### Create 'local_settings.py' file inside SpaceFlight folder, in the same directory as settings.py.
```
|---Root
|---manage.py
|---SpaceFlight Folder
|------settings.py
|------local_settings.py
```

### Generate a new secret key, you can use the site below:
[https://djecrety.ir/](https://djecrety.ir/)

### In local_settings.py, create a variable named SECRET_KEY and asign your generated secrey key
```
SECRET_KEY = 'generated_key_here' 
```

## PostgreSQL Configuration
### With postgreSQL installed in your local machine, add the code bellow in your local_settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'HOST': 'db_host',
        'PORT': 'db_port',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
    }
}
```

### Change the fields db_name, db_host, db_port, db_user and db_password accordingly
example:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'HOST': 'localhost'
        'PORT': '5432',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
    }
}
```

### Don't forget to created a new db in your postgreSQL with the same name of your DB_NAME local_settings value

### With your terminal in the project root folder, run the following command:
```
python manage.py migrate # This will create the required tables inside your postgre database.
```

## Running the server
### Again in the project root folder, run the server with the command:
```
python manage.py runserver
```
### If you want to use a port other than 8000, run the command like this:
```
python manage.py runserver 127.0.0.1:desired_port
```

### Populate your database with Space Flight News API Articles
```
python manage.py updatedatabase # This will loop through Space Flight News API Articles and save it in your local Database, you can acess the saved data in localhost:8000/articles endpoint
```

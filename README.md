# browser-code-executor

It is final task from EPAM training center. Application represents simple 
browser code executor that is written by using django framework.

### Installation:

Development running:

$ docker-compose -f docker-compose.yml up -d --build

Prod running:

$ docker-compose -f docker-compose.prod.yml up -d --build

### Rebuild:

Development running:

$ docker-compose down -v

$ docker-compose build

$ docker-compose up -d

Prod running:

$ docker-compose -f docker-compose.prod.yml down -v

$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

### Verification 
Development running:

http://localhost:8000/

Prod running:

http://localhost:1337/

### appearance

![Пример работы](https://raw.githubusercontent.com/skosarew/browser-code-executor/master/appearance.png)
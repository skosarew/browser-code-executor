# browser-code-executor

This application represents simple browser code executor.

## To start do the following:

docker build -t browser-executor .

docker run -it --publish=8000:8000 browser-executor

python3 manage.py runserver 0.0.0.0:8000
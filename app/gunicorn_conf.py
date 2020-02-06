import multiprocessing

# workers = multiprocessing.cpu_count() * 2

bind = "0.0.0.0:8000"
accesslog = '/home/app/web/gunicorn-access.log'
errorlog = '/home/app/web/gunicorn-error.log'
# workers = 1
# threads = 12


# timeout - Workers silent for more than this many seconds are killed
# and restarted
loglevel = 'debug'
# keepalive = 1
timeout = 30

# worker-connections = 3

def foo():
    print('wtf')


import multiprocessing

# Server Socket
bind = 'unix:/run/gunicorn.sock'
backlog = 2048

# Worker Processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 500
timeout = 10
keepalive = 3
debug = False
spew = False

# Logging
logfile = '/var/www/apps/sampleapp/app.log'
loglevel = 'info'
logconfig = None

# Process Name
proc_name = 'gunicorn_my_app'

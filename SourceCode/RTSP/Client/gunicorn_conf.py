from multiprocessing import cpu_count

chdir = '/home/tss_1171240/Repository/Python/RTSP/Client'

# Socket Path
bind = 'localhost:8000'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'info'
accesslog = '~/Repository/Python/RTSP/access_log'
errorlog = '~/Repository/Python/RTSP/error_log'

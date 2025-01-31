import os

from multiprocessing import cpu_count

def main():
    chdir = '/home/tss_1171240/Repository/Python/RTSP/Client'
    
    # Socket Path
    bind = 'localhost:58000'
    
    # Worker Options
    workers = cpu_count() + 1
    worker_class = 'uvicorn.workers.UvicornWorker'
    
    # Logging Options
    loglevel = 'info'
    
    accesslog = '~/Repository/Python/RTSP/access_log'
    if not os.path.exists(accesslog):
        os.mkdir(accesslog)
    
    errorlog = '~/Repository/Python/RTSP/error_log'
    if not os.path.exists(errorlog):
        os.mkdir(errorlog)

if __name__ == '__main__':
    main()

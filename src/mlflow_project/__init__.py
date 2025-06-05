import os
import sys
import logging

logging_str = '[%(asctime)s: %(levelname)s - %(module)s - %(message)s]'

logdir = 'logs'
log_fpath = os.path.join(logdir, 'running_logs.log')
os.makedirs(logdir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    handlers=[
        logging.FileHandler(log_fpath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("MlflowProjectLogger")
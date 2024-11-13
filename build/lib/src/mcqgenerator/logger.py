import logging
import os
from datetime import datetime

# Collect the current time
# the filename will be the date-time extraction below
# signifying the exact time code got executed.
# this generates the name of the logfile
LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}.log"

# Creating the folder to house our logfiles:
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok = True)

# Create the logfile in the folder
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Create logging object
logging.basicConfig(level = logging.INFO,
    filename = LOG_FILEPATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
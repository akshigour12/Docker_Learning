import logging
import random
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

while True:
    logging.info("Application Started")

    if random.randint(1,5) == 3:
        logging.warning("High CPU Usage")

    if random.randint(1,8) == 5:
        logging.error("Database Connection Failed")

    time.sleep(5)

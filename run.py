import os
import json
import time
import requests
import traceback
import logging

from configparser import ConfigParser


# Logger
logging.basicConfig(
    # filename="run.logs",
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%H:%M:%S"
)

# Create logger
log = logging.getLogger("rotate.run")
log.setLevel(logging.DEBUG)


# Config file
log.info("Loading config file.")
config_file = os.path.join(os.getcwd(), "config.ini")
config = ConfigParser()
config.read(config_file)


# Config vars
log.info("Setting config variables.")
ROTATE_INTERVAL_IN_SECONDS = int(config.get("ROTATE", "ROTATE_INTERVAL_IN_SECONDS"))
ENDPOINTS = json.loads(config.get("ROTATE", "ENDPOINTS"))


while True:
	try:
		for endpoint in ENDPOINTS:
			log.info(f"Rotating: {endpoint}")
			response = requests.get(endpoint, timeout=60)
			
			log.info(f"Result: {response.text}")

		log.info(f"Sleeping for {ROTATE_INTERVAL_IN_SECONDS}s")
		time.sleep(ROTATE_INTERVAL_IN_SECONDS)

	except KeyboardInterrupt:
		log.info("KeyboardInterrupt, exiting.")
		break

	except:
		log.error(traceback.format_exc())
		log.error("Failed to rotate.")

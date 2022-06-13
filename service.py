import requests
import logging

logger = logging.getLogger(__name__)

#DINNING_HALL_BASE_URL = "http://dinning-hall-container:5001"
DINNING_HALL_BASE_URL = "http://127.0.0.1:5001"

def send_distribution_request(distribution):
    logging.info(f"Sending post request to {DINNING_HALL_BASE_URL}/distribution, id = " + str(distribution['order_id']))

    r = requests.post(f'{DINNING_HALL_BASE_URL}/distribution', json=distribution)

    logging.info(f"Response status code: " + str(r.status_code))
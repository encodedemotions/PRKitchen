import logging

from domain.kitchen import Kitchen
import threading
from flask import Flask, request
from flask.json import jsonify
import utils
import time

#Cream virtual environment venv (python3 -m venv venv), de activat venv (source venv/bin/activate), de instalat dependențele (pip3 install -r requirements.txt); python3 app.py

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(name)s:%(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)


app = Flask(__name__)
kitchen = None

@app.route('/order', methods=['POST'])
def receive_order():
    logger.debug(f"Received order, time: {time.time()}")

    order = request.json

    logger.debug(f"Order {order['order_id']} received. Notifying cooks...")

    kitchen.receive_order(order)

    return jsonify(order)




if __name__ == "__main__":
    threading.Thread(target=lambda: {
         app.run(debug=True, use_reloader=False, host="0.0.0.0", port=5010)
    }).start()

    kitchen = Kitchen()
    kitchen.run_simulation()
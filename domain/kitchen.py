from datetime import datetime
from queue import PriorityQueue
import logging
import time
from config import COOKS, TIME_DELTA
from domain.menu import RestaurantMenu
from domain.order import Order
import threading
import service
from settings import OVENS, STOVES

import utils
from .cooking_aparatus import CookingAparatus

logger = logging.getLogger(__name__)


class Kitchen():
    def __init__(self, ovens_n=OVENS, stoves_n=STOVES) -> None:
        self.order_list = PriorityQueue()
        self.menu:RestaurantMenu = RestaurantMenu()
        self.cooks = utils.read_cooks(self)[:COOKS]
        self.cooking_apparatus = {
            "oven": [CookingAparatus("oven") for i in range(ovens_n)],
            "stove": [CookingAparatus("stove") for i in range(stoves_n)] 
        }

        self.order_list_mutex = threading.Lock()
        self.apparatus_mutex = threading.Lock()
        
    
    def run_simulation(self):
        logging.info("Starting kitchen simulation...")
        for cook in self.cooks:
            threading.Thread(target=cook.start_working).start() 

        while True:
            for _, order in self.order_list.queue: 
                if order.is_finished() and order.is_delivered == False:
                    logging.info(f"order {order.order_id} is ready!")

                    order.cooking_time = datetime.utcnow().timestamp() - order.received_time
                    order.is_delivered = True
                    distribution = utils.order_to_distribution(order)

                    service.send_distribution_request(distribution)

                    break

            while not self.order_list.empty() and self.order_list.queue[0][1].is_finished():
                top = self.order_list.get()

            time.sleep(TIME_DELTA)


    def receive_order(self, request_order):
        order_id = request_order['order_id']
        table_id = request_order['table_id']
        waiter_id = request_order['waiter_id']
        items = request_order['items']
        priority = request_order['priority']
        max_wait = request_order['max_wait']
        pick_up_time = request_order['pick_up_time']

        order = Order(order_id, table_id, waiter_id, items, priority, pick_up_time, max_wait, self.menu)

        self.order_list.put((-order.priority, order))


    

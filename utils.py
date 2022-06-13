import json
from os import name
from domain.order import Order
from domain.cook import Cook


def order_to_distribution(order: Order):
    distribution = {
        "order_id": order.order_id,
        "table_id": order.table_id,
        "waiter_id": order.waiter_id,
        "items": order.items,
        "priority": order.priority,
        "max_wait": order.max_wait,
        "pick_up_time": order.pick_up_time,
        "cooking_time": order.cooking_time,
        "cooking_details": [{ "food_id": food_item.item_id, "cook_id": food_item.cook_id} for food_item in order.food_items ]
    }

    return distribution

def read_cooks(kithen):
    cooks = []

    with open('cooks.json') as file:
        data  = json.load(file)

    cooks = [Cook(kitchen=kithen, id=i,  rank=cook['rank'],
                    proficiency=cook['proficiency'], 
                    name=cook['name'], catch_phrase=cook['catch-phrase']) for i, cook in enumerate(data)]

    return cooks
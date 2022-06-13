import json

class RestaurantMenu:
    def __init__(self) -> None:
        self.foods = []

        with open('menu.json') as file:
            data  = json.load(file)

        self.foods = {item['id']:item for item in data}


    def get_preparation_time(self, item_id):
        return self.foods[item_id]['preparation-time']
        
    def get_complexity(self, item_id):
        return self.foods[item_id]['complexity']


    def get_apparatus(self, item_id):
        return self.foods[item_id]['cooking-apparatus']
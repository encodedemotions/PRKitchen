
import enum
from domain import kitchen
from domain.menu import RestaurantMenu

class FoodItemState(enum.Enum):
    NOT_DISTRIBUTED = 1,
    IN_PREPARATION = 2,
    PREPARED = 3


class FoodItem:
    def __init__(self, order_id, item_id, menu: RestaurantMenu) -> None:
        self.order_id = order_id
        self.item_id = item_id
        self.estimated_preparation_time = None
        self.preparation_time = menu.get_preparation_time(item_id)
        self.state:FoodItemState = FoodItemState.NOT_DISTRIBUTED
        self.apparatus = menu.get_apparatus(item_id)
        self.complexity = menu.get_complexity(item_id)
        self.cook_id = None
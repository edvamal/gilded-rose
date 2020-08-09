from item import Item
from item_catalog import ItemCatalog


class ItemService:
    def increment_quality(self, item: Item, quantity: int = 1) -> Item:
        if item.quality < 50:
            item.quality += quantity
        return item

    def check_item_sell_in(self, item: Item) -> Item:
        if item.sell_in < 11:
            self.increment_quality(item)
        elif item.sell_in < 6:
            self.increment_quality(item)
        return item

    def decrement_quality(self, item: Item, quantity: int = 1) -> Item:
        if item.quality > 0:
            item.quality -= quantity
        return item

    def decrement_quality_if_not_in_catalog(self, item: Item) -> Item:
        if self.__is_item_not_in_catalog(item):
            self.decrement_quality(item)
        return item

    def __is_item_not_in_catalog(self, item: Item) -> bool:
        return True if (item.name != ItemCatalog.Aged_Brie and
                        item.name != ItemCatalog.Backstage and
                        item.name != ItemCatalog.Sulfuras) else False

    def update_item_if_sell_in_below_zero(self, item: Item) -> Item:
        if item.sell_in < 0:
            self.decrement_quality(item) if self.__is_item_not_in_catalog(item) else self.decrement_quality(item,
                                                                                                            item.quality)
        else:
            self.increment_quality(item)
        return item

    def __update_based_on_catalog(self, item: Item, catalog: ItemCatalog):
        if catalog == ItemCatalog.Backstage:
            if item.name == catalog.Backstage:
                self.increment_quality(item, 1)
                self.check_item_sell_in(item)
        elif catalog == ItemCatalog.Sulfuras:
            if item.name != catalog.Sulfuras:
                item.sell_in -= 1

    def update_item(self, item: Item):
        self.decrement_quality_if_not_in_catalog(item)
        for cat in ItemCatalog: self.__update_based_on_catalog(item, cat)
        self.update_item_if_sell_in_below_zero(item)

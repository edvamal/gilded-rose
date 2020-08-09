# -*- coding: utf-8 -*-
from typing import List

from item import Item
from item_service import ItemService


class GildedRose:
    __item_service = ItemService()

    def __init__(self, items: List[Item]):
        self.__items = items

    def update_quality(self):
        for item in self.__items:
            self.__item_service.update_item(item)

    @property
    def items(self):
        return self.__items

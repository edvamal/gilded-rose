# -*- coding: utf-8 -*-

import pytest
from pytest import *

from gilded_rose import GildedRose
from item import Item


@pytest.fixture
def gildedrose_test_fixture() -> GildedRose:
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
    return GildedRose(items)


def test_item_name(gildedrose_test_fixture: GildedRose):
    gildedrose_test_fixture.update_quality()
    assert "+5 Dexterity Vest" == gildedrose_test_fixture.items[0].name


def test_sell_in_change(gildedrose_test_fixture: GildedRose):
    gildedrose_test_fixture.update_quality()
    assert gildedrose_test_fixture.items[0].sell_in == 9


def test_quality_change(gildedrose_test_fixture: GildedRose):
    gildedrose_test_fixture.update_quality()
    assert gildedrose_test_fixture.items[0].quality == 20


def test_result_print(mocker, gildedrose_test_fixture: GildedRose):
    mock_print = mocker.patch('builtins.print')
    print(gildedrose_test_fixture.items[0])
    assert mock_print.call_args == ((gildedrose_test_fixture.items[0],),)

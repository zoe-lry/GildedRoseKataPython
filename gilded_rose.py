# gilded_rose.py

from abc import ABC, abstractmethod

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemStrategy(ABC):
    """Abstract base class for item update strategies."""
    @abstractmethod
    def update_quality(self, item):
        pass


class NormalItemStrategy(ItemStrategy):
    def update_quality(self, item):
        degrade = 1
        if item.sell_in <= 0:
            degrade *= 2

        item.quality -= degrade
        if item.quality < 0:
            item.quality = 0

        item.sell_in -= 1


class AgedBrieStrategy(ItemStrategy):
    def update_quality(self, item):
        increase = 1
        if item.sell_in <= 0:
            increase *= 2

        item.quality += increase
        if item.quality > 50:
            item.quality = 50

        item.sell_in -= 1


class SulfurasStrategy(ItemStrategy):
    def update_quality(self, item):
        pass


class BackstagePassesStrategy(ItemStrategy):
    def update_quality(self, item):
        if item.sell_in > 10:
            item.quality += 1
        elif item.sell_in > 5:
            item.quality += 2
        elif item.sell_in > 0:
            item.quality += 3
        else:
            item.quality = 0

        if item.quality > 50:
            item.quality = 50

        item.sell_in -= 1


class ConjuredItemStrategy(ItemStrategy):
    def update_quality(self, item):
        degrade = 2
        if item.sell_in <= 0:
            degrade *= 2

        item.quality -= degrade
        if item.quality < 0:
            item.quality = 0

        item.sell_in -= 1


class GildedRose:
    def __init__(self, items):
        self.items = items
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesStrategy(),
            "Conjured Mana Cake": ConjuredItemStrategy(),
            "Conjured": ConjuredItemStrategy(),
        }

    def update_quality(self):
        for item in self.items:

            if not isinstance(item.quality, int) or not isinstance(item.sell_in, int):
                item.quality = None
                continue

            if item.quality < 0 or (item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros"):
                item.quality = None
                continue

            strategy = self.strategies.get(item.name, NormalItemStrategy())
            strategy.update_quality(item)

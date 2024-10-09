# -*- coding: utf-8 -*-

"""
Refactor the source code with Behavioural Pattern to encapsulate the behavior for different types of items.
e.g., regular items, Aged Brie, Backstage Passes, and Sulfuras.
This approach will simplify the update_quality method by letting each item type handle its own specific behavior in separate classes.
"""
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


class UpdateStrategy:
    """Base strategy class for updating items."""
    def update(self, item: Item):
        raise NotImplementedError("This method should be overridden by subclasses")


# inherit from the base class UpdateStrategy
class RegularItemStrategy(UpdateStrategy):
    """Strategy for regular items."""
    def update(self, item: Item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieStrategy(UpdateStrategy):
    """Strategy for Aged Brie."""
    def update(self, item: Item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class BackstagePassesStrategy(UpdateStrategy):
    """Strategy for Backstage Passes."""
    def update(self, item: Item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 10 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 5 and item.quality < 50:
                item.quality += 1
        if item.sell_in < 0:
            item.quality = 0


class SulfurasStrategy(UpdateStrategy):
    """Strategy for Sulfuras, Hand of Ragnaros (Legendary Item)."""
    def update(self, item: Item):
        # Sulfuras does not change in sell_in or quality.
        pass


class GildedRose:
    """Context class that uses strategies to update items."""
    def __init__(self, items: list[Item]):
        self.items = items
        # align with the test cases
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
        }

    def update_quality(self):
        for item in self.items:
            # get strategy of the item, if no specific strategy, then use RegularItemStrategy() as default one
            strategy = self.strategies.get(item.name, RegularItemStrategy()) 
            strategy.update(item)

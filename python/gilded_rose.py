# -*- coding: utf-8 -*-

MAX_QUALITY=50
MIN_QUALITY=0

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            item.sell_in -= 1
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass(item)
            else:
                self._update_normal(item)

    def _update_normal(self, item):
        # Degrades 1/day, 2/day after sell_in passes
        if item.sell_in < 0:
            item.quality = max(MIN_QUALITY, item.quality - 2)
        else:
            item.quality = max(MIN_QUALITY, item.quality - 1)

    def _update_aged_brie(self, item):
        # Appreciates 1/day, 2/day after sell_in passes
        if item.sell_in < 0:
            item.quality = min(MAX_QUALITY, item.quality + 2)
        else:
            item.quality = min(MAX_QUALITY, item.quality + 1)

    def _update_backstage_pass(self, item):
        # Drops to 0 after concert
        # +3 when <= 5 days, +2 when <= 10 days, +1 otherwise
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(MAX_QUALITY, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(MAX_QUALITY, item.quality + 2)
        else:
            item.quality = min(MAX_QUALITY, item.quality + 1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

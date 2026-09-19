# -*- coding: utf-8 -*-

MAX_QUALITY=50
MIN_QUALITY=0

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > MIN_QUALITY:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < MAX_QUALITY:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 0:
                            item.quality = MIN_QUALITY
                        if item.sell_in < 10:
                            item.quality = min(MAX_QUALITY, item.quality + 1)
                        if item.sell_in < 5:
                            item.quality = min(MAX_QUALITY, item.quality + 2)
                        else:
                            item.quality = min(MAX_QUALITY, item.quality + 1)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > MIN_QUALITY:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = MIN_QUALITY
                else:
                    if item.quality < MAX_QUALITY:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

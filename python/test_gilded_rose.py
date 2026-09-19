# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class TestNormalItems(unittest.TestCase):

    def test_quality_decreases_by_one(self):
        items = [Item("Normal Item", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 19)

    def test_sell_in_decreases_by_one(self):
        items = [Item("Normal Item", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].sell_in, 9)

    def test_quality_degrades_twice_after_sell_in(self):
        items = [Item("Normal Item", sell_in=0, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 18)

    def test_quality_never_negative(self):
        items = [Item("Normal Item", sell_in=5, quality=0)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_quality_floor_after_sell_in(self):
        items = [Item("Normal Item", sell_in=-1, quality=1)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)


class TestAgedBrie(unittest.TestCase):

    def test_quality_increases_by_one(self):
        items = [Item("Aged Brie", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_quality_increases_by_two_after_sell_in(self):
        items = [Item("Aged Brie", sell_in=0, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", sell_in=10, quality=50)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_quality_at_49_caps_at_50(self):
        items = [Item("Aged Brie", sell_in=10, quality=49)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 50)


class TestSulfuras(unittest.TestCase):

    def test_quality_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 80)

    def test_sell_in_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].sell_in, 10)


class TestBackstagePasses(unittest.TestCase):

    def test_quality_increases_by_one_normally(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_quality_increases_by_two_at_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_quality_increases_by_three_at_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 23)

    def test_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_quality_never_exceeds_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 50)


class TestConjured(unittest.TestCase):

    def test_quality_decreases_by_two(self):
        items = [Item("Conjured Mana Cake", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 18)

    def test_quality_decreases_by_four_after_sell_in(self):
        items = [Item("Conjured Mana Cake", sell_in=0, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 16)

    def test_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", sell_in=5, quality=1)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)


class TestEdgeCases(unittest.TestCase):

    def test_multiple_items_updated_independently(self):
        items = [
            Item("Normal Item", sell_in=10, quality=20),
            Item("Aged Brie", sell_in=10, quality=20),
            Item("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80),
        ]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[1].quality, 21)
        self.assertEqual(items[2].quality, 80)

    def test_empty_list_no_error(self):
        GildedRose([]).update_quality()


if __name__ == '__main__':
    unittest.main(verbosity=2)

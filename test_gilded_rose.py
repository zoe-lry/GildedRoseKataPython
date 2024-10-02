# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)


    def test_vest_item_greater_than_50(self):
        vest = "test"
        items = [Item(vest, 1, 60)]
        gr = GildedRose(items)

        gr.update_quality()
        self.assertEqual(items[0].quality, None)


    def test_vest_item_with_wrong_quality_type(self):
        vest = "test"
        items = [Item(vest, "aa", "aa")]
        # gr = GildedRose(items)

        self.assertEqual(items[0].quality, None)
    

    def test_Conjured_degrade_twice_as_normal(self):
        vest = "Conjured"
        items = [Item(vest, 10, 10)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(items[0].quality, 8)


if __name__ == '__main__':
    unittest.main()

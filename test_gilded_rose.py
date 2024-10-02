# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        
        
    def test_vest_item_should_decrease_after_one_day(self):

        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)

        gr.update_quality()
        
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[1].sell_in, 8)
        self.assertEqual(items[1].quality, 18)
        self.assertEqual(items[2].sell_in, 3)
        self.assertEqual(items[2].quality, 5)
        

        # or just write a enumerate loop to test
        # expected_items = [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]
        # for i, item in enumerate(gr.items):
        #     assert item.name == expected_items[i].name
        #     assert item.sell_in == expected_items[i].sell_in
        #     assert item.quality == expected_items[i].quality
        
        
    def test_aged_brie_increases_in_quality(self):
        name = "Aged Brie"
        items = [Item(name, 2, 0)]  # Item starts with sell_in = 2 days, quality = 0
        gr = GildedRose(items)

        # Call update_quality for 3 days to check the progression
        gr.update_quality()  # Day 1
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 1)  # Quality increases by 1

        gr.update_quality()  # Day 2
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 2)  # Quality increases by 1 again

        gr.update_quality()  # Day 3 (sell_in < 0)
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 4)  # Quality increases by 2 after sell_in < 0

    def test_sulfuras_hand_of_agnaros_in_quality(self):
        name = "Sulfuras, Hand of Ragnaros"
        items = [Item(name, 2, 0), Item(name, 12, 0), Item(name, 22, 0)]  # Item starts with sell_in = 2 days, quality = 0
        gr = GildedRose(items)
        
        # Update quality for 5 days
        for _ in range(5):
            gr.update_quality()
            
        for item in items:
            assert item.quality == 0 # Quality does not change by sell_in days
            
        assert items[0].sell_in == 2
        assert items[1].sell_in == 12
        assert items[2].sell_in == 22 # Sell_in does not change by sell_in days
            
        
if __name__ == '__main__':
    unittest.main()

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
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)
        gr.update_quality()

        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[1].sell_in, 8)
        self.assertEqual(items[1].quality, 18)
        self.assertEqual(items[2].sell_in, 3)
        self.assertEqual(items[2].quality, 5)

    def test_aged_brie_increases_in_quality(self):
        name = "Aged Brie"
        items = [Item(name, 2, 0)]
        gr = GildedRose(items)

        gr.update_quality()
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 1)

        gr.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 2)

        gr.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 4)

    def test_sulfuras_hand_of_agnaros_in_quality(self):
        name = "Sulfuras, Hand of Ragnaros"
        items = [Item(name, 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()

        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 80)


if __name__ == '__main__':
    unittest.main()

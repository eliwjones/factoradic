import random
import unittest

from factoradic import number_to_deck, deck_to_number


class TestFactoradic(unittest.TestCase):

    def test_factoradic(self):
        number = random.randrange(2**128)
        deck = number_to_deck(number=number)

        print(f"\n\nnumber: {number}\n")
        print(f"shuffled deck: {deck}\n")

        self.assertEqual(number, deck_to_number(deck=deck))

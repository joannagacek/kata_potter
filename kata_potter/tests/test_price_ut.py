import unittest

from kata_potter.price import price

# Test funkcji kata_potter.price, wyliczającej cenę za wypożeczenie książek
class TestPrice(unittest.TestCase):

    # Lista zniżek tj. np. za 2 książki cena wynosi 95% ceny jednostkowej itd.
    discount = [0, 1, 0.95, 0.9, 0.80, 0.75]

    test_data = [
        # Test elementarny
        [0, list([])],
        [8, list([0])],
        [8, list([1])],
        [8, list([2])],
        [8, list([3])],
        [8, list([4])],
        [8 * 2, list([0, 0])],
        [8 * 3, list([1, 1, 1])],
        # Test podstawowych zniżek
        [8 * 2 * 0.95, list([0, 1])],
        [8 * 3 * 0.9, list([0, 2, 4])],
        [8 * 4 * 0.8, list([0, 1, 2, 4])],
        [8 * 5 * 0.75, list([0, 1, 2, 3, 4])],
        # Test zniżek łączonych
        [8 + (8 * 2 * 0.95), list([0, 0, 1])],
        [2 * (8 * 2 * 0.95), list([0, 0, 1, 1])],
        [(8 * 4 * 0.8) + (8 * 2 * 0.95), list([0, 0, 1, 2, 2, 3])],
        [8 + (8 * 5 * 0.75), list([0, 1, 1, 2, 3, 4])],
        # Test przypadków granicznych
        [2 * (8 * 4 * 0.8), list([0, 0, 1, 1, 2, 2, 3, 4])],
        [3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8), list([0, 0, 0, 0, 0,
           1, 1, 1, 1, 1,
           2, 2, 2, 2,
           3, 3, 3, 3, 3,
           4, 4, 4, 4])],
    ]

    def test_kata_potter(self):
        # Dla wszystkich danych testowych test_data upewnij się, że funkcja price zwraca poprawną kwotę do zapłaty
        for idx, data in enumerate(self.test_data):
            self.assertEqual(data[0], price(data[1], self.discount), "Test failed at test_data[%d]" % (idx))


if __name__ == '__main__':
    unittest.main()
import unittest
from src.model import PricingModel
from src.domain import Apartment

class TestPricing(unittest.TestCase):
    def setUp(self):
        self.model = PricingModel()
        # Добавляем тестовые данные вручную (без файла)
        self.model.data = [
            Apartment(100, 3, 5, 10_000_000),
            Apartment(50, 1, 2, 5_000_000)
        ]

    def test_statistics(self):
        stats = self.model.get_statistics()
        self.assertEqual(stats["Средняя цена"], 7_500_000)
        self.assertEqual(stats["Макс. площадь"], 100)

    def test_prediction(self):
        self.model.train_model()
        # Линейная зависимость идеальная: 100м->10млн, 50м->5млн.
        # Значит 75м должно быть 7.5млн
        price = self.model.predict_price(75, 2)
        self.assertAlmostEqual(price, 7_500_000, delta=1000)

if __name__ == '__main__':
    unittest.main()
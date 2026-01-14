import pandas as pd
from typing import List, Dict
from src.domain import RealEstateObject, Apartment
from src.strategies import IRegressionStrategy, LinearStrategy, ForestStrategy


class PricingModel:
    def __init__(self):
        self.data: List[RealEstateObject] = []
        # По умолчанию используем Линейную регрессию
        self.strategy: IRegressionStrategy = LinearStrategy()

    def load_data_from_csv(self, filepath: str):
        df = pd.read_csv(filepath, sep=',')
        self.data.clear()
        # Фабричный метод (упрощенный) создания объектов из строк CSV
        for _, row in df.iterrows():
            apt = Apartment(row['area'], row['rooms'], row['floor'], row['price'])
            self.data.append(apt)

    def get_statistics(self) -> Dict[str, float]:
        if not self.data:
            return {}
        prices = [x.price for x in self.data]
        areas = [x.area for x in self.data]
        return {
            "Средняя цена": sum(prices) / len(prices),
            "Макс. площадь": max(areas),
            "Всего объектов": len(prices)
        }

    def set_strategy(self, strategy: IRegressionStrategy):
        self.strategy = strategy

    def train_model(self):
        if not self.data:
            raise ValueError("Нет данных для обучения!")

        # Подготовка данных для sklearn
        df = pd.DataFrame([vars(o) for o in self.data])
        X = df[['area', 'rooms']]  # Обучаем по площади и комнатам
        y = df['price']

        self.strategy.train(X, y)


    def predict_price(self, area: float, rooms: int) -> float:
        # Создаем DataFrame из одного элемента для прогноза
        input_data = pd.DataFrame([[area, rooms]], columns=['area', 'rooms'])
        return self.strategy.predict(input_data)
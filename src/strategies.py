from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# Интерфейс стратегии
class IRegressionStrategy(ABC):
    @abstractmethod
    def train(self, X: pd.DataFrame, y: pd.Series):
        pass

    @abstractmethod
    def predict(self, X: pd.DataFrame) -> float:
        pass

# Стратегия 1: Линейная регрессия
class LinearStrategy(IRegressionStrategy):
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)[0]

# Стратегия 2: Случайный лес
class ForestStrategy(IRegressionStrategy):
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)[0]
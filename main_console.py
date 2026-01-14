import os
from src.model import PricingModel
from src.view import ConsoleView
from src.presenter import Presenter

if __name__ == "__main__":
    # Настройка путей
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'dataset.csv')

    # Инициализация MVP
    model = PricingModel()
    view = ConsoleView()
    presenter = Presenter(view, model)

    # Запуск
    presenter.run_workflow(csv_path)
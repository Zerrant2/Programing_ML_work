from src.model import PricingModel
from src.view import IView


class Presenter:
    def __init__(self, view: IView, model: PricingModel):
        self.view = view
        self.model = model

    def run_workflow(self, csv_path: str):
        self.view.show_message("Запуск приложения...")

        # 1. Загрузка данных
        try:
            self.model.load_data_from_csv(csv_path)
            self.view.show_message(f"Данные загружены из {csv_path}")
        except Exception as e:
            self.view.show_message(f"Ошибка загрузки: {e}")
            return

        # 2. Показ статистики
        stats = self.model.get_statistics()
        self.view.show_stats(stats)

        # 3. Обучение модели
        self.view.show_message("Обучение ML модели (Линейная регрессия)...")
        self.model.train_model()
        self.view.show_message("Модель обучена.")

        # 4. Пример прогноза (захардкоженный тест)
        test_area = 55
        test_rooms = 2
        predicted = self.model.predict_price(test_area, test_rooms)
        self.view.show_message(f"Прогноз для {test_area}м2, {test_rooms} комн. -> {predicted:,.2f} руб.")
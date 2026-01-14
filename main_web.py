from fastapi import FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel
from src.model import PricingModel
from src.strategies import ForestStrategy, LinearStrategy
import os
from fastapi.responses import RedirectResponse

# Глобальный экземпляр модели
model = PricingModel()


# --- НОВЫЙ СПОСОБ (Lifespan) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # ЛОГИКА ЗАПУСКА (выполняется 1 раз при старте)
    csv_path = "data/dataset.csv"

    # Проверка путей для запуска из разных папок
    if not os.path.exists(csv_path):
        # Попробуем найти файл на уровень выше (если запускаем из src)
        possible_path = os.path.join("..", "data", "dataset.csv")
        if os.path.exists(possible_path):
            csv_path = possible_path

    if os.path.exists(csv_path):
        model.load_data_from_csv(csv_path)
        model.train_model()
        print(f"API: Данные загружены из {csv_path} и модель обучена.")
    else:
        print(f"API WARNING: Файл {csv_path} не найден. Модель пустая.")

    yield  # Здесь приложение работает

    # ЛОГИКА ЗАВЕРШЕНИЯ (можно очистить ресурсы, если надо)
    print("API: Остановка сервера.")


# Передаем lifespan в приложение
app = FastAPI(title="ML Real Estate API", lifespan=lifespan)


# DTO (Data Transfer Object) для запроса
class PredictionRequest(BaseModel):
    area: float
    rooms: int
    strategy: str = "linear"





# Добавляем маршрут для корня
@app.get("/")
def read_root():
    # Можно просто вернуть текст:
    # return {"message": "Сервер работает! Перейдите на /docs для проверки"}

    # А можно сразу перенаправлять на документацию (удобнее):
    return RedirectResponse(url="/docs")

@app.get("/stats")
def get_stats():
    return model.get_statistics()


@app.post("/predict")
def predict(req: PredictionRequest):
    if req.strategy == "forest":
        model.set_strategy(ForestStrategy())
    else:
        model.set_strategy(LinearStrategy())

    # При смене стратегии переобучаем (условно для лабы)
    if model.data:
        model.train_model()

    price = model.predict_price(req.area, req.rooms)
    return {
        "input": {"area": req.area, "rooms": req.rooms},
        "strategy": req.strategy,
        "predicted_price": price
    }
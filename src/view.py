from abc import ABC, abstractmethod


class IView(ABC):
    @abstractmethod
    def show_message(self, message: str): pass

    @abstractmethod
    def show_stats(self, stats: dict): pass


class ConsoleView(IView):
    def show_message(self, message: str):
        print(f"[LOG]: {message}")

    def show_stats(self, stats: dict):
        print("\n--- СТАТИСТИКА ---")
        for key, value in stats.items():
            print(f"{key}: {value}")
        print("------------------\n")
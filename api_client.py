import requests

class ApiClient:
    """
    Клас для роботи з API за допомогою HTTP запитів.

    Атрибути:
        base_url (str): Базовий URL для API, за замовчуванням використовує "https://jsonplaceholder.typicode.com".
    
    Методи:
        get(endpoint): Виконує GET-запит до зазначеного ендпоінту API та повертає відповідь.
    """

    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        """
        Ініціалізація клієнта API.

        Параметри:
            base_url (str): Базовий URL для API. За замовчуванням використовує "https://jsonplaceholder.typicode.com".
        """
        self.base_url = base_url

    def get(self, endpoint):
        """
        Виконує GET-запит до API.

        Параметри:
            endpoint (str): Шлях до конкретного ендпоінту API, до якого необхідно зробити запит.
        
        Повертає:
            Response: Об'єкт відповіді від запиту, який містить дані, статус та інші метадані.

        Виключення:
            - Викидає виняток `requests.exceptions.HTTPError`, якщо запит не успішний (наприклад, статус 4xx чи 5xx).
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)

        # Перевірка на наявність помилки у відповіді
        response.raise_for_status()  # Викидає помилку, якщо код відповіді 4xx або 5xx
        
        return response

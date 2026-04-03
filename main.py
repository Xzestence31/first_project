import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные из файла .env
    load_dotenv()
    
    # Читаем значение переменной AUTHOR
    author = os.getenv('AUTHOR')
    
    # Если переменная не найдена, используем значение по умолчанию
    if author is None:
        author = "Неизвестный автор"
    
    # Печатаем результат
    print(f"Автор проекта: {author}")

# Вызываем функцию для проверки
if __name__ == "__main__":
    print_author()
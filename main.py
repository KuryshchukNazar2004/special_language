import json
from api_client import ApiClient
from repository import UserRepository, PostRepository, CommentRepository

def main():
    """
    Основний метод, який надає користувачу вибір дій з роботи з користувачами, постами і коментарями.
    
    Запускається нескінченний цикл, в якому користувач може вибрати одну з дій:
    1. Показати список користувачів
    2. Показати деталі користувача
    3. Показати список постів
    4. Показати деталі посту
    5. Показати коментарі до посту
    6. Зберегти дані у файли
    7. Вихід з програми
    """
    
    # Створюємо об'єкти для взаємодії з API
    api_client = ApiClient()
    user_repository = UserRepository(api_client)
    post_repository = PostRepository(api_client)
    comment_repository = CommentRepository(api_client)

    while True:
        # Виведення меню для користувача
        print("Виберіть дію:")
        print("1. Показати список користувачів")
        print("2. Показати деталі користувача")
        print("3. Показати список постів")
        print("4. Показати деталі посту")
        print("5. Показати коментарі до посту")
        print("6. Зберегти дані")
        print("7. Вихід")

        # Отримуємо вибір користувача
        choice = input("Введіть номер дії: ")

        if choice == '1':
            """
            Отримує список користувачів і виводить їх у форматі JSON.
            """
            users = user_repository.get_users()  # Отримуємо список користувачів
            print(json.dumps(users, indent=4))  # Виводимо список у форматі JSON
        elif choice == '2':
            """
            Отримує користувача за ID та виводить його дані в форматі JSON.
            """
            user_id = input("Введіть ID користувача: ")
            user = user_repository.get_user_by_id(user_id)  # Отримуємо користувача за ID
            print(json.dumps(user, indent=4))
        elif choice == '3':
            """
            Отримує список постів і виводить їх у форматі JSON.
            """
            posts = post_repository.get_posts()  # Отримуємо список постів
            print(json.dumps(posts, indent=4))  # Виводимо список постів у форматі JSON
        elif choice == '4':
            """
            Отримує пост за ID і виводить його деталі у форматі JSON.
            """
            post_id = input("Введіть ID посту: ")
            post = post_repository.get_post_by_id(post_id)  # Отримуємо пост за ID
            print(json.dumps(post, indent=4))
        elif choice == '5':
            """
            Отримує коментарі до посту за його ID і виводить їх у форматі JSON.
            """
            post_id = input("Введіть ID посту: ")
            comments = comment_repository.get_comments_by_post_id(post_id)  # Отримуємо коментарі до посту
            print(json.dumps(comments, indent=4))
        elif choice == '6':
            """
            Запит на вибір даних для збереження у файл: користувачів, постів або коментарів.
            """
            print("Виберіть дані для збереження:")
            print("1. Користувачі")
            print("2. Пости")
            print("3. Коментарі")

            save_choice = input("Введіть номер: ")

            if save_choice == '1':
                """
                Зберігає дані користувачів у файл `data/users.json`.
                """
                users = user_repository.get_users()  # Отримуємо дані користувачів
                with open("data/users.json", "w") as f:
                    json.dump(users, f, indent=4)
                print("Дані користувачів збережено в data/users.json")
            elif save_choice == '2':
                """
                Зберігає дані постів у файл `data/posts.json`.
                """
                posts = post_repository.get_posts()  # Отримуємо дані постів
                with open("data/posts.json", "w") as f:
                    json.dump(posts, f, indent=4)
                print("Дані постів збережено в data/posts.json")
            elif save_choice == '3':
                """
                Зберігає дані коментарів у файл `data/comments.json`.
                """
                comments = comment_repository.get_comments()  # Отримуємо коментарі
                with open("data/comments.json", "w") as f:
                    json.dump(comments, f, indent=4)
                print("Дані коментарів збережено в data/comments.json")
            else:
                print("Неправильний вибір.")
        elif choice == '7':
            """
            Завершує програму.
            """
            print("Вихід")
            break
        else:
            print("Неправильний вибір дії.")

if __name__ == "__main__":
    main()

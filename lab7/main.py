import json
from api_client import ApiClient
from repository import UserRepository, PostRepository, CommentRepository

def main():
    api_client = ApiClient()
    user_repository = UserRepository(api_client)
    post_repository = PostRepository(api_client)
    comment_repository = CommentRepository(api_client)

    while True:
        print("Виберіть дію:")
        print("1. Показати список користувачів")
        print("2. Показати деталі користувача")
        print("3. Показати список постів")
        print("4. Показати деталі посту")
        print("5. Показати коментарі до посту")
        print("6. Зберегти дані")
        print("7. Вихід")

        choice = input("Введіть номер дії: ")

        if choice == '1':
            users = user_repository.get_users()
            print(json.dumps(users, indent=4))
        elif choice == '2':
            user_id = input("Введіть ID користувача: ")
            user = user_repository.get_user_by_id(user_id)
            print(json.dumps(user, indent=4))
        elif choice == '3':
            posts = post_repository.get_posts()
            print(json.dumps(posts, indent=4))
        elif choice == '4':
            post_id = input("Введіть ID посту: ")
            post = post_repository.get_post_by_id(post_id)
            print(json.dumps(post, indent=4))
        elif choice == '5':
            post_id = input("Введіть ID посту: ")
            comments = comment_repository.get_comments_by_post_id(post_id)
            print(json.dumps(comments, indent=4))
        elif choice == '6':
            print("Виберіть дані для збереження:")
            print("1. Користувачі")
            print("2. Пости")
            print("3. Коментарі")

            save_choice = input("Введіть номер: ")

            if save_choice == '1':
                users = user_repository.get_users() 
                with open("data/users.json", "w") as f:
                    json.dump(users, f, indent=4)
                print("Дані користувачів збережено в data/users.json")
            elif save_choice == '2':
                posts = post_repository.get_posts()
                with open("data/posts.json", "w") as f:
                    json.dump(posts, f, indent=4)
                print("Дані постів збережено в data/posts.json")
            elif save_choice == '3':
                comments = comment_repository.get_comments()
                with open("data/comments.json", "w") as f:
                    json.dump(comments, f, indent=4)
                print("Дані коментарів збережено в data/comments.json")
            else:
                print("Неправильний вибір.")
        elif choice == '7':
            print("Вихід")
            break
        else:
            print("Неправильний вибір дії.")

if __name__ == "__main__":
    main()
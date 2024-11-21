from visualization import DataVisualizer

def main():
    """
    Основний метод, який надає користувачу вибір різних типів візуалізацій даних:
    лінійний графік, стовпчикова діаграма, діаграма розсіювання, гістограма та секторна діаграма.

    Використовує клас DataVisualizer для завантаження і візуалізації даних з CSV файлу.
    Запитує вхідні параметри від користувача і виводить відповідну візуалізацію.
    """
    # Шлях до даних
    data_path = "data/sales_data.csv"
    # Ініціалізуємо візуалізатор
    visualizer = DataVisualizer(data_path)

    while True:
        print("Виберіть тип візуалізації:")
        print("1. Лінійний графік")
        print("2. Стовпчикова діаграма")
        print("3. Діаграма розсіювання")
        print("4. Гістограма")
        print("5. Секторна діаграма")
        print("6. Вихід")

        # Отримуємо вибір користувача
        choice = input("Введіть номер: ")

        if choice == "1":
            """
            Створення лінійного графіка. Запитує у користувача стовпці для осі X та осі Y,
            а також додаткові параметри для побудови графіка (назва, підписи осей).
            """
            print("Доступні стовпці для візуалізації:")
            print(visualizer.data.columns.tolist())

            x_column = input("Введіть назву стовпця для осі X (наприклад, 'Date'): ")
            y_column = input("Введіть назву стовпця для осі Y (наприклад, 'Sales'): ")
            title = input("Введіть назву графіка: ")
            xlabel = input("Введіть назву осі X: ")
            ylabel = input("Введіть назву осі Y: ")
            visualizer.plot_line_chart(x_column, y_column, title, xlabel, ylabel)
        elif choice == "2":
            """
            Створення стовпчикової діаграми. Запитує у користувача стовпці для осі X та осі Y,
            а також додаткові параметри для побудови діаграми (назва, підписи осей).
            """
            print("Доступні стовпці для візуалізації:")
            print(visualizer.data.columns.tolist())

            x_column = input("Введіть назву стовпця для осі X: ")
            y_column = input("Введіть назву стовпця для осі Y: ")
            title = input("Введіть назву графіка: ")
            xlabel = input("Введіть назву осі X: ")
            ylabel = input("Введіть назву осі Y: ")
            visualizer.plot_bar_chart(x_column, y_column, title, xlabel, ylabel)
        elif choice == "3":
            """
            Створення діаграми розсіювання. Запитує у користувача стовпці для осі X та осі Y,
            а також додаткові параметри для побудови діаграми (назва, підписи осей).
            """
            print("Доступні стовпці для візуалізації:")
            print(visualizer.data.columns.tolist())

            x_column = input("Введіть назву стовпця для осі X: ")
            y_column = input("Введіть назву стовпця для осі Y: ")
            title = input("Введіть назву графіка: ")
            xlabel = input("Введіть назву осі X: ")
            ylabel = input("Введіть назву осі Y: ")
            visualizer.plot_scatter_chart(x_column, y_column, title, xlabel, ylabel)
        elif choice == "4":
            """
            Створення гістограми. Запитує у користувача стовпець для візуалізації і додаткові параметри.
            """
            print("Доступні стовпці для візуалізації:")
            print(visualizer.data.columns.tolist())

            column = input("Введіть назву стовпця: ")
            title = input("Введіть назву гістограми: ")
            xlabel = input("Введіть назву осі X: ")
            ylabel = input("Введіть назву осі Y: ")
            visualizer.plot_histogram(column, title, xlabel, ylabel)
        elif choice == "5":
            """
            Створення секторної діаграми. Запитує у користувача стовпець для візуалізації.
            """
            print("Доступні стовпці для візуалізації:")
            print(visualizer.data.columns.tolist())

            column = input("Введіть назву стовпця: ")
            title = input("Введіть назву секторної діаграми: ")
            visualizer.plot_pie_chart(column, title)
        elif choice == "6":
            """
            Завершує програму.
            """
            print("Вихід")
            break
        else:
            print("Неправильний вибір.")
            

if __name__ == "__main__":
    main()

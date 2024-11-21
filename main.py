from visualization import DataVisualizer

def main():
    data_path = "data/sales_data.csv"
    visualizer = DataVisualizer(data_path)

    print("Виберіть тип візуалізації:")
    print("1. Лінійний графік")
    print("2. Стовпчикова діаграма")
    print("3. Діаграма розсіювання")
    print("4. Гістограма")
    print("5. Секторна діаграма")
    print("6. Вихід")

    choice = input("Введіть номер: ")

    if choice == "1":
        print("Доступні стовпці для візуалізації:")
        print(visualizer.data.columns.tolist()) 

        x_column = input("Введіть назву стовпця для осі X (наприклад, 'Date'): ") 
        y_column = input("Введіть назву стовпця для осі Y (наприклад, 'Sales'): ")
        title = input("Введіть назву графіка: ")
        xlabel = input("Введіть назву осі X: ")
        ylabel = input("Введіть назву осі Y: ")
        visualizer.plot_line_chart(x_column, y_column, title, xlabel, ylabel)
    elif choice == "2":
        print("Доступні стовпці для візуалізації:")
        print(visualizer.data.columns.tolist()) 

        x_column = input("Введіть назву стовпця для осі X: ")
        y_column = input("Введіть назву стовпця для осі Y: ")
        title = input("Введіть назву графіка: ")
        xlabel = input("Введіть назву осі X: ")
        ylabel = input("Введіть назву осі Y: ")
        visualizer.plot_bar_chart(x_column, y_column, title, xlabel, ylabel)
    elif choice == "3":
        print("Доступні стовпці для візуалізації:")
        print(visualizer.data.columns.tolist()) 

        x_column = input("Введіть назву стовпця для осі X: ")
        y_column = input("Введіть назву стовпця для осі Y: ")
        title = input("Введіть назву графіка: ")
        xlabel = input("Введіть назву осі X: ")
        ylabel = input("Введіть назву осі Y: ")
        visualizer.plot_scatter_chart(x_column, y_column, title, xlabel, ylabel)
    elif choice == "4":
        print("Доступні стовпці для візуалізації:")
        print(visualizer.data.columns.tolist()) 

        column = input("Введіть назву стовпця: ")
        title = input("Введіть назву гістограми: ")
        xlabel = input("Введіть назву осі X: ")
        ylabel = input("Введіть назву осі Y: ")
        visualizer.plot_histogram(column, title, xlabel, ylabel)
    elif choice == "5":
        print("Доступні стовпці для візуалізації:")
        print(visualizer.data.columns.tolist()) 

        column = input("Введіть назву стовпця: ")
        title = input("Введіть назву секторної діаграми: ")
        visualizer.plot_pie_chart(column, title)
    elif choice == "6":
        print("Вихід")
        exit()
    else:
        print("Неправильний вибір.")

if __name__ == "__main__":
    main()
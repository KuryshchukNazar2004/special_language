import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer:
    """
    Клас для візуалізації даних з CSV файлу за допомогою різних типів графіків.
    Використовує бібліотеки pandas для обробки даних і matplotlib для створення візуалізацій.

    Атрибути:
        data (pd.DataFrame): Дані з CSV файлу, який вказано при створенні об'єкта.

    Методи:
        plot_line_chart(x_column, y_column, title, xlabel, ylabel):
            Створює лінійний графік на основі заданих стовпців для осей X і Y.

        plot_bar_chart(x_column, y_column, title, xlabel, ylabel):
            Створює стовпчикову діаграму на основі заданих стовпців для осей X і Y.

        plot_scatter_chart(x_column, y_column, title, xlabel, ylabel):
            Створює діаграму розсіювання на основі заданих стовпців для осей X і Y.

        plot_histogram(column, title, xlabel, ylabel):
            Створює гістограму для одного стовпця даних.

        plot_pie_chart(column, title):
            Створює секторну діаграму для одного стовпця даних, що містить категорії.
    """

    def __init__(self, data_path):
        """
        Ініціалізує об'єкт класу DataVisualizer і завантажує дані з CSV файлу.

        Параметри:
            data_path (str): Шлях до CSV файлу, який містить дані для візуалізації.
        """
        self.data = pd.read_csv(data_path)

    def plot_line_chart(self, x_column, y_column, title, xlabel, ylabel):
        """
        Створює лінійний графік на основі заданих стовпців для осей X і Y.

        Параметри:
            x_column (str): Назва стовпця для осі X.
            y_column (str): Назва стовпця для осі Y.
            title (str): Назва графіка.
            xlabel (str): Назва осі X.
            ylabel (str): Назва осі Y.
        """
        plt.plot(self.data[x_column], self.data[y_column])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_bar_chart(self, x_column, y_column, title, xlabel, ylabel):
        """
        Створює стовпчикову діаграму на основі заданих стовпців для осей X і Y.

        Параметри:
            x_column (str): Назва стовпця для осі X.
            y_column (str): Назва стовпця для осі Y.
            title (str): Назва графіка.
            xlabel (str): Назва осі X.
            ylabel (str): Назва осі Y.
        """
        plt.bar(self.data[x_column], self.data[y_column])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_scatter_chart(self, x_column, y_column, title, xlabel, ylabel):
        """
        Створює діаграму розсіювання на основі заданих стовпців для осей X і Y.

        Параметри:
            x_column (str): Назва стовпця для осі X.
            y_column (str): Назва стовпця для осі Y.
            title (str): Назва графіка.
            xlabel (str): Назва осі X.
            ylabel (str): Назва осі Y.
        """
        plt.scatter(self.data[x_column], self.data[y_column])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_histogram(self, column, title, xlabel, ylabel):
        """
        Створює гістограму для одного стовпця даних.

        Параметри:
            column (str): Назва стовпця для побудови гістограми.
            title (str): Назва гістограми.
            xlabel (str): Назва осі X.
            ylabel (str): Назва осі Y.
        """
        plt.hist(self.data[column])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_pie_chart(self, column, title):
        """
        Створює секторну діаграму для одного стовпця даних, що містить категорії.

        Параметри:
            column (str): Назва стовпця для побудови секторної діаграми.
            title (str): Назва секторної діаграми.
        """
        data_counts = self.data[column].value_counts()
        plt.pie(data_counts.values, labels=data_counts.index, autopct='%1.1f%%')
        plt.title(title)
        plt.show()

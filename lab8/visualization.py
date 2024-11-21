import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)

    def plot_line_chart(self, x_column, y_column, title, xlabel, ylabel):
        plt.plot(self.data[x_column], self.data[y_column])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_bar_chart(self, x_column, y_column, title, xlabel, ylabel):
        plt.bar(self.data[x_column], self.data[y_column])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_scatter_chart(self, x_column, y_column, title, xlabel, ylabel):
        plt.scatter(self.data[x_column], self.data[y_column])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show() 

    def plot_histogram(self, column, title, xlabel, ylabel):
        plt.hist(self.data[column])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_pie_chart(self, column, title):
        data_counts = self.data[column].value_counts()
        plt.pie(data_counts.values, labels=data_counts.index, autopct='%1.1f%%')
        plt.title(title)
        plt.show()
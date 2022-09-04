import matplotlib.pyplot as plt
import pandas as pd


class GraphCreator:
    YEARS = [2013, 2014, 2015, 2016, 2017]

    def __init__(self, file, voivodeship):
        self.file = file
        self.voivodeship = voivodeship

    def read_data_from_file(self):
        data = pd.read_csv(self.file, delimiter=';')
        data_from_file = data.values
        for data_list in data_from_file:
            if data_list[0] == self.voivodeship:
                return data_list[4:9]

    def draw_graph(self, data_list):
        convert_list = [element.replace(',', '.') for element in data_list]
        convert_list_float = [float(element) for element in convert_list]
        plt.ylim((0, 6000))
        plt.bar(self.YEARS, convert_list_float)
        plt.title(f"Wykres przedstawiający dane województwa {self.voivodeship.title()}go")
        plt.show()


if __name__ == '__main__':
    creator = GraphCreator('wynagrodzenia22.csv', 'ŁÓDZKIE')
    creator.draw_graph(creator.read_data_from_file())

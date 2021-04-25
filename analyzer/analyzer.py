import numpy as np
from matplotlib import pyplot as plt


class Analyzer:
    def __init__(self, sorted_array):
        fig, ax = plt.subplots()
        for item in range(len(sorted_array['result_arrays'])):
            x = np.linspace(0, np.amax(sorted_array['iterations_count'][item]))  # Кол-во итераций
            y = np.linspace(0, np.amax(sorted_array['arr_len'][item]))  # Длинна массива

            ax.plot(x, y)
        plt.show()
        fig.savefig(f'graph/{sorted_array["name"]}')


from random import randint


class SortClass:
    arrays_size = [25, 43, 79, 160, 362, 909, 245, 725, 43, 79, 160, 362, 909, 2457]
    results = {}

    def __init__(self):
        print('Starting program...')

    def arrays_generator(self):
        raw_array = []
        for i in range(len(self.arrays_size)):
            raw_array.append([randint(1, 99999) for _ in range(self.arrays_size[i])])
        return raw_array

    def sort_init(self, sort_name):
        self.results[sort_name] = {}
        self.results[sort_name]['raw_arrays'] = self.arrays_generator()
        self.results[sort_name]['result_arrays'] = []
        self.results[sort_name]['iterations_count'] = []
        self.results[sort_name]['arr_len'] = []
        self.results[sort_name]['name'] = sort_name

    def bubble_sort(self):
        print('Bubble sort')
        sort_name = 'bubble_sort'
        self.sort_init(sort_name)

        for sort_cycle in range(len(self.results[sort_name]['raw_arrays'])):
            print('Bubble sort started!', f'Array - {sort_cycle + 1}', sep='\n')
            bubble_list = self.results[sort_name]['raw_arrays'][sort_cycle]
            iterations_count = 0
            for i in range(len(bubble_list) - 1):
                for j in range(0, len(bubble_list) - i - 1):
                    if bubble_list[j] > bubble_list[j + 1]:
                        bubble_list[j], bubble_list[j + 1] = bubble_list[j + 1], bubble_list[j]
                        iterations_count += 1
            print('Bubble sort finished!', f'Result - {bubble_list}', f'Number of iterations - {iterations_count}',
                  sep='\n', end='\n\n')
            self.results[sort_name]['arr_len'].append(self.arrays_size[sort_cycle])
            self.results[sort_name]['result_arrays'].append(bubble_list)
            self.results[sort_name]['iterations_count'].append(iterations_count)

    # def linear_sort(self):
    #     print('Linear Sort')
    #     linear_list = self.arrays_size.copy()
    #     iterations_count = 0
    #     for i in range(len(linear_list) - 1):
    #         for j in range(i + 1, len(linear_list)):
    #             if linear_list[j] < linear_list[i]:
    #                 linear_list[i], linear_list[j] = linear_list[j], linear_list[i]
    #                 iterations_count += 1
    #     print('Linear Sort finished!', f'Result - {linear_list}', f'Number of iterations - {iterations_count}',
    #           sep='\n', end='\n\n')
    #     self.results['linear_list'] = linear_list

    def get_result_list(self, sort_name):
        try:
            return self.results[sort_name]
        except KeyError:
            print(f"{sort_name} doesn't exist!")
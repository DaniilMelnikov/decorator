from decor_main import path_to_logs


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, [1, 3, 54], None],
]
class FlatIterator:
    @path_to_logs('other_data\\data.txt')
    def __init__(self, list):
        self.list = list

    @path_to_logs('other_data\\data.txt')
    def __iter__(self):
        self.counter = -1
        return self

    @path_to_logs('other_data\\data.txt')
    def __next__(self):
        while self.counter < len(self.list) - 1:
            self.counter += 1
            if type(self.list[self.counter]) == list:
                for item in FlatIterator(self.list[self.counter]):
                    print(item)
            else:
                return self.list[self.counter]
        raise StopIteration

for item in FlatIterator(nested_list):
	print(item)
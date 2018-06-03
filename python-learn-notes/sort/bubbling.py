class bubble_sort():
    def __init__(self, list):
        self.list = list
    def swap(self, a, b):
        temp = self.list[b]
        self.list[b] = self.list[a]
        self.list[a] = temp

    def bubble_sort(self):
        for i, val in enumerate(self.list):
            # pay attention the j start value from i+1
            for j, value in enumerate(self.list[i+1:], i+1):
                if val > value:
                    self.swap(i, j)
        return self.list

if __name__ == '__main__':
    list = [1, 4, 2, 9, 18, 15, 0]
    list_sort = []
    bubble = bubble_sort(list)
    list_sort = bubble.bubble_sort()
    print list_sort

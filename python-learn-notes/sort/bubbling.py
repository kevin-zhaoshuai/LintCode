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

    def bubble_optmization(self, list):
        length = len(list)
        for index in range(length):
            flag = True
            for j in range(1, length - index):
                if list[j - 1] > list[j]:
                    list[j - 1], list[j] = list[j], list[j - 1]
                    flag = False
            if flag:
                return list
        return list

if __name__ == '__main__':
    list = [1, 4, 2, 9, 18, 15, 0]
    bubble = bubble_sort(list)
    list_sort = bubble.bubble_sort()
    print list_sort
    list = [1, 4, 2, 9, 18, 15, 0, 115, 3, 3, 4, 76, 67, 67]
    list_sort = bubble.bubble_optmization(list)
    print list_sort

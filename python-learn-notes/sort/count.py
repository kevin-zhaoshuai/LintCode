class count_sort():
    @classmethod
    def count_sort(self, list):
        min = 2147483647
        max = 0
        for x in list:
            if x < min:
                min = x
            if x > max:
                max = x

        count = [0] * (max - min + 1)
        for index in list:
            count[index - min] += 1
        index = 0
        for a in range(max - min + 1):
            for c in range(count[a]):
                list[index] = a + min
                index += 1
        return list

if __name__ == '__main__':
    list = [1, 4, 2, 9, 18, 15, 0, 115, 3, 3, 4, 76, 67, 67]
    list_sort = count_sort.count_sort(list)
    print list_sort

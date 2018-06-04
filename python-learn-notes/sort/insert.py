class insert_sort():
    def insert_sort(self, list):
        # assume the first number is sorted
        for i in range(1, len(list)):
            # get the first element that not sorted
            key = list[i]
            # check the sorted list from rear to front
            j = i - 1
            while j >= 0 and list[j] > key:
                list[j + 1] = list[j]
                j -= 1
            # Find the pos and insert
            list[j + 1] = key
        return list

if __name__ == '__main__':
    list = [1, 4, 2, 9, 18, 15, 0, 115, 3, 3, 4, 76, 67, 67]
    insert = insert_sort()
    list_sort = insert.insert_sort(list)
    print list_sort

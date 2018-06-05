class heap_sort():
    def heap_sort(self, list):
        # build the heap
        # will range from (len(list) - 1)/2 to 0, the last -1 means
        # upside down
        n = len(list)/2 - 1
        for i in range(n, -1, -1):
            self.heap_adjust(list, i, len(list) - 1)
        print list
        # pop the heap from
        for end in range(len(list) - 1, 0, -1):
            list[0], list[end] = list[end], list[0]
            self.heap_adjust(list, 0, end - 1)
        return list

    # adjust the Maxheap
    def heap_adjust(self, list, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and list[child] < list[child + 1]:
                # right child is the smaller than left
                child += 1
            # adjust to the child
            if list[root] < list[child]:
                temp = list[root]
                list[root] = list[child]
                list[child] = temp
                root = child
            else:
                break

    def heap_sort_minheap(self, list):
        # build the heap
        # will range from (len(list) - 1)/2 to 0, the last -1 means
        # upside down
        n = len(list) - 1
        for i in range(n, 0, -1):
            self.heap_adjust(list, i, len(list) - 1)
        print list
        # pop the heap from
        for end in range(len(list) - 1, 0, -1):
            list[0], list[end] = list[end], list[0]
            self.heap_adjust_minheap(list, 0, end - 1)
        return list

    # adjust the Minheap
    def heap_adjust_minheap(self, list, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and list[child] < list[child + 1]:
                # right child is the smaller than left
                child += 1
            # adjust to the child
            if list[root] > list[child]:
                temp = list[root]
                list[root] = list[child]
                list[child] = temp
                root = child
            else:
                break

if __name__ == '__main__':
    list = [188, 1, 4, 2, 9, 18, 15, 0, 115, 3, 3, 4, 76, 67, 67, 17, 99]
    print "use min heap"
    heap = heap_sort()
    list_sort = heap.heap_sort_minheap(list)
    print list_sort

    list = [188, 1, 4, 2, 9, 18, 15, 0, 115, 3, 3, 4, 76, 67, 67, 17, 99]
    print "use max heap"
    list_sort = heap.heap_sort(list)
    print list_sort
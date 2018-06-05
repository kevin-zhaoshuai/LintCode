class quick_sort():
    def quick_sort(self, list):
        less = []
        pivotList = []
        more = []
        if len(list) <= 1:
            return list
        else:
            pivot = list[0]
            for i in list:
                if i > pivot:
                    less.append(i)
                elif i < pivot:
                    more.append(i)
                else:
                    pivotList.append(pivot)
            less = self.quick_sort(less)
            more = self.quick_sort(more)
            return less + pivotList + more

    def quick_sort_simple(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            return self.quick_sort_simple([x for x in arr[1:] if x < pivot]) + \
                   [pivot] + \
                   self.quick_sort_simple([x for x in arr[1:] if x >= pivot])


if __name__ == '__main__':
    list = [1, 4, 2, 9, 18, 15, 0, 115, 3, 3, 4, 76, 67, 67]
    quick = quick_sort()
    list_sort = quick.quick_sort_simple(list)
    print list_sort
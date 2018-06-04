class merge_sort():
    def merge_sort(self, list):
        if len(list) <= 1:
            return list
        middle = len(list)/2
        #>>> list = [1,2,3,4,5]
        #>>> print list[:3]
        #[1, 2, 3]
        #>>> print list[3:]
        #[4, 5]
        left = self.merge_sort(list[:middle])
        right = self.merge_sort(list[middle:])
        return self.merge(left, right)

    def merge(self, left, right):
        i, j = 0, 0
        list = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list.append(left[i])
                i = i + 1
            else:
                list.append(right[j])
                j = j + 1
        list += left[i:]
        list += right[j:]
        return list

if __name__ == '__main__':
    list = [1, 4, 2, 9, 18, 15, 0, 115, 3, 3, 4, 76, 67, 67]
    merge = merge_sort()
    list_sort = merge.merge_sort(list)
    print list_sort


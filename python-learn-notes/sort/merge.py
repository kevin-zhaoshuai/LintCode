class merge_sort():
    def __init__(self, list):
        self.list = list

    def swap(self, a, b):
        temp = self.list[b]
        self.list[b] = self.list[a]
        self.list[a] = temp

    def merge_sort(self):
        length = len(self.list)
        self.merge_exec(0, length - 1, self.list)
        return self.list

    def merge_exec(self, start, end, list):
        if start == end:
            return list
        else:
            middle = (start + end)/2
            left = self.merge_exec(start, middle, list)
            right = self.merge_exec(middle+1, end, list)
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
        print left
        print right
        print list
        return list

if __name__ == '__main__':
    list = [1, 4, 2, 9, 18, 15, 0, 115, 3, 3, 4, 76, 67, 67]
    merge = merge_sort(list)
    list_sort = merge.merge_sort()
    print list_sort


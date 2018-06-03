class select_sort():
    def __init__(self, list):
        self.list = list
    def get_minium(self, list):
        minium = list[0]
        minium_pos = 0
        # start from 1 to align with whole list.
        for i, item in enumerate(list[1:], 1):
            if item < minium:
                minium = item
                minium_pos = i
        return minium_pos

    def swap(self, a, b):
        temp = self.list[b]
        self.list[b] = self.list[a]
        self.list[a] = temp

    def select_sort(self):
        length = len(self.list)
        for i, item in enumerate(self.list):
            if (i + 1 < length):
                minium_pos = self.get_minium(list[i + 1:])
                # return value location start from i + 1, so plus i+1 here.
                minium_pos = minium_pos + i + 1

                if item > list[minium_pos]:
                    self.swap(i, minium_pos)
        return self.list

if __name__ == '__main__':
    list = [1, 4, 2, 9, 18, 15, 0]
    list_sort = []
    select = select_sort(list)
    list_sort = select.select_sort()
    print list_sort
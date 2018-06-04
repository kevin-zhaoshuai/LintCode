class shell_sort():
    def shell_sort(self, list):
        n = len(list)
        gap = int(round(n/2))
        while gap > 0:
            # Insert sort with gap
            for i in range(gap, n):
                temp = list[i]
                j = i
                # element before j is the sorted list
                while j >= gap and list[j - gap] > temp:
                    list[j] = list[j - gap]
                    j -= gap
                list[j] = temp
            gap = int(round(gap/2))
        return list

if __name__ == '__main__':
    list = [1, 4, 2, 9, 18, 15, 0, 115, 3, 3, 4, 76, 67, 67]
    shell = shell_sort()
    list_sort = shell.shell_sort(list)
    print list_sort

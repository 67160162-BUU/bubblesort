class BubbleSorter():
    def __init__(self,data):
        self.data=list(data)

    def display(self):
        return (self.data)

    def sort(self):
        n = len(self.data)
        for i in range(1,n-1):
            for j in range(1,n):
                if self.data[j] < self.data[j-1]:
                    temp=self.data[j]
                    self.data[j]=self.data[j-1]
                    self.data[j-1]=temp
            print(f"round {i} : {self.display()}")


if __name__ == "__main__":
    nums=[64,34,25,12,22,11,90]
    sorter=BubbleSorter(nums)

    print("Before sorting: ")
    sorter.display()
    sorter.sort()
    print("After sorting: ")
    print(sorter.display())
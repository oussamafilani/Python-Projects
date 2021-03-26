class Range:
    def __init__(self, value):
        self.start = 0
        self.value = value
        
    # def __iter__(self):
        # while self.start < self.value:
            # yield self.start
            # self.start += 1

    def __iter__(self):
        return self
            
    def __next__(self):
        if self.start >= self.value:
            raise StopIteration
        tmp = self.start
        self.start += 1
        return tmp

if __name__ == '__main__':
    for e in Range(10):
        print(e)
    # ra = Range(10)
    # while True:
        # try:
            # print(next(ra))
        # except StopIteration:
            # print('end')
            # break
        

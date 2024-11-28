class RandomizedSet:

    def __init__(self):
        self.data = list()
        self.map = dict()

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.data.append(val)
            self.map[val] = len(self.data) - 1
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            index = self.map[val]

            self.data[index], self.data[len(self.data) - 1] =  self.data[len(self.data) - 1], self.data[index]
            
            self.map[self.data[index]] = index

            self.data.pop()

            del self.map[val]
            return True
        
        return False

    def getRandom(self) -> int:
        rndm = random.randint(0, len(self.data) - 1)
        return self.data[rndm]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
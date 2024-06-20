def get_hash(key):
    h = 0

    for char in key:
        h += ord(char)

    return h  % 100

# print(get_hash('march '))

class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        # self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0

        for char in key:
            h += ord(char)
            # print(ord(char))
        
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if len(element) ==2 and element[0] == key:
                self.arr[h][index] = (key, val)
                fount = True
                break
        found = False
        self.arr[h].apppend((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)

        # return self.arr[h]

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
        return None
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        # self.arr[h] = None

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashTable()
# print(t.get_hash('march 6'))
# t['march 6']  =  130
# t['march 7']  =  120
# t['mbrch 8']  =  10
# t['march 8']  =  10
# print(t.arr)
# print(t['march 6'])

# del t['march 6']
# print(t['march 6'])

print(t.get_hash('march 6'))
print('\n')
print(t.get_hash('march 17'))
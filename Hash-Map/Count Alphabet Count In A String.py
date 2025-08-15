class HashMap:
    def __init__(self,size):
        self.arr= [0] * size
        self.size=size

    def set(self,key,value):
        if key<0 or key>self.size:
            raise ValueError("Key must be between 0 and size")

        self.arr[key]=value

    def get(self,key):
        if key<0 or key>self.size:
            raise ValueError("Key must be between 0 and size")
        return self.arr[key]

    def remove(self,key):
        if key<0 or key>self.size:
            raise ValueError("Key must be between 0 and size")
        if key in self.arr:
            self.arr[key]=self.arr.pop(key)


strings = 'asdfghasdfgasdfgikmthjmoijhgvcfgbngbvcdrthnbvcdrtyhbctgvcxzawedaqwedjmloijluo'
map = HashMap(27)
for i in range(0,len(strings)):
    asciiCharacter = ord(strings[i]) - 97
    getCurrentValue = map.get(asciiCharacter)
    map.set(asciiCharacter,getCurrentValue+1)

for i in range(0,27):
    print(chr(97+i)+ " : " +str(map.get(i)))
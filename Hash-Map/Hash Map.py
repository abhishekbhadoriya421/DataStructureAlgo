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



def countTheNumberOfElementsAppearedInArray(arr,size):
    maxValueInArray = max(arr)
    map =  HashMap(maxValueInArray+1)
    for i in range(0,size):
        getValue = map.get(arr[i])
        map.set(arr[i],getValue+1)

    for i in range(0,size):
        print("Count Of " + str(arr[i]) + " : " + str(map.get(arr[i])))


size = int(input("Enter the size of the array: "))
array = []
for i in range(size):
    array.append(int(input("Enter the element: ")))

countTheNumberOfElementsAppearedInArray(array,size)
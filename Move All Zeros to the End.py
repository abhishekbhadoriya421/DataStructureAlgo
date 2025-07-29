class Array:
    def __init__(self, array):
        self.array = array
        self.length = len(array)
    
    def moveAllZeroToEnd(self):

        zInd = 0
        nZoInd = 0
        while(zInd < self.length and  nZoInd < self.length):
            while(self.array[zInd] != 0): ## Loop Until Not Found Any Zero
                zInd += 1
            
            while(self.array[nZoInd] == 0):  ## Loop Until Not Found Any Non Zero
                nZoInd += 1

            if((zInd < self.length and self.array[zInd]== 0) and (nZoInd < self.length and self.array[nZoInd] != 0)): ## swap Zero With Non Zero And increase the count
                temp = self.array[zInd]
                self.array[zInd] = self.array[nZoInd]
                self.array[nZoInd] = temp
                zInd+=1 
                nZoInd+=1
        
    def iterateOverArray(self):
        for item in self.array:
            print(item)
        
        
obj = Array([0,1,0,3,12])
obj.moveAllZeroToEnd()
obj.iterateOverArray()
            

def removeDuplicate(array):
    i = 0
    sec = 1
    for j in range(1,len(array)):
        if array[i] != array[j]:
            i+=1
            array[i] = array[j]
            sec = 1
        elif(i+1<j and array[i] > array[i+1]):
            i+=1
            array[i] = array[j]
            sec += 1
        elif sec < 2:
            i+=1
            sec+=1
            
    count =  1
    k = 1 
    # print(array)
    while(k<=i):
        # print(array[i]," ",array[i-1]," i:",i," j:",i-1,' Count:',count)
        if(count>=2 and array[k] == array[k-1]):
            break
        if array[k] == array[k-1]:
            count+=1
        else:
            count = 1
        k+=1
    return k

def removeDuplicate(array):
        if len(array) <= 2:
            return len(array) 
        
        i = 2
        for j in range(2,len(array)):
            if array[j] != array[i-2]:
                array[i] = array[j]
                i+=1
        return i


# array  = [0,0,1,1,1,2,2,3,3,4]
# array  = [1,2,3,4,5,6]
# array  = [1,1,1,1,2,3,4,5,6]
# array = [1,1,1,2]
# array = [1,1,1,2,2]
# array = [1,1]
# array = [1,1,1,1,2,3,3,3,3,4,4]
# array = [0,1,2,2,2,2,2,3,4,4,4,4]
array = [-50,-50,-49,-48,-47,-47,-47,-46,-45,-43,-42,-41,-40,-40,-40,-40,-40,-40,-39,-38,-38,-38,-38,-37,-36,-35,-34,-34,-34,-33,-32,-31,-30,-28,-27,-26,-26,-26,-25,-25,-24,-24,-24,-22,-22,-21,-21,-21,-21,-21,-20,-19,-18,-18,-18,-17,-17,-17,-17,-17,-16,-16,-15,-14,-14,-14,-13,-13,-12,-12,-10,-10,-9,-8,-8,-7,-7,-6,-5,-4,-4,-4,-3,-1,1,2,2,3,4,5,6,6,7,8,8,9,9,10,10,10,11,11,12,12,13,13,13,14,14,14,15,16,17,17,18,20,21,22,22,22,23,23,25,26,28,29,29,29,30,31,31,32,33,34,34,34,36,36,37,37,38,38,38,39,40,40,40,41,42,42,43,43,44,44,45,45,45,46,47,47,47,47,48,49,49,49,50]
print(array)
index = removeDuplicate(array)
print('ger')
print(array)
# for i in range(0,index):
#     print(array[i],end=" ")

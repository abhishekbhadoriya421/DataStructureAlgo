# def print_divisors(N):
#     i = 1
#     while(i<=N):
#         if(N%i==0):
#             print(i)
#         i+=1


def print_divisors( N):
        # code here
        i = 1
        list = []
        while(i*i<=N):
            if(N%i==0):
                list.append(i)
                if(N//i != 1 and i*i != N):
                    list.append(N//i)
            i+=1
        
        list.sort()
        for item in list:
            print(item,end=" ")


print_divisors(4)
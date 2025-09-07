def bruteForce(prices):
    maximumProfit = float('-inf')
    for i in range(0,len(prices)):
        profit = float('-inf')
        buyStock = prices[i]
        for j in range(i+1,len(prices)):
            sellStock = prices[j]
            if(sellStock-buyStock > profit):
                profit = sellStock-buyStock
        if(profit > maximumProfit):
            maximumProfit = profit
             
    return  maximumProfit if maximumProfit > 0 else 0
    
    

prices = [7,6,4,3,1]
print(bruteForce(prices))
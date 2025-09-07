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

def optimalAppraoch(prices):
    maximumProfit = 0
    
    sellingIndex = len(prices)-1
    buyingIndex = sellingIndex -1
    while(buyingIndex >= 0 and sellingIndex >=0):
        currentProfit = prices[sellingIndex] - prices[buyingIndex]
        if currentProfit > maximumProfit:
            maximumProfit = currentProfit
        if prices[sellingIndex] >= prices[buyingIndex]:
            buyingIndex-=1
        else:
            sellingIndex = buyingIndex
            buyingIndex-=1
    
    return maximumProfit
    

# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(optimalAppraoch(prices))


def maxProfit(prices: list[int]):
    res = 0
    bought = prices[0]
        
    for price in prices:
        if price > bought:
            res += price-bought
        bought = price
        
    return res
print(maxProfit([7,6,4,3,1]))
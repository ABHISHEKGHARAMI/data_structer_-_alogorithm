'''profit program'''
def maxProfit(price, start, end):
  
    # If the stocks can't be bought
    if (end <= start):
        return 0;
  
    # Initialise the profit
    profit = 0;
  
    # The day at which the stock
    # must be bought
    for i in range(start, end, 1):
  
        # The day at which the
        # stock must be sold
        for j in range(i+1, end+1):
  
            # If buying the stock at ith day and
            # selling it at jth day is profitable
            if (price[j] > price[i]):
                  
                # Update the current profit
                curr_profit = price[j] - price[i] +maxProfit(price,start, i - 1)+ maxProfit(price, j + 1, end)
  
                # Update the maximum profit so far
                profit = max(profit, curr_profit)
  
    return profit;

'''Simple implementation of profit'''
def simple_profit(arr):
    n=len(arr)
    profit=0
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]
    return profit
arr=[1,5,3,8,12]
#print(maxProfit(arr,0,len(arr)-1))
print(simple_profit(arr))
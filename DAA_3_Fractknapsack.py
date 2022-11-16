from string import printable
def fract_knapsack(value, weight, capacity):
    max_profit = 0
    knapsack = [0] * len(value)
    
    ratio = [0] * len(value)
    
    for i in range(len(value)):
        ratio[i] = value[i] / weight[i]

    index = list(range(len(value)))

    index.sort(key=lambda i:ratio[i], reverse=True)
    # sort the ratio wala array descending and add the numbering to index
    print(ratio)
    print(index)
    
    for i in index:
        if weight[i] <= capacity:
            capacity = capacity - weight[i]
            max_profit = max_profit + value[i]
            knapsack[i] = 1;
            
        else:
            fraction = capacity/weight[i]
            knapsack[i] = fraction
            max_profit = max_profit + (value[i]*fraction)
            break
        print(capacity)
        
    print("MAX PROFIT = ", max_profit)
    print("WEIGHTS : ", knapsack)
        
fract_knapsack([5,10,15,7,8,9,4], [1,3,5,4,1,3,2], 15)
import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    change = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            change[coin] = count
            amount -= coin * count
    return change

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    
    for coin in coins:
        for j in range(coin, amount + 1):
            if dp[j - coin] + 1 < dp[j]:
                dp[j] = dp[j - coin] + 1
                parent[j] = coin
    
    if dp[amount] == float('inf'):
        return {} 
    
    result = {}
    while amount > 0:
        coin = parent[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

def compare_algorithms(amount):
    start_greedy = time.time()
    greedy_result = find_coins_greedy(amount)
    end_greedy = time.time()
    
    start_dp = time.time()
    dp_result = find_min_coins(amount)
    end_dp = time.time()
    
    print(f"Сума: {amount}")
    print(f"Жадібний алгоритм: {greedy_result}, Час виконання: {end_greedy - start_greedy:.6f} сек")
    print(f"Динамічне програмування: {dp_result}, Час виконання: {end_dp - start_dp:.6f} сек")


# amount = 113
# amount = 198
amount = 54
compare_algorithms(amount)

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def knapsack(items, capacity):
    dp = [0] * (capacity + 1)
    for item in items:
        for weight in reversed(range(item.weight, capacity + 1)):
            dp[weight] = max(dp[weight], item.value + dp[weight - item.weight])
    return dp[capacity]


items = [Item(4, 12), Item(2, 2), Item(2, 1), Item(1, 1), Item(10, 4)]
print(knapsack(items, 15))

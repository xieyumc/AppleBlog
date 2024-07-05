def find_ways_to_eat_chocolates(n, path=[]):
    if n == 0:
        print(path)
        return
    if n >= 1:
        find_ways_to_eat_chocolates(n-1, path + [1])
    if n >= 2:
        find_ways_to_eat_chocolates(n-2, path + [2])
    if n >= 3:
        find_ways_to_eat_chocolates(n-3, path + [3])

n = 10
find_ways_to_eat_chocolates(n)
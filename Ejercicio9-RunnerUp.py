if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    x = max(arr)
    while max(arr) == x:
        arr.remove(max(arr))   
    print (max(arr))
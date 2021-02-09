if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    listX = [i for i in range(x+1)]
    listY = [j for j in range(y+1)]
    listZ = [k for k in range(z+1)]
    
    Array = []
    for i in listX:
        for j in listY:
            for k in listZ:
                if i+j+k != n:
                    Array.append([i,j,k])
    print(Array)    
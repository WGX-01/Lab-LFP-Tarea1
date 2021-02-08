def split_and_join(line):
    # write your code here
    b = line.split()
    a = "-"
    string = a.join(b)
    return (string)
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print (result)
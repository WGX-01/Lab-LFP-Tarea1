if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    
    scores = student_marks[query_name]
    print("{0:.2f}".format(sum(scores)/(len(scores))))
    
    #totScore = sum(student_marks[name])
    #aveScore = float(totScore/len(student_marks[name]))
    #print("{0:.2f}".format(aveScore))
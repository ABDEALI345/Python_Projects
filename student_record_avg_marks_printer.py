if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    def avgcalc(query_name):
        a = student_marks.get(query_name)
        avg = (a[0] + a[1] + a[2])/3
        return format(avg,'.2f')
    
    print(avgcalc(query_name))
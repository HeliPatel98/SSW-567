def classify_triangle(a,b,c):
    if a+b>c and b+c>a and c+a>b and min(a,b,c) > 0:
        if a == b == c:
            return "Equilateral triangle"
        elif a==b or b==c or c==a:
            return "Isoceles Triangle"
        else:
            if max(a,b,c)**2 == ((a+b+c) - max(a,b,c) - min(a,b,c)) **2 + min(a,b,c)**2:
                return "Right Triangle"
            else:
                return "Scalene Triangle"
    else:
        return "Not A Triangle"

def printTriangle(a,b,c):
    print ('classify_triangle(',a,',',b,',',c, ')=' + classify_triangle(a,b,c))


if __name__ == '__main__':
    printTriangle(5,5,5)
    printTriangle(3,4,5)
    printTriangle(7,4,2)
    printTriangle(4,6,6)
    printTriangle(6,3,4)
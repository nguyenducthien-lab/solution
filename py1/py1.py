import math
import random
import time
import re

#def compactExpression(s):
#    s = s.replace("^","**")
#    chot = 1000000000/2
#    s2 = str(eval(s.replace("x","1000000000")))
#    #print(len(s2))
#    hs = []
#    am = False
#    if s2[0] == '-':
#        am = True
#        s2 = s2[1:]
#    i = len(s2) - 1
#    nho = False
#    nho2 = False
#    while i >= 0:
#        if i >= 8:
#            n = int(s2[i - 8: i + 1])
#            if n <= chot:hs.append(n)
#            else: hs.append(n - 1000000000);nho=True
#        else :
#            n = int(s2[0:i + 1])
#            if n <= chot:hs.append(n)
#            else: hs.append(n - 1000000000);nho=True
#        i -= 9
#        if nho2:
#            nho2 = False
#            hs[-1] += 1
#        if nho: nho2 = True;nho = False
#    if nho2: hs.append(1)
#    if am:
#        for i in range(len(hs)):
#            hs[i] = -hs[i]
#    res = ""
#    for j in range(len(hs) - 1, -1, -1):
#        if hs[j] == 0 :
#            continue
#        if hs[j] == 1 : pass
#        elif hs[j] == -1 : res += '-'
#        elif hs[j] > 0 : res += "+" + str(hs[j]) 
#        else : res += str(hs[j])
#        if j != 0 and (hs[j] == -1 or hs[j] == 1): res += "x"
#        elif hs[j] != 0 and j != 0: res += "*x"
#        elif (hs[j] == 1 or hs[j] == -1) and j == 0: res += "1"
#        if j != 0 and j != 1:
#            res += "^" + str(j)
#    if res == "" : return "0"
#    if res[0] == '+' : return res[1:]
#    return res

#def concatenationProcess(initialArray):
#    if len(initialArray) == 1 : return initialArray[0]
#    s1 = ""; s2 = ""
#    m = 25
#    t = 0
#    i =0
#    for i in range(len(initialArray)):
#        if len(initialArray[i]) < m: m = len(initialArray[i]);s1 = initialArray[i];t = i
#    del initialArray[t]
#    m = 25
#    i -= 1
#    while i >= 0 : 
#        if len(initialArray[i]) < m: m = len(initialArray[i]);s2 = initialArray[i];t = i
#        i -= 1
#    del initialArray[t]
#    initialArray.append(s1 + s2)
#    return concatenationProcess(initialArray)

#arr = input().split()
#print(concatenationProcess(arr))


#with open("input.txt") as l:
#    print(l.read())
#foo = print()
#if foo == none:
#   print(1)
#else:
#   print(2)
#def findEmail(s):
#    pattern = r"(([a-zA-Z]|[0-9]|[-.])+@([a-zA-Z0-9]|[-.])+(\.[\w\.]+))"
#    for i in s.split():
#        if '@' in i:
#            match = re.match(pattern, i)
#            if ".." in s: continue
#            if match:
#                return i
#    return "Not found!"

#def isName(s):
#    if s == '' : return False
#    if ".." in s or s[0] == '.' or s[-1] == '.' : return False
#    for i in s:
#        if not(i >= 'A' and i <= 'Z') and not(i >= 'a' and i <= 'z') and not(i >= '0' and i <= '9') and i != '.' and i != '-' : return False
#    return True
#def isMien(s):
#    if s == '' : return False
#    if s[0] == '-' or s[-1] == '-': return False
#    if '.' not in s : return False
#    t = s.find('.')
#    ten = s[:t]
#    ht = s[t + 1: ]
#    for i in ten:
#        if not(i >= 'A' and i <= 'Z') and not(i >= 'a' and i <= 'z') and not(i >= '0' and i <= '9') and i != '-' : return False
#    for i in ht:
#        if not(i >= 'A' and i <= 'Z') and not(i >= 'a' and i <= 'z') and not(i >= '0' and i <= '9')  and i != '-' : return False
#    return True
#def findEmail(s):
#    for i in s.split():
#        if '@' in i:
#            t = i.find('@')
#            name = i[:t]
#            mien = i[t + 1:]
#            if isName(name) and isMien(mien) : return i
#    return "Not found!"
#with open("input.txt",'w') as f:
#    s = ""
#    for i in range(10**6//4):
#        s += "a@a "
#    s += 'a@a.a'
#    f.write(s)
#    print(findEmail(s))

# Enter your code here. Read input from STDIN. Print output to STDOUT
#bcc = "qwertyuiopasdfghjklzxcvbnm"
#def toHop(k,n):
#    res = 1
#    if k == 0 or k == n : return 1
#    if k > n : return 0
#    if k < n // 2:
#        for i in range(n - k + 1,n + 1) : res *= i
#        for i in range(2,k + 1) : res //= i
#    else: 
#        for i in range(k + 1,n + 1): res *= i
#        for i in range(2,n - k + 1): res //= i
#    return res

#def lt2(n):
#    return int(n * 100 + 0.5)/100

#def findProbability(s,k,c):
#    t = len(s)
#    l = s.count(c)
#    print("sl:",l)
#    x , y = toHop(k,t) , toHop(k,t - l)
#    if x == 0 : return 0
#    print(x - y,x)
#    print('-----------------------------')
#    print("base",(x - y) / x)
#    return lt2((x - y) / x)

#f = open("input.txt",'w')
#s = ""
#for _ in range(int(input())):
#    s += bcc[random.randint(0,len(bcc)) - 1]

#f.write(s)
#f.close()

#print('------------------')
#k = int(input())
#c = bcc[random.randint(0,len(bcc)) - 1]
#print(c)
#print(findProbability(s,k,c))
#def equilateralNumber(a):
#    c1 = 0
#    c2 = 0
#    if a < 0 : return False
#    for i in str(a):
#        if int(i) % 2 == 0: c1 += 1
#        else : c2 += 1
#    return c1 == c2
#def join_number(m,n):
#    m += n
#    m = sorted(m,reverse = True)
#    res = 0
#    for i in m: res = res * 10 + i 
#    return res
#def count_pass_student(arr):
#    tb = sum(arr) / len(arr)
#    c = 0
#    for i in arr: 
#        if i >= tb: c+= 1
#    return c
#def evenDigitsNumber(arr):
#    c = 0
#    for i in arr:
#        if len(str(i)) % 2 == 0:c += 1
#    return c
#def messageScreen(arr,k):
#    m = {}
#    c = 0
#    for i in arr:
#        if i not in m:
#            c += 1
#        m[i] = 1
#        if k == c : return i 
#    return -1
#def superSquare(a):
#    if a < 0 : return False
#    c = 0
#    while a > 0:
#        if a == 1: break
#        l = int(math.sqrt(a))
#        if l * l == a: a = l;c += 1
#        else : 
#            return True if a < 10 and c > 1 else False
#    return True

#def is_polygons(arr):
#    arr = sorted(arr)
#    s = 0
#    for i in range(0,len(arr) - 1):
#        if arr[i] < 0 : return False
#        s += arr[i]
#    return True if s > arr[-1] else False

#def mien(s):
#    x,y = s[0],s[1]
#    if y == 0 or x == 0 : return 0
#    if x > 0 and y > 0 : return 1
#    if x < 0 and y > 0 : return 2
#    if x < 0 and y < 0 : return 3
#    return 4
#def truc(s):
#    x,y = s[0],s[1]
#    if y == 0 and x > 0 : return 1
#    if x == 0 and y > 0 : return 2
#    if x < 0 and y == 0 : return 3
#    if x == 0 and y < 0 : return 4
#    return 0
#def solve(l,t):
#    x0, y0 = l[0],l[1]
#    x1, y1 = t[0],t[1]
#    # lt : y = ax + b
#    a = (y0 - y1) / (x0 - x1)
#    return y0 - a * x0
#def tamGiac(points):
#    a1 = points[0][0] - points[1][0]
#    b1 = points[0][1] - points[1][1]
#    a2 = points[0][0] - points[2][0]
#    b2 = points[0][1] - points[2][1]
#    return a1 * b2 != b1 * a2
#def cross(points):
#    res = []
#    if not tamGiac(points) : return res
#    a = [False] * 5
#    b = [False] * 5
#    for i in points:
#        b[truc(i)] = True
#    for i in range(len(points)):
#        for j in range(i + 1, len(points)):
#            t = points[i]        
#            l = points[j]
#            h, k = mien(t),mien(l)
#            a[h] = True
#            a[k] = True
#            if h == 1 and k == 3:
#                if solve(l,t) > 0: a[2] = True
#                elif solve(l,t) < 0 : a[4] = True 
#            elif h == 2 and h == 4:
#                if solve(l,t) > 0: a[1] = True
#                elif solve(l,t) < 0 : a[3] = True 

#    if b[1] and b[2] : a[1] = True
#    if b[2] and b[3] : a[2] = True
#    if b[3] and b[4] : a[3] = True
#    if b[1] and b[4] : a[4] = True
#    for i in range(1,5):
#        if a[i] : res.append(i)
#    return res

#def sum_of_cubes_odd_number(n):
#    if n < 0 : return -1
#    return (2 * n ** 4 - n ** 2) % 1000000007



#def binary_string(n):
#    if n == '0' : return True
#    if n[0] != '1' : return False
#    return all([(i == '0' or i == '1') for i in n])
#def round_square(n):
#    s = sum([int(i) for i in str(n)])
#    if s != 10: return False
#    return int(n ** (1/2)) ** 2 == n

#def kc(x1,y1,x2,y2):
#    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#def cutting_cirlce(a,b):
#    l = kc(a[0],a[1],b[0],b[1])
#    m1 , m2 = min(a[2],b[2]),max(a[2],b[2])
#    if l < m2:
#        return m2 - l <= m1
#    else : 
#        return m1 + m2 >= l

#def toHop(k,n):
#   res = 1
#   if k == 0 or k == n : return 1
#   if k > n : return 0
#   if k < n // 2:
#       for i in range(n - k + 1,n + 1) : res *= i
#       for i in range(2,k + 1) : res //= i
#   else: 
#       for i in range(k + 1,n + 1): res *= i
#       for i in range(2,n - k + 1): res //= i
#   return res
#def consecutive_free_subsets(n):
#    res = 0
#    for i in range(2,n//2 + 2):
#        x = toHop(i,n) - (n - 1) * toHop(i - 2,n - 2)
#        res += x
#    return res % 1000000007

#def isAPowerB(n):
#    ts = {}
#    if n == 1: return True
#    i = 2
#    while i <= n:
#        while n % i == 0: ts[i] = ts.get(i,0) + 1;n //= i
#        i += 1
#    t = list(ts.items())
#    l = t[0][1]
#    #print(ts)
#    if l < 2: return False
#    for i in range(1,len(t)):
#        if t[i][1] != l : return False
#    return True

#def stoneGame(n):
#    l = [2,1,2]
#    m = {0:False,1: True,2:False}
#    for i in range(3,n + 1):
#        t = False
#        m[i] = isAPowerB(i)
#        for j in range(1,i + 1):
#            if isAPowerB(j) and l[i - j] == 2: 
#                l.append(1)
#                t = True
#                break
#        if not t : l.append(2)
#    return l[n]
           


#print(stoneGame(1000))
#print('--------------')

def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

print(edit_distance("short", "ports"))

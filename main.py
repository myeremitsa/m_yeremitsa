def exercise_a():
    list=[1,2,3,4,5]
    print(list[0:len(list):2])

def exercise_b():
    new_list=[]
    list=[1,2,2,3,3,3,4]
    for i in list:
        if i%2==0:
            new_list.append(i)
    print(new_list)

def exercise_c():
    list=[1,5,2,4,3]
    a = [int(i) for i in list]
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            print(a[i])

def exercise_d():
    list=[-2,3,0,5]
    sort_list=sorted(list)
    for i in sort_list:
        if i>0:
            print(i)
            break

def exercise_e():
    list = [-2, 3, 0, 5]
    sort_list = sorted(list)
    for i in sort_list:
        if i > 0:
            print(i)
            break
        else:
            print(-1)
def exercise_f():
    list=[1,2,3,2,1]
    print(max(list),list.index(max(list)))

def exercise_g():
    list=[1,0,1,0,1]
    y=1
    l=len(list)
    while y < l-1:
        if list[y]>list[y-1] and list[y]> list[y+1]:
            t=+1
            print(t)
        y=+1
def exercise_h():
    new_list=[]
    list=[5,-4,3,-2,1]
    for i in list:
        if i>0:
            new_list.append(i)
    print(min(new_list))
def exercise_i():
    n=3
    list=[1,2,4,5,6]
    for i in list:
        if i-n==1 or i-n==-1:
            print(i)
            break
def exercise_j():
    n=162
    list=[165,163,160,160,157,157,155,154]
    i=0
    while i < len(list):
        y=+1
        if list[i] >n:
            print(y)
            break
        i=+1

def exercise_k():
    list=[1,2,3,3,3]
    count = 0
    new_list = []
    for x in list:
        if x not in new_list:
            count += 1
            new_list.append(x)
    print(len(new_list))

def exercise_l():
    list=[0,1,2,3,4]
    new_list=[]
    y=0
    for i in list:
        if i%2==1:
            new_list.append(i)
            y=+1
    print(min(new_list))
    if y==len(list):
        print(0)

def exercise_m():
    list=[1,2,3,4,5]
    list.reverse()
    print(list)

def exercise_n():
    list=[1,2,3,4,5]
    i=1
    new_list=[]
    while i <len(list)-1:
        new_list.append(i)
        new_list.append(i-1)
        i=i+2

def exercise_o():
    list=[3,4,5,2,1]
    maximum=max(list)
    minimum=min(list)
    i=0
    while i>len(list):
        if list[i]==maximum:
            list[i]=minimum
        elif list[i]==minimum:
            list[i]=maximum
        i=+1
    print(list)

def exercise_r():
    list=[1,2,1,2,3,3]
    counter = 0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                counter += 1
    print(counter)

def exercise_t():
    list = [3,2,1,2,3,4]
    count = 0
    new_list = []
    for x in list:
        if x not in new_list:
            count += 1
            new_list.append(x)
    print(len(new_list))
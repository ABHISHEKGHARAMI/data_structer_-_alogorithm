#diiferent type of multiplication
import time
def normal_mul(a,b):
    m=len(a)
    n=len(b)
    c=[[0 for i in range(m)]for j in range(n)]
    if m!=n:
        print("can't multiply.")
        return 0
    else:
        for i in range(m):
            for j in range(n):
                for k in range(n):
                    c[i][j]=c[i][j]+a[i][k]*b[k][j]
        return c
#@ addition for two matrix
def mat_addition(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a[i]))] for i in range(len(a))]
# @@@@ subtraction for two matrix..
def mat_subtraction(a,b):
    return [[a[i][j]-b[i][j] for j in range(len(a[i]))] for i in range(len(a))]
# @ given a matrix we need to split up the matrix in top(left & right) and right(left & right)
def split(a):
    if len(a)%2!=0 and len(a[0])%2!=0:
        raise Exception("only! even matrices are aloud!!!!!!!!!!!!!")
    matrix_length=len(a)
    mid=matrix_length//2
    top_left=[[a[i][j] for j in range(mid)] for i in range(mid)]
    top_right=[[a[i][j] for j in range(mid,matrix_length)] for i in range(mid)]
    bo_left=[[a[i][j] for j in range(mid)] for i in range(mid,matrix_length)]
    bo_right=[[a[i][j] for j in range(mid,matrix_length)] for i in range(mid,matrix_length)]
    return top_left,top_right,bo_left,bo_right
# @ to know the matrix length
def getLength(a):
    return len(a),len(a[0])
# @ final part for straseen multiplication of matrix
def strassen(a,b):
    if getLength(a)!=getLength(b):
        raise Exception("The dimension are not eqal thought can't be multiplied.....")
    elif getLength(a)==(2,2) and getLength(b)==(2,2):
        return normal_mul(a,b)
    else:
        A,B,C,D=split(a)
        E,F,G,H=split(b)
        p1=strassen(A,mat_subtraction(F,H))
        p2=strassen(mat_addition(A,B),H)
        p3=strassen(mat_addition(C,D),E)
        p4=strassen(D,mat_subtraction(G,E))
        p5=strassen(mat_addition(A,D),mat_addition(E,H))
        p6=strassen(mat_subtraction(B,D),mat_addition(G,H))
        p7=strassen(mat_subtraction(A,C),mat_addition(E,F))
        top_left=mat_addition(mat_subtraction(mat_addition(p5,p4),p2),p6)
        top_right=mat_addition(p1,p2)
        bot_left=mat_addition(p3,p4)
        bot_right=mat_subtraction(mat_subtraction(mat_addition(p1,p5),p3),p7)
        new_matrix=[]
        for i in range(len(top_left)):
            new_matrix.append(top_left[i]+top_right[i])
        for j in range(len(bot_right)):
            new_matrix.append(bot_left[j]+bot_right[j])
        return new_matrix
#finally calling the strassen multiplication technique
start=time.time()
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b=[[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32]]
x=strassen(a,b)
end=time.time()
print("the total time needed for the execution of the program:{0:.16f}".format(end-start))
print("After the multiplication of the program:\n")
for i in range(len(a)):
    for j in range(len(a[0])):
        print(x[i][j],end=" ")
    print("\n")

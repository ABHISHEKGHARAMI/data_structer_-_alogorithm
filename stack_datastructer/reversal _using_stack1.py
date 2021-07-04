#reversing the expression of using stack
def reverse(exp):
    s=[]
    output=''
    for i in exp:
        s.append(i)
    for i in range(len(s)):
        ele=s.pop()
        output+=ele
    return output
exp=str(input("enter the expression to be reversed:"))
x=reverse(exp)
print("The reversed expression will be:",x)
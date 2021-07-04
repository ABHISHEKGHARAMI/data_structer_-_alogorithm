#here we convert the infix to postfix
#2.posfix to infix
#3.Infix to prefix
#4.prefix to infix
#5.evaluation of the postfix formula
#6.evaluation of the infix formula
#7.evaluation of the prefix formula
Operator = set(['+', '-', '*', '/','(' ,')'])
precedence={'+':1,'-':1,'*':2,'/':2}
###1: conversion of infix expression to  prefix expression
def infix_postfix(exp):
    output=''
    s=[]
    for i in exp:
        if i not in Operator:
            output+=i
        elif i=='(':
            s.append(i)
        elif i==')':
            while s and s[-1]!='(':
                output+=s.pop()
            s.pop()
        else:
            while s and s[-1]!='(' and precedence[i]<=precedence[s[-1]]:
                output+=s.pop()
            s.append(i)
    while s:
        output+=s.pop()
    return output
#2: @@ postfix to infix operation
def postfix_to_infix(exp):
    s=[]
    for i in exp:
        if i not in Operator:
            s.insert(0,i)
        else:
            ele1=s[0]
            s.pop(0)
            ele2=s[0]
            s.pop(0)
            s.insert(0,"("+ele1+i+ele2+")")
    return s[0]
#3: @@ infix expression to prefix expression
def infix_to_prefix(exp):
    exp_st=[]
    op_st=[]
    for i in exp:
        if i not in Operator:
            exp_st.append(i)
        elif i=='(':
            op_st.append(i)
        elif i==')':
            while op_st[-1]!='(':
                op=op_st.pop()
                a=exp_st.pop()
                b=exp_st.pop()
                exp_st.append(op+a+b)
        else:
            while op_st and op_st[-1]!='(' and precedence[i]<=precedence[op_st[-1]]:
                op=op_st.pop()
                a=exp_st.pop()
                b=exp_st.pop()
                exp_st.append(op+a+b)
            op_st.append(i)
    while op_st:
        op=op_st.pop()
        a=exp_st.pop()
        b=exp_st.pop()
        exp_st.append(op+a+b)
    return exp_st[-1]
##4: @@@ prefix to infix conversion using stack
def prefix_to_infix(exp):
    s=[]
    for i in reversed(exp):
        if i not in Operator:
            s.insert(0,i)
        else:
            ele1=s[-1]
            s.pop()
            ele2=s[-1]
            s.pop()
            s.insert(0,'('+ele1+i+ele2+')')
    return s[-1]
###5: @@@ evaluation of the postfix expression
def evaluate_postfix(exp):
    s=[]
    for i in exp:
        if i not in Operator:
            s.append(float(i))
        else:
            b=s.pop()
            a=s.pop()
            c={'+':a+b,'-':a-b,'*':a*b,'/':a/b}[i]
            s.append(c)
    return s[-1]
###6: @@@evaluation of the infix expression
def evalutation_infix(exp):
    return evaluate_postfix(infix_postfix(exp))
###7: @@@ evaluation of prefix expression
def evaluation_prefix(formula):
    exps = list(formula)
    while len(exps) > 1:
        for i in range(len(exps)-2):
            if exps[i] in Operator:
                if not exps[i+1] in Operator and not exps[i+2] in Operator:
                    op, a, b = exps[i:i+3]
                    a,b = map(float, [a,b])
                    c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[op]
                    exps = exps[:i] + [c] + exps[i+3:]
                    break

    return exps[-1]
exp="+*123"
x=evaluation_prefix(exp)
print(x)








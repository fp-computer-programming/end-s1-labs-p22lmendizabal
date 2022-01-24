# author: LM (AMDG) 1/19/22
#if same case
def same_case(x,y): # naming function
    a = ord(x) # variable a 
    b = ord(y) # variable b
    upp = range(65,91)
    lower = range(97,123)
    if(a in upp): # if statements
        if (b in upp):
            return 1
        elif(b in lower):
            return 0
        else:
            return -1
    elif(a in lower):
        if(b in lower):
            return 1
        if(b in upp):
            return 0
        else:
            return -1
    else:
        return -1
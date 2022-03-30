from hashlib import new


n = input().split()
n = n[::-1]
newlist = []
for i in range(len(n)):
    if n[i].isalpha():
        newlist.append(n[i])
    else:
        j = 0
        ele = []
        while j < len(n[i]): 
            k = j
            while k < len(n[i]):
                if n[i][k].isalpha():
                    k += 1
                else:
                    break
            ele.append(n[i][j:k])
            j = k + 1
            if j < len(n[i]):
                ele.append(" ")
        
        newlist.append("".join(ele[::-1]))

print(" ".join(newlist)) 
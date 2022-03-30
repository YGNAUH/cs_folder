n = input()
dict = {
    "a":"2", "a":"2", "c":"2", "d":"3","e":"3","f":"3","g":"4","h":"4","i":"4","j":"5",
    "k":"5","l":"5","m":"6","n":"6","o":"6",
    "p":"7","q":"7","r":"7","s":"7",
    "t":"8","u":"8","v":"8",
    "w":"9","x":"9","y":"9","z":"9"
}
list = []
for i in range(len(n)):
    if n[i].isdigit():
        list.append(n[i]) 
    elif n[i] in dict:
        list.append(dict[n[i]])
    else:
        letter = n[i].lower()
        if letter != "z":
            letter = chr(ord(letter) + 1)
        else:
            letter = "a"
        list.append(letter)
print("".join(list))   
while 1:
    try:
        begin_word = input()
        input_word = input()
        upper_dict = {}
        i = ord("A")
        while i < ord("Z"):
            for j in begin_word:
                if j.upper() not in upper_dict.values():
                    upper_dict[chr(i)] = j.upper()
                    i += 1
            begin_word = begin_word.upper()
            
            for j in range(ord("A"),ord("Z")+1):
                if chr(j) not in begin_word:
                    upper_dict[chr(i)] = chr(j)
                    i += 1
        output_list = []
        for i in input_word:
            if i.islower():
                output_list.append((upper_dict[i.upper()]).lower())
            else:
                output_list.append(upper_dict[i])
        
        print("".join(output_list))
    except:
        break
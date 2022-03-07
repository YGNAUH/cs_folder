while(1):
    try:
        password = input()
        score = 0
        if len(password) <= 4:
            score = 5
        elif len(password) <= 7:
            score = 10
        else:
            score = 25
        
        letter_up = 0
        letter_low = 0
        digitmix = 0
        elsemix = 0
        for i in range(len(password)):
            if password[i].isupper():
                    letter_up += 1
            if password[i].islower():
                    letter_low += 1
            
            if password[i].isdigit():
                    digitmix += 1
 
            if password[i].isdigit() == 0 and password[i].isalpha() == 0:
                elsemix += 1
        if (letter_up >0 and letter_low == 0) or (letter_low >0 and letter_up == 0):
            score += 10
        elif letter_up >0 and letter_low > 0:
            score += 20

        if digitmix == 1:
            score += 10
        elif digitmix > 1:
            score += 20

        if elsemix == 1:
            score += 10
        elif elsemix >= 1:
            score += 25
        letters = letter_low + letter_up
        if letter_low > 0 and letter_up > 0 and digitmix > 0 and elsemix > 0:
            score += 5
        elif letters > 0 and digitmix > 0 and elsemix > 0:
            score += 3
        elif letters > 0 and digitmix > 0:
            score += 1 
        
        if score >= 90:
            print("VERY_SECURE")
        elif score >= 80:
            print("SECURE")
        elif score >= 70:
            print("VERY_STRONG")
        elif score >= 60:
            print("STRONG")
        elif score >= 50:
            print("AVERAGE")
        elif score >= 25:
            print("WEAK")
        else:
            print("VERY_WEAK")

    except:
        break
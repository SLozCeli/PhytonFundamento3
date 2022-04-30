
def cred(v = 1):
    while True:
        try:    
            v = int(input("Number: "))
            vs = str(v)
### VISA
            if len(vs) == 13 and vs[0] == 4:
                j = 0
                k = 0
                while 13 > k:
                    for i in vs:
                        if k%2 != 0:
                            i_2 = int(i) * 2
                            if i_2 >= 10:
                                i_3 = str(i_2)
                                i_3 = int(int(i_3[0]) + int(i_3[1]))
                                j += i_3
                                k +=1    
                            else:
                                j += i_2
                                k += 1
                        elif k%2 == 0:
                            j += int(i)
                            k += 1
                if j%10 == 0:
                    print("VISA\n")
                else:
                    print("INVALID\n")
### American Express
            elif len(vs) == 15:
                if int(vs[0]) == 3:
                    if int(vs[1]) == 4 or int(vs[1]) == 7:
                        j = 0
                        k = 0
                        while 15 > k:
                            for i in vs:
                                if k%2 != 0:
                                    i_2 = int(i) * 2
                                    if i_2 >= 10:
                                        i_3 = str(i_2)
                                        i_3 = int(int(i_3[0]) + int(i_3[1]))
                                        j += i_3
                                        k +=1    
                                    else:
                                        j += i_2
                                        k += 1
                                elif k%2 == 0:
                                    j += int(i)
                                    k += 1
                        if j%10 == 0:
                            print("AMEX\n")
                        else:
                            print("INVALID\n")
                    else:
                        print("INVALID\n")
                else:
                    print("INVALID\n")
### VISA o MASTERCARD
            elif len(vs) == 16:
### VISA
                if int(vs[0]) == 4:
                    j = 0
                    k = 0
                    while 16 > k:
                        for i in vs:
                            if k%2 == 0:
                                i_2 = int(i) * 2
                                if i_2 >= 10:
                                    i_3 = str(i_2)
                                    i_3 = int(int(i_3[0]) + int(i_3[1]))
                                    j += i_3
                                    k +=1    
                                else:
                                    j += i_2
                                    k += 1
                            elif k%2 != 0:
                                j += int(i)
                                k += 1
                        if j % 10 == 0:
                            print("VISA\n")
                        else:
                            print("INVALID\n")

### MASTERCARD
                elif int(vs[0]) == 5 and int(vs[1]) in range(1, 6):
                    j = 0
                    k = 0
                    while 16 > k:
                        for i in vs:
                            if k%2 == 0:
                                i_2 = int(i) * 2
                                if i_2 >= 10:
                                    i_3 = str(i_2)
                                    i_3 = int(int(i_3[0]) + int(i_3[1]))
                                    j += i_3
                                    k +=1    
                                else:
                                    j += i_2
                                    k += 1
                            elif k%2 != 0:
                                j += int(i)
                                k += 1
                    if j % 10 == 0:
                        print("MASTERCARD\n")
                    else:
                        print("INVALID\n")
                else:
                    print("INVALID\n")
            else:
                print("INVALID\n")

        except:
            print("INVALID\n")
        break

cred()
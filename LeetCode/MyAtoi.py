def myAtoi(s: str) -> int:
    t = False
    listOfIntegers = ["-","0","1","2","3","4","5","6","7","8","9"]
    finalList = []
    a = 0
    if a != len(s[a]):
        while listOfIntegers.__contains__(s[a]):
            if listOfIntegers.__contains__(s[a]):
                if s[a] == "-":
                    if listOfIntegers.__contains__(s[a+1]):
                        finalList.append(s[a])
                        a += 1
                        t = True
                if listOfIntegers.__contains__(s[a]):
                    finalList.append(s[a])
                    a += 1
                    t = True
                else:
                    t = True
                    break
            else:
                a += 1


    if t:
        D = [str(integer) for integer in finalList]
        a_string = "".join(D)
        res = int(a_string)
        return res
    else:
        return 0



print(myAtoi("42"))





import random

small_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
captial_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7']
other_sign = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
              ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

pass_len = int(input("enter length of pass (8 to 12): "))
t_number = int(input("enter range of num in pass : "))
t_other_sign = int(input("enter total num of sumble in pass : "))


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


# simple


if int(pass_len) >= 8 and int(pass_len) <= 12:
    if (t_number) < pass_len or (t_other_sign) < pass_len-t_number:
        a = random.choices(small_letter, k=int((pass_len-t_other_sign-t_number)/2))
        c = random.choices(numbers, k=int(t_number))
        d = random.choices(other_sign, k=int(t_other_sign))
        b = random.choices(captial_letter,  k=int(pass_len-len(a)-len(c)-len(d)))
        rand_pass = listToString(a)+listToString(b) + \
            listToString(c)+listToString(d)
        print(f"Easy random pass is: {rand_pass}")

    else:
        print("please, Enter num in range")


else:
    print("oh! enter pass range 8 to 12 ")


# hard

lis = []
def listpass(l):
    for x in l:
        lis.append(x)
    

if int(pass_len) >= 8 and int(pass_len) <= 12:
    if (t_number) < pass_len or (t_other_sign) < pass_len-t_number:
        a = random.choices(small_letter, k=int((pass_len-t_other_sign-t_number)/2))
        c = random.choices(numbers, k=int(t_number))
        d = random.choices(other_sign, k=int(t_other_sign))
        b = random.choices(captial_letter,  k=int(pass_len-len(a)-len(c)-len(d)))

        listpass(a)
        listpass(b)
        listpass(c)
        listpass(d)

        new_hard_rand_pass = random.shuffle(lis)
        pass_convert_string = listToString(lis)
        print(f"Hard random pass is: {pass_convert_string}")

    else:
        print("please, Enter num in range")


else:
    print("oh! enter pass range 8 to 12 ")

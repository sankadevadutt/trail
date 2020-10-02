print("Enter number for pallindrom check")
number = int(input())
pall_check = number
reverse=0
while number>0 :
    a = number%10
    reverse = reverse * 10 + a
    number-=a
    number = int(number/10)
print ("pallindrom" if (pall_check == reverse) else "not a pallindrom")

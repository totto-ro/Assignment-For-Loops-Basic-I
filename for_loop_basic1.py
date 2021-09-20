#Basic
for num in range(0,101,1):
    print(num)

#Multiples of Five
for num in range(5,1001,5):
    print(num)

#Counting, the Dojo Way
for num in range(1,101,1):
    if num % 10 == 0:
        print("Coding")
    elif num % 5 == 0:       #if its divisible by 10 print "coding", unless its divisible by 5, print "coding dojo"
        print("Coding Dojo")
    else:
        print (num)

#Whoa. That Sucker's Huge
sum = 0
for num in range(0,500001,1):
    if num % 2 != 0:
        sum += num
print(sum)

#Countdown by Fours
for num in range(2018,-1,-4):
    print(num)

#Flexible Counter 
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum + 1,1):
    if num % mult == 0:
        print(num)






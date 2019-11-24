#question 1
for i in range (1,6) :                                                            #5 lines
    a = "*"
    print (a*i)                                                                   #print * according to the line number

for i in range (1,6) :                                                            #5 lines
    a = "*"
    b =" "
    print (b*(5-i)+a*i)                                                           #print * and space according to the line number

for i in range (1,6) :                                                            #5 lines
    a = "*"
    b =" "
    print (b*(5-i)+a*2*i+b*(5-i))                                                 #print * and space according to the line nubmer


#question 2
cont = "y"                                                                        #default value of cont is "y"
while cont.lower() == "y":                                                        #do loops until input "n"
    print("Please input a number to verify whether it is a leap year or not:")
    year = int(input())
    if year%400 == 0:                                                             #if the year is divisible by 400, it is a leap year
        print("True")
    elif year%100 == 0:                                                           #if the year is not divisible by 400 and can be divided by 100, it is not a leap year
        print("False")
    elif year%4 == 0:                                                             #if the year is not divisible by 100 and can be divided by 4, it is a leap year
        print("True")
    else: print("False")                                                          #if the year is not divisible by 4, it is not a leap year
    cont = input("Do you want to verify again? (y/n):")                           #ask if verify again or not


#question 3
cont = "y"                                                                        #default value of cont is "y"
chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
keys = dict(zip(chars, codes))                                                    #create a dictionary from letter to morse code
while cont.lower()=="y":                                                          #do loops until input "n"
    print("Please input a word:")
    word = input()
    temp = set()
    for index in word:
        temp_morse = []                                                           #create a list to store letters
        for i in index:
            temp_morse.append(keys[i])                                            #add objects at the end of the list
        s=''.join(temp_morse)                                                     #connect the strings together
        print(s,end="")
    print("\n Do you want to input a word again? (y/n): ")
    cont=input()


#question 4
import math
import re

def findComplement(num):
    numWord=bin(num)                                                              #converts decimal number to binary representation
    numWord=numWord[2:]                                                           #trims initial 2 chars from the string
    length=len(numWord)                                                           #calculates the length of the string
    i=0
    res=''
    #Following loop would iterate for every char to convert it.
    while i<length:
        if numWord[i]=='1':
            res+='0'
        else:
            res+='1'
        i+=1
    return res

def find2sComplement(string):
    num=int(string)+1                                                             #add 1 to the binary representation
    strs = list(map(int, str(num)))                                               #create a list to separate numbers
    length=len(string)
    if re.search("0",string):                                                     #if the first number of the string is 0, decrease the length by one
        length-=1
    sum=0
    i=length-1
    while 0<=i<length:                                                            #use loops to get the sum of numbers in the list
        sum+=strs[i]*math.pow(2,length-i-1)
        i-=1
    return int(sum)

print("Please input a number:")
num =int(input())
string=findComplement(num)
print(find2sComplement(string))


#question 5
list1=[0,0]                                                                       #create a list to store the position information
print("Please input the move sequence:")
string=input()
list_string=list(string)                                                          #convert the string to a list
length=len(string)
i=0
while i<length:                                                                   #use loop to get the position
    if list_string[i]=="R":
        list1[0]=list1[0]+1
    elif list_string[i]=="L":
        list1[0]=list1[0]-1
    elif list_string[i]=="U":
        list1[1]=list1[1]+1
    elif list_string[i]=="D":
        list1[1]=list1[1]-1
    else:                                                                         #if the input is not correct, list1=["a","a"] and break
        list1=["a","a"]
        break
    i+=1
if list1==[0,0]:                                                                  #use if to verify if the robot make a circle
    print("True")
elif list1==["a","a"]:
    print("Please input a correct move sequence!")
else:
    print("False")


#question 6
print("Please input a number:")
num=int(input())
print("Please input a word:")
word=input()
list_word=list(word)                                                               #create a list to store the word information
i=len(word)
if num==0 or num>1:                                                                #if number equals to 0 or greater than 1, add "s" according to rules
    if word[-3:]=="ife":                                                           #words end in ife,becomes ives
        list_word[i-2]="v"
        list_word+=["s"]
    elif word[-2:]=="sh" or word[-2:]=="ch":                                       #words end in sh/ch,becomes shes/ches
        list_word+=["es"]
    elif word[-2:]=="us":                                                          #words end in us,becomes i
        list_word[i-2]="i"
        list_word[i-1]=""
    elif word[-1:]=="y":                                                           #words end in y,becomes ies except end in ay/oy/ey/uy
        if word[-2:]=="ay" or word[-2:]=="oy" or word[-2:]=="ey" or word[-2:]=="uy":
            list_word+=["s"]
        else:
            list_word[i-1]="i"
            list_word+=["es"]
    else:                                                                          #words end in everything else, add -s
        list_word+=["s"]
print(num, "".join(list_word))


#question 7
#def is_prime
num = int(input("Please input a number: "))
if num < 2:                                                                        #if the number is less than 2, print false
    print("False")
else:
    i = 2
    while i < num:                                                                 #do loops until i equals to number
        if num % i == 0:
            print("False")
            break
        i += 1
    if i >= num:
        print("True")


#question 8
#def snake_case
print("Please input a string:")
list_text=list(input())                                                            #store the input string in a list
final=''
for i in range (len(list_text)):
    item=list_text[i]
    if i<len(list_text):                                                           #converting everything to lowercase and separating by underscores
        if item.isupper():
            final+="_"+item.lower()
        else:
            final+=item
if final[0]=="_":                                                                  #delete the first "_" if the first one is capital letter
    final=final[1:]
print(final)


#question 9
#def get_number_input
judge=0
while judge==0:
    print("Please enter a number:")
    num = input()
    try:
        float(num)      # convert input to float, if error, judge=0 and continue to ask
        judge=1
    except ValueError:
        judge=0

print("The number you entered:",num)

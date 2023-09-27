def title1():
    print("****************************   !!!!!!! WELCOME YOU  !!!!!     ***************\n")
    print("    TOTAL QUESTION : 5                                                                    TOTAL PRICE :- 700000\n")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    
def question_1():
    print("""Q.1 )  What is the output of the following code? 
          
                    x = 10
                    y = 5
                    result = x / y
                    print(result)
          
                         a) 2         b) 5            c) 10.0                 d) 0  \n""")
    answar_1=input("enter the option : ")
    if answar_1=="a" or answar_1=="A":
        print(" CORRECT Answer ")
        print(" Congratulations !!  you won : 50,000/- rupee\n")
    else:
        print("SORRY ! Your Answer is worng ")
      #  print("----------------------------------SO GAME IS OVER -------------------------------------------------------------------")

def question_2():
    print("""Q.2 )  Which of the following is the correct way to comment a single-line code in Python? 

                             a) /* comment */      b) // comment    c) # comment     d) <!-- comment -->  \n""")
    
    answar_2=input("enter the option : ")
    if answar_2=="c" or answar_2=="C":
        print(" CORRECT Answer ")
        print(" Congratulations !!  you won : 1,50,000/- rupee\n")
    else:
        print("SORRY ! Your Answer is worng ")
       # print("----------------------------------SO GAME IS OVER -------------------------------------------------------------------")

def question_3():
    print("""Q.3 )  What is the output of the following code?

                        my_list = [1, 2, 3, 4, 5]
                        result = my_list[1:3]
                        print(result)


                            a) [1, 2]        b) [2, 3]        c) [2, 3, 4]            d) [3, 4]  \n""")
    
    answar_3=input("enter the option : ")
    if answar_3=="b" or answar_3=="B":
        print(" CORRECT Answer ")
        print(" Congratulations !!  you won : 3,00,000/- rupee\n")
    else:
        print("SORRY ! Your Answer is worng ")
       # print("----------------------------------SO GAME IS OVER -------------------------------------------------------------------")
def question_4():
    print("""Q.4 )  In Python, which of the following is used to take input from the user?

                        a) get()            b) read()         c) input()                d) scanf() \n""")
    
    answar_4=input("enter the option : ")
    if answar_4=="c" or answar_4=="C":
        print(" CORRECT Answer ")
        print(" Congratulations !!  you won : 4,80,000/- rupee\n")
    else:
        print("SORRY ! Your Answer is worng ")
       # print("----------------------------------SO GAME IS OVER -------------------------------------------------------------------")
def question_5():
    print("""Q.5 )   What will be the output of the following code?
          
                            x = 5
                            y = 2
                            result = x ** y
                            print(result)

                         a) 10             b) 25            c) 7                d) 1   \n""")
    
    answar_5=input("enter the option : ")
    if answar_5=="b" or answar_5=="B":
        print(" CORRECT Answer ")
        print(" Congratulations !!  you won : 7,00,000/- rupee\n")
    else:
        print("SORRY ! Your Answer is worng ")
      #  print("----------------------------------SO GAME IS OVER -------------------------------------------------------------------")




print("\n")
permission=input("ARE YOU READ FOR PLAYING GAME :\n (enter YES or NOT)\n : ")
if permission=="yes":
    show1=title1()
elif permission =="no":
    print("PLEASE ENTER Yes !! ")
    permission=input("ARE YOU READ FOR PLAYING GAME :\n (enter YES or NOT)\n : ")
    if permission=="yes":
        show1=title1()
question_1()
question_2()
question_3()
question_4()
question_5()
print("\n===============================================================================================================")
print("----------------------- !!!!!!!!!!! THE GAME IS OVER !!!!!!!!!!! -----------------------------------------------")





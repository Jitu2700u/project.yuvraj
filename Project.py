print(" 1 - Add ")
print("2 - subtract")
print("3 - multiply ")
print("4 - divide")
option = int(input("operation -"))
if(option in [1,2,3,4]):
    num1 = int(input("Frist number - "))
    num2 = int(input("second number - "))#     calculator

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 // num2
else:
        print("invalid operation")
print("ANSWER {}".format(result))



#KAUN BANEGA COROREPAATI
A = "kaun banega corepati"
print(A.center(50))
B = "Q.1 Yuvraj ka nick name kya hai"
print(B.center(45))
C = "1] jitu"

D = "2] UV"
print(C.center(22))
print(D.center(20))
UV = int(input("Select Your answer :-"))
match UV:
     case 1:
         print("your ans is correct")
         print("you win 50₹")
     case 2:
         print("your ans is incorrect")
         print("you loses")


#KAUN BANEGA COREREPATI 2.0

questions =["yuvraj khangar real name", "uv","jitu","kokushibo","none",4]
questions =["yuvraj khangar real name", "uv","jitu","kokushibo","none",4]
questions =["yuvraj khangar real name", "uv","jitu","kokushibo","none",4]
questions =["yuvraj khangar real name", "uv","jitu","kokushibo","none",4]
level = [10,100,1000,10000]
for i in range(0, len(questions)):
    question = questions[i]

    print(f"\n\nquestions is for {level[i]}")

    print(questions[0])
    print(f"1.{questions[1]}             2.{questions[2]}")
    print(f"4.{questions[3]}      3.{questions[4]}")
    reply = int(input("enter your answer: "))
    if (reply == 0):
        break
    if (reply == 2):
       print(f"u won {level[i]}")
       if (i ==0):
           prize = ("airplane")
           if i == 0:
               print("quit 0")
       elif(i == 1):
           prize = ("privat yart")


    else:
        print("u lost game")
        break
print(f"your prize is {prize}")
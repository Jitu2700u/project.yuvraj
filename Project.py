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

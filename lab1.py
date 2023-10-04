"Task 1"
"1.1"
print('4','8','15','16','23','42')
“на этом задаче мы просто использовали запетю” 
"1.2"
print('4')
print('8')
print('15')
print('16')
print('23')
print('42')
“на этом задаче мы по отдельности всех написали через принт ” 
"1.3"
a = int(input())
print(a+1)
print(a+2)
“здесь мы просто плюсуем на a на 1 и на 2” 
"1.4"
a = int(input()) 
b = int(input()) 
c = int(input()) 
q = a + b + c 
print(q) 
“на этом задаче мы должны найти общий сумму всех чисел мы здесь всех просто плюсуем и  вводим общию сумму “ 

"1.5"
'''
Сначала вводим длину ребра через тип данных int 
который принимает только целые числа
'''
a1 = int(input())
'''
Вводим формулу обьема куба и поверхности куба через команду Print
'''
print("Volume is =",a1**3)
print("Total surface area is =",6*(a1**2))
"Task 2"
"2.1"
n = int(input()) 
k = int(input()) 
print(n // k) 
print(n % k)  
“здесь мы использовали арифметические операторы // и %, // это означает деление, % это остаток ” 
"2.2"
c = int(input())
c1 = c//1000
c2 = (c//100)%10
c3 = (c%100)//10
c4 = c%10
print('The number in the thousands position equals', c1)
“выводит первую цифру введенного числа” 
print('The number in the hundreds position is', c2)
“выводит вторую цифру введенного числа” 
print('The digit in the tens position is equal to', c3)
“выводит третью  цифру введенного числа” 
print('The digit in the units position is equal to', c4)
“выводит четвертую цифру введенного числа” 
"2.3"
n=int(input()) 
print((n+1)//2) 
“здесь мы просто плюсуем 1 на 99 и делим на 2” 

"2.4"
try:
    e = int(input("Enter the number:"))
    if e==0:
        print("Error,Try again!")
    else:
        print("The result of << is:",2**e)
except ValueError:
    print("Please enter a valid integer!")



"2.5"
print("please enter the first number:")
e = int(input())
print("please enter the second number:")
m = int(input())
print("please choose an operation (+, -, *, /):")
b = str(input())
if b=='+' :
    print(e+m)
elif b=='-':
    print(e-m)
elif b=='*':
    print(e*m)
elif b=='/':
    print(int(e/m))

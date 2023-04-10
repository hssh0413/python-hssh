'''
input(입력)
.문법
-input("A")
'''
while True:
    num1=input("첫번째 수: ")
    num2=input("두번째 수: ")
    str=f"첫번째 수는 {num1}이고,두번째 수는 {num2}라서 두 수의 합은 {int(num1)+int(num2)}이고,차는 {int(num1)-int(num2)}이고,곱은 {int(num1)*int(num2)}이고,첫번째 수를 두번째 수로 나눈 몫은 {int(num1)//int(num2)}이고,나머지는 {int(num1)%int(num2)}입니다."
    print(str)
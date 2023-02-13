'''
함수
-반복적인 작업을 사용할떄 유용함
-함수를 호출하는 부분이 필요함
1)
def 함수이름():
    실행할 코드 작성
2)
def 함수이름(입력):
    실행할 코드 작성
3)
def 함수이름(입력):
    실행할 코드 작성
    return 출력
'''
# Q1-두수의 입력을 받아,합만큼 출력
# def hssh(a,b):
#     for i in range(a+b):
#         print("chatGPT")
# hssh(2,3)
# hssh(5,10)
# Q2-두수의 입력을 받아,두수의 합,차,곱,나누기 의 결과를 출력
# def hssh(a,b):
#         print(a+b,a-b,a*b,a/b)
# hssh(3,2)
# hssh(10,5)
# Q3-구구단 출력
# def hssh(a):
#     for i in range(1,10):
#         print(i*a)
# hssh(3)
# hssh(7)
# Q4-삼각형 넓이
# def hssh(a,b):
#     print(a*b/2)
# hssh(3,6)
# hssh(10,20)
# Q5-주어진 수중 짝수 출력
def hssh(a):
    for i in range(a%2==0):
        print(i)
hssh(5)
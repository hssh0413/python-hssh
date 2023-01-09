'''
조건문
1.if/else
1)
  if 조건:
    참일떄 실행할거 작성
  else:
    거짓일떄 실행할거 작성
2)
  if 조건:
    참일떄 실행할거 작성
  elif 또 다른 조건:
    조건은 거짓 또 다른 조건이 참일때 작성
  else:
    모두 다 거짓일때 작성

2.for
1)
 for 변수 in range(반복 숫자):
    실행할 내용
  +반복 숫자=0부터 시작
2)
  for 변수 in range(시작 숫자,끝 숫자):
    실행할 내용 
  +시작 숫자=이상,
   끝 숫자=미만
   1씩 증가
3)
  for 변수 in range(시작,끝,증감 숫자):
    실행할 내용
'''
# 1
# for i in range(1,10):
#     if i%2==1:
#         print(i)

# 2
# for i in range(1,11):
#     if i%3!=0:
#         print(i)
# 3
# for i in range(50,101):
#     if i%3==0:
#         if i%4==0:
#             print(i)
# 4
# a=1
# for i in range(1,21):
#     if i%7==0:
#         a*=i
# print(a)
# 5
# a=0
# for i in range(50,61):
#     if i%4!=0:
#         a+=i
# print(a)
# 6
# a=1
# b=1
# for i in range(1,101):
#     if i%2==0:
#         a+=i
#     if i%2!=0:
#         b+=i
# print(a-b)
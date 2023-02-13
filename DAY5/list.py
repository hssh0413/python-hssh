'''
리스트(list)
-열거형 변수를 나타내는 자료구조 중 하나
-대괄호로 표현
-각 요소는 쉼표로 구분
-비어있는 list는 "[]"로 표현
-메소드를 가짐
    -특1,맨 오른쪽에 요소를 추가할 때 append 메소드 사용
    -특2,맨 오른쪽 요소를 삭제할 때 pop 메소드 사용
    -특3,list 전체를 비울 때는 clear 메소드 사용
    -특4,오름차순 정렬할 때 sort 메소드 사용
    -특5,list를 거꾸로 정렬할 때 reverse 메소드 사용
'''
# a=1
# b="list"
# c=[1,2,3,4]
# print(c)
# d=["apple","bananaaaaa","fys"]
# print(d)
# e=[1,"apple",2,"banana"]
# print(e)
# f=[]
# print(f)
# f.append(100)
# print(f)
# f.append(50)
# print(f)
# f.append(1)
# print(f)
# f.pop()
# print(f)
# f.pop()
# print(f)
# f.pop()
# print(f)
# g=[100,50,1]
# g.clear()
# print(g)
# h=[2,4,1,3]
# h.sort()
# print(h)
# i=["orange","cherry","apple"]
# i.sort()
# print(i)
# j=[2,4,1,3]
# j.reverse()
# print(j)
# Q1.[2,4,1,3]을 내림차순 정렬
# j=[2,4,1,3]
# j.sort()
# j.reverse()
# print(j)
# Q2.1~20 중 3의 배수를 내림차순 list로 출력
# a=[]
# for i in range(1,21):
#         if i%3==0:
#             a.append(i)
#             a.sort()
#             a.reverse()
# print(a)
# Q3.구구단
for i in range(1,10):
    print(i*a)
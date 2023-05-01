"""
dictionary
.python에서 사용하는 자료구조 중 하나
.key와 value 쌍으로 존재
.문법:{}와 :를 이용
.indexing 가능=key를 이용해서
.indexing method를 사용하는 방법:get
.keys method를 이용해서 dict. 내 key값들 모두를 확인할 수 있음
.values method를 이용해서 dict. 내 value값들 모두를 확인할 수 있음
.value 수정하는 방법
 -indexing 이용
 -update method 이용
.key와 value 쌍을 추가하는 방법
 -indexing 이용
 -update method 이용
.key와 value 쌍을 삭제하는 방법
."key in dict"사용 시 tf
"""
# sports={'손흥민':'축구','류현진':'야구','서장훈':'농구'}
# print("손흥민"in sports)
# print("강호동"in sports)

fruits={"orange":50,"banana":100,"apple":200}
fruit=input("This is fruit store.What do you want?:")
if fruit in fruits:
    print(f"We have {fruit}.{fruits[fruit]} left.")
else:
    print(f"sorry,we don't have {fruit}")
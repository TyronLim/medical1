a = [1,2,3,4,5]
c = [*a] # 전개연산자
b = a # 얕은 복사
a[1] = 20 # a 데이터 값 변경
print(b) # 같이 변경이 됨
print(c) # 같이 변경이 안 됨. 

product = ['새우깡','90g',1200,3]

print('상품 : {}, 무게 : {}, 가격 : {}원, 유통기한 : {}년'.format(
    product[0],product[1],product[2],product[3]))

print('상품 : {}, 무게 : {}, 가격 : {}원, 유통기한 : {}년'.format(*product))
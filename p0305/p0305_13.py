foods = {'떡볶이':'오뎅', '짜장면':'단무지', '라면':'김치',
         '피자':'피클', '맥주':'땅콩', '삼겹살':'상추'}

# 키의 값을 출력하시오.
print(foods.keys())
for key in foods:
    print(key,end = '\t')
print()
# value값을 출력하시오.
print(foods.values())
for key in foods:
    print(foods[key],end='\t')
print()
# key : value 형태로 출력하시오.
for key in foods:
    print('{}:{}'.format(key,foods[key]))


ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 재밌진 않죠^^'
# 존재하는 문자가 몇번 나왔는지 확인
print(ss.count('공부'))
print(ss.count('자바')) # 없으면 0

# 존재하는 문자열의 첫글자의 위치값
print(ss.find('물론 모든'))
print(ss.find('자바')) # 없으면 -1
print(ss.find('공부',21)) # 문자열 7번째 자리부터 검색시작해서 위치값 출력

print(ss.rfind('공부')) # 존재하는 문자열의 첫글자의 위치값 (뒤에서부터 검색 시작)
print('-'*20)

#index
print(ss.index('공부'))  # 위치값
# print(ss.index('자바'))  # 없으면 에러
print(ss.rindex('공부')) # 뒤에서부터 검색 시작

print(ss.startswith('파이썬'))  # 맞으면 True
print(ss.startswith('공부'))    # 틀리면 False

print(ss.endswith('^^'))   # 끝나는 문자열이 맞으면 True
print(ss.endswith('자바'))   # 끝나는 문자열이 틀리면 False







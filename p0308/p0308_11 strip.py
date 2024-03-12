# strip() 공백 제거
ss = 'apple은 당도가 높고, apple의 색상은 빨강, 녹색이 있습니다.'
s1 = '        파    이     썬                '
s2 = '파이썬'

print(s1.lstrip())     # 글자 기준 왼쪽의 공백 제거
print(s1.rstrip())     # 글자 기준 오른쪽의 공백 제거
print(s1.strip())     # 왼, 오의 모든 공백 제거

# replace (문자열을 다른 문자열로 대체)
print(s1.replace(' ',''))
print(ss.replace('apple은','사과는'))

news = "정용진 신세계그룹 총괄부회장이 8일 회장 자리에 올랐다.\
    2006년 부회장에 오른 후 18년 만에 이뤄진 승진 인사다. 지난해 이마트 창립 이후 적자를 기록했고, \
    신세계그룹 매출이 감소하는 등 사업 환경이 악화하면서 위기 극복을 위한 새로운 리더십을 내세웠다."
print(news.replace(' ','')) # 공백 제거
print(news.replace('그룹','group'))   # 그룹을 group으로 변경    
 # 비파괴 = 출력은 가능하지만 원본 news 에는 반영이 안 됨.



# # input 시 빈공백 제거
# s_input = input('문자를 입력하세요. >> ').strip()           # 인풋값에 공백 제거

# if s_input() == s2:             # 공백 제거
#     print(True)
# else :
#     print(False)

# # if s1.strip() == s2:             # 공백 제거
#     print(True)
# else :
#     print(False)
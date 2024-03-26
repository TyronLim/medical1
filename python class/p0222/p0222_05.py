# 변수 : kor, eng, math

# kor = input('국어 점수 => ')
# eng = input('영어 점수 => ')
# math = input('수학 점수 => ')
# kor = int(kor)
# eng = int(eng)
# math = int(math)
# avg = int(kor+eng+math)/3

# print("평균은", '{:.0f}'.format(avg),"입니다.")


kor = 100
eng = 90
math = 80
# print("평균은 {}점 입니다".format((kor+eng+math)/3))
print("평균은 %.0f점입니다."%int((kor+eng+math)/3))
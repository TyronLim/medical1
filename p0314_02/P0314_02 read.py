# read용 파일

# 파일 열기
file = open('떫떠름한치즈김밥.txt','r',encoding='utf-8')

# 파일 읽기
content = file.read()   # read를 써서 메모장의 모든 글을 읽어옴.
content = content.strip()  # strip = 문자열 빈 공백 제거

print(content)  # strip = 문자열 빈 공백 제거
stuNo,name,kor,eng,math = content.split('\n') # 홍길동,100,99,98.         split(',') = 문자열을 쉼표로 분리 (list 타입으로)
print(stuNo,name,kor,eng,math)
c_list = [0]*5
c_list[0] = int(stuNo)
c_list[1] = name
c_list[2] = int(kor)
c_list[3] = int(eng)
c_list[4] = int(math)
print(c_list)

# 파일 닫기
file.close()
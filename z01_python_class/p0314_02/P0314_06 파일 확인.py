txt = '파이썬 파일 중에 a.txt 이 폴더에 존재합니다'
print(txt.find('나나'))         # find 는 없으면 -1 출력. 
print(txt.find('.'))           # 있으면 위치값 출력
print(txt.count('.'))          # count는 있으면 개수를 출력, 없으면
print(txt.count('나나'))       # 없으면 0 출력
print(txt.endswith('합니다'))  # endswith는 그 문자열로 끝나면 True.
print(txt.endswith('폴더에'))  # 아니면 False.


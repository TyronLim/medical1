print('1234'.isdigit())     # 숫자인지 확인
print('1234a'.isdigit())    # 숫자인지 확인 False
print('abc'.isalpha())      # 영어인지 확인
print('abc1'.isalpha())     # 영어인지 확인 False
print('abc'.islower())      # 소문자인지 확인
print('abcA'.islower())     # 소문자인지 확인 False
print('ABS'.isupper())      # 대문자인지 확인
print('ABaS'.isupper())     # 대문자인지 확인 False
print('a dw 123'.isspace()) # 문자열이 빈공백인지 확인 아니면 False
print(' '.isspace())        # 문자열이 빈공백인지 확인 맞으면 True
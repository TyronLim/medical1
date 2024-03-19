# 예외 - 프로그램 실행시 알 수 없는 오류로 인한 프로그램 종료를 방지하기 위해 사용
# 프로그램 에러 - 프로그램 실행하면서 수정을 해야 함.

# try : 프로그램에서 오류가 발생될 것 같은 소스
# except : 오류가 발생되었을 때 처리하는 구문 소스
# except Exception as e : 예외발생 시, 어떤 예외가 발생 되었는지 확인 가능  print(e)
# 예외 종류별로 except 가능
# valueError, Index, ZeroDivisionError.....     최고부모 : Exception
# else : 오류가 발생하지 않았을 때 처리하는 소스
# finally : 무조건 실행되는 소스
# raise : 강제로 예외 발생      raise '메모내용'


print('1.학생성적입력')
print('2.학생성적출력')
print('3.학생성적수정')
num = int(input('숫자 입력 >>'))

if num == 1:
    print('학생성적입력 완성')
    
elif num == 2:
    print('김과장이 해야 할 부분')
    raise '김과장에게 소스를 받아야 함'         # 강제로 예외를 발생시켜 알림 형태로 많이 씀
    
elif num == 3:
    print('이대리가 해야 할 부분')
    raise '이대리에게 소스를 받아야 함'

while True:
    print("-"*40)
    print("[ 학생성적프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체입력")
    print("3. 학생검색")
    print("4. 학생성적수정")
    print('5. 학생삭제')
    print('6. 등수처리')
    print('7. 학생성적 파일저장')
    print('0. 프로그램종료')
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.>> ")
    if not choice.isdigit():
        print('정확한 번호를 입력하세요.')
        continue
    choice = int(choice)

    if choice == 1:
        print('학생성적입력')
        search = input('입력할 학생의 이름을 입력해주세요. >> ')



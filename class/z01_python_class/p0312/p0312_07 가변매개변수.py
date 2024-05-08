# 가변매개변수

def str_title(num,*txt):
    print('타입 :',type(txt))
    print(txt)
    for i in range(num):
        for t in txt:
            print(t,end=' ')

str_title(1,'안녕','잘가','안녕하세요','반가워요')
    
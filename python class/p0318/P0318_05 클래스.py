class Tv:               # 클래스 선언 - 설계도
    channel = 0
    color = 'black'
    size = 65
    volume = 0
    
    def up_volume(self,volume):
        self.volume += volume
        
    def down_volume(self,volume):
        self.volume -= volume

    def up_channel(self,channel):
        self.channel += channel
        
    def down_channel(self,channel):
        self.channel -= channel
        
    def __init__(self,channel,color):
        self.channel = channel
        self.color = color
        
        
        
# 철수=white,채널 10변경, 2증가 / 영희=pink,채널 7변경, 5 증가 / 반장=silver,채널 1, 채널 3증가

tv1 = Tv(10,'white')
tv1.up_channel(2)
print('철수 TV :',tv1.color,tv1.channel,tv1.size,tv1.volume)

tv2 = Tv(7,'pink')
tv2.up_channel(5)
print('영희 TV :',tv2.color,tv2.channel,tv2.size,tv2.volume)

tv3 = Tv(1,'silver')
tv3.up_channel(3)
print('반장 TV :',tv3.color,tv3.channel,tv3.size,tv3.volume)


# tv1 = Tv()            # 객체선언 - 제품생산
# tv1.color = 'white'
# tv1.channel = 10
# tv1.up_channel(2)
# print('철수 TV :',tv1.color,tv1.channel,tv1.size,tv1.volume)

# tv2 = Tv()
# tv2.color = 'pink'
# tv2.channel = 7
# tv2.up_channel(5)
# print('영희 TV :',tv2.color,tv2.channel,tv2.size,tv2.volume)

# tv3 = Tv()
# tv3.color = 'silver'
# tv3.channel = 10
# tv3.up_channel(2)
# print('반장 TV :',tv3.color,tv3.channel,tv3.size,tv3.volume)

    

    
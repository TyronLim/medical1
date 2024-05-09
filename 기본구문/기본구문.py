import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
df.sort_index(inplace=True)
df.to_csv('score.csv',encoding='utf-8-sig')
df.to_csv('score.txt',encoding='utf-8')
df.to_excel('score.xlsx')


#    --------------행----------------------------둘 다---------------------------열---------------
# df            df[0:1]                                                     '열이름'                    
# df        ['index':'index']                                       
#  
# df.loc        ['index']                                               
# df.loc    ['index':'index']                                       
# df.loc   [['index','index']]                  
# df.loc                                   ['index','열이름']                         
# df.loc                         [['index','index'],['열이름','열이름']]                  
# 
# df.iloc       [행주소]
# df.iloc    [행주소:행주소]
# df.iloc                                       [0,0]
# df.iloc                                     [0:3,0:3]
# df.iloc                                    [0:3,[0,1]]
# df.iloc                                   [[0,2],[0,2]]
# df.iloc                                    [[0,3],0:2]

df.columns[0]   # '국어'


df.drop(columns=['합계'],inplace=True)
df.drop(index='1번',inplace=True)

df['item_price'] = df['item_price'].str.replace('$','').astype(float)       # 타입 변경, 달라 삭제

df.dropna(axis='columns',how='any',inplace=True)        ## 행이냐 열이냐 선택해서 NaN 삭제

bSet = list(zip('name','births','custom'))    ## zip
list(zip('name','births'))                  ## zip

str.slice(1,3)

df.loc['1번',['이름','키']]
df.loc[['1번','5번'],['이름','키']]         # row 데이터 출력
df.loc['1번':'5번','국어':'사회']

df['키'].max()
df['키'].min()
df['키'].mean()
df['키'].count()
df['item_name'].value_counts()  # 각각의 개수
df['키'].describe()
df['키'].info()
df['SW특기'].count()    # NaN은 카운트되지 않음
df['국어'].sum()        # 전체 합계

df.head(5)
df.tail(5)
df.values   # 리스트로
df.index    # index 정보
df.info()   # 정보
df.shape    # 행렬 크기
df.describe # 기본 정보 타입

# rows 데이터 가져오기
df[0:3]
df.iloc[[0,1,3]]

df.columns
df.columns[0]
df['이름']
df[df.columns[0]]   # = df['이름']
df[df.columns[-1]]  # 제일 마지막 컬럼

df.shape[0] # 행의 개수
df.shape[1] # 컬럼의 개수
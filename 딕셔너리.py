dic = {'name':'A', 'age':'20','height':'180'}
dic['weight'] = 70 #딕셔너리에 쌍추가
del dic['weight'] #딕셔너리 삭제

print(dic['name'])
 #리스트는 key불가, 튜플은 가능 (immutable이기 때문)
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get('name'))
print(dic.get(0)) #get()은 오류발생x 
print(dic.get(0,"default")) #디폴트값 생성
print('name' in dic)

print(list(dic.keys()))
dic.clear #초기화 

'''
print('안녕하세요')

for a in range(5):
    print('{} '.format(a), end='')

print()

for a in range(11):
    print('{} '.format(a), end='')

print()

for a in range(3, 10, 3):
    print('{} '.format(a), end='')


li = ['a', 'b', 'c']

print(str(li.index('c')))
print(li)

li.append('d')  #항상 맨 뒤에 추가
print(li)

li.insert(2, 'e')  #원하는 위치에 추가
print(li)

li.remove('e')
print(li)

del li[1]
print(li)

print('b' in li)
print('a' in li)

print(len(li))
print(li.count('d'))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num)
print(sum(num))
print(min(num))
print(max(num))

num.reverse()  # 역순 만들기
print(num)

num.sort()  #오름차순
print(num)

num.sort(reverse=True)  #내림차순
print(num)



# tu = tuple() 튜플은 값을 변경할 수 없다.
tu = ('a', 'b', 'c')
print(tu)
print(tu.index('b'))

num = (1,2,3)
n1,n2,n3 = num
print(num)
print(n1, n2, n3)

a='hello'
b='python'
c='world'
print(a, b, c)

(a,b,c) = (c,a,b)
print(a, b, c)

li = ['a','b','c','d']
li_tu = tuple(li)
print(li_tu)

tu = (1,2,3,4,5)
tu_li = list(tu)
print(tu_li)


# se = set() 세트 선언하기
# se={} 빈 값으로 선언할 시 세트 사용 불가능, 딕셔너리로 만들어짐

se1 = set()
se2 = {}
print(type(se1))
print(type(se2))

# 세트는 순서, 중복이 없음
# 순서가 없기 때문에 인덱스를 쓸 수 없음
a = {2,4,3,4,5}
b = {1,2,2,3,4,5,6}
print(a)
print(b)
print(type(a))
print(type(b))

a.add(9) #추가
print(a)

a_li = list(a)
print(a_li)

a_tu = tuple(a)
print(a_tu)

print()
print(a&b) #교집합
print(a|b) #합집합
print(a-b) #차집합
print(a^b) #대칭 차집합
'''

#딕셔너리 만들기
dic1 = {}
dic2 = dict()
print(type(dic1))
print(type(dic2))

dic = {'kor':90, 'eng':70, 'mat':100}
print(dic)
print(dic['mat'])
dic['sci'] = 40
print(dic['sci'])
#print(dic[2]) 인덱스는 사용할 수 없다. 키가 기준이기 때문

del dic['sci']
print(dic)

dic.clear()
print(dic)

dic = {'kor':90, 'eng':70, 'mat':100}
print(dic.keys())
print(dic.values())
print(dic.items())

print(tuple(dic))
print(list(dic))
print(set(dic))

print(tuple(dic.values()))

li=['ab','cd','ef']
print(dict(li))

li=[['a',1],['b',2],['c',3]]
print(dict(li))
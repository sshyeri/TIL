# pyformat
#'{} {}'.format('one','two')
name = '도레미'
# e_name = 'doraemi'
# print('안녕하세요? {}입니다. my name is {}.'.format(name, e_name))
# print('안녕하세요? {1}입니다. my name is {0}.'.format(name, e_name))
# print('안녕하세요? {1}입니다. my name is {1}.'.format(name, e_name),'\n')

# # f-string python 3.6
# print(f'안녕하세요? {name}입니다. my name is {e_name}')

import random

numbers = range(1,46)
pick = random.sample(numbers, 6)
print(f'추첨 번호는 {sorted(pick)}입니다.')
a=[1,2,3,4]
b=[5,6,7,8,9]
c=range(5)
d=range(4)
#print(a+b+'\n')
print(a+b,'\n')
#print(c+d)
print(list(c)+list(d))
print("내 이름은" + name)

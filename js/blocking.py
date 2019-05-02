from time import sleep

# 3초 자는 함수
def sleep_3s():
    sleep(3)
    print('Wake up!')
print('start sleeping')
sleep_3s() # blocking
print('end of program')
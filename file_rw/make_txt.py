# f = open("new.txt","w")
# f.write("Hello !!!")
# f.close()

# with open("new.txt","w") as f:
#     f.write("안녕하세요")

# f = open("new.txt","r")
# data = f.read()
# print(data)
# f.close()

# with open("new.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("new.txt","w", encoding='utf-8') as f:
#     for i in range(1,6):
#         data = f'{i}번째 줄입니다.\n'
#         f.write(data)

# with open("new.txt","a",  encoding='utf-8') as f :
#     f.write("짜잔")

# menu = ["카레\n", "육개장\n", "라면\n"]
# with open("menu.txt","w", encoding='utf-8') as f :
#     f.writelines(menu)

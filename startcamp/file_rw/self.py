# with open("ssafy.txt", "w", encoding='utf=8') as f:
#     for i in range(1,11):
#         data = f"{i}번째 줄입니다.\n"
#         f.write(data)
with open("ssafy.txt","r", encoding='utf=8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
   
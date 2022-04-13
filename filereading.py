f = open(
    "Bugatti.txt","rt"
    )
# print(f.readlines())
# print(f.readline())
# content = f.read()
for line in f:
    print(
        line,end=""
        )
# print(content)
# content = f.read(20)
# print(content)
# f.close()
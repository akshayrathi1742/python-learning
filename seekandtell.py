f = open(
    "Bugatti.txt"
    )
# print(f.tell())
print(
    f.readline()
    )
f.seek(
    10
    )
# print(f.tell())
print(
    f.readline()
    )
# print(f.tell())
f.close()
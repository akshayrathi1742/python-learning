with open (
    "Bugatti.txt"
    ) as f:
    a = f.read(
        12
        )
    print(a)

f = open(
    "Bugatti.txt"
    )
print(
    f.readlines()
    )
# print(f.readline())
f.close()

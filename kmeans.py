dataset = [2, 3, 6, 8, 9, 12, 15, 18, 22]
m1 = int(input("Enter m1: "))
m2 = int(input("Enter m2: "))

avg1 = 0
avg2 = 0
p1 = 0
p2 = 0

while m1 != p1 and m2 != p2:
    j = 1
    k1 = []
    k2 = []
    for i in dataset:
        if abs(i - m1) < abs(i - m2):
            k1.append(i)
        else:
            k2.append(i)

    avg1 = sum(k1) / len(k1)
    avg2 = sum(k2) / len(k2)
    print(f"k{j}    k{j+1}")
    print(k1, k2)
    p1 = m1
    p2 = m2
    m1 = avg1
    m2 = avg2

print(f"m1 = {m1} , m2 = {m2}")
# Enter m1: 8
# Enter m2: 9
# k1    k2
# [2, 3, 6, 8] [9, 12, 15, 18, 22]
# k1    k2
# [2, 3, 6, 8, 9] [12, 15, 18, 22]
# k1    k2
# [2, 3, 6, 8, 9] [12, 15, 18, 22]
# m1 = 5.6 , m2 = 16.75

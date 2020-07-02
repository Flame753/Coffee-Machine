A = int(input())
B = int(input())
H = int(input())

if H < A:
    print("Deficiency")
elif H > B:
    print("Excess")
elif A <= H <= B:
    print("Normal")

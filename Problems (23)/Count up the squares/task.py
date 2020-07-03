# put your python code here
norm_sum = 0
squr_sum = 0
while True:
    num = int(input())
    norm_sum += num
    squr_sum += (num**2)
    if norm_sum == 0:
        print(squr_sum)
        break

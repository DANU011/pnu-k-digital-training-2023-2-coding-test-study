n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

a_lst.sort()
b_lst.sort(reverse=True)

s=0
for i in range(n):
    s += a_lst[i]*b_lst[i]

print(s)

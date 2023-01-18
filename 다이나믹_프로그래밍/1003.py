# 다이나믹 프로그래밍에 대한 이론적인 이해는 됐는데 막상 짜려고 하니까 엄두가 안남..
# 다시 차근 차근 처음부터 이해하는 시간이 필요한 듯 하다...ㅠㅠ
# 너무 어려워잉 ㅠㅠ

t = int(input())
zero = [1,0,1]
one = [0,1,1]

def fibo(n) : #[0,1,3]
    if len(zero) <= n :
        for i in range(len(zero), n+1) :
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])

for i in range(t) : #[3]
    a = int(input()) #[0,1,3]
    fibo(a)

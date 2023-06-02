def solution(code):
    for start in reversed(range(len(code))):
        key = code[start:]

        if len(key) == 1:
            dp[key] =1
        elif int(key) in range(10, 27):
            dp[key] = 2

        else:
            if int(key[0:2]) in range(10, 27):
                dp[key] = dp[key[1:]] + dp[key[2:]]
            else:
                dp[key] = dp[key[1:]]
    return dp[code] % 1000000

code = input()
code = code.replace('10', ',').replace('20', ',')

if '0' in code:
    print(0)
else:
    code=code.split(',')
    dp = {}
    for num in code:
        if num != '':
            solution(num)

    ans = 1
    for num in code:
        if num != '':
            ans *= dp[num]
    print(ans % 1000000)

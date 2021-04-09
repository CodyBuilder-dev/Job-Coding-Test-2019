"""
제목 : 이진 변환 반복하기

아이디어 : 이진 변환의 결과는 아래와 같다
- 1이 N개 -> N의 2진수 표현
    - 1이 1개인 경우는 무한반복
    - 1이 N개인데 값도 N개인 수가 있나?? -> 987,654,321까지는 없다
- 결국 필요로 하는 것은 제거된 0의 개수와 변환 회수
    - 이거 과거와 동일한 결과가 계속 반복되므로, 메모이제이션 적용 가능

구현 : 2차원 DP
- dp테이블 생성
    - 1부터 시작해서, [필요한 변환의 횟수,지워지는 0의 개수] 
    - 1의 개수 n = 2(11)이라고 하자
    - 이진수로 바꾸면 10
    - 0제거 개수는 dp[1][1] +1 = 0+1
    - 변환회수는 dp[1][0] +1 = 0+1
    
    - 1의개수 n = 3(111)이라고 하자
    - 이진수로 바꾸면 11
    - dp[3][1] = dp[2][1] +0
    = dp[3][0] = dp[2][0]+1

    - n = 4 (1111) 라고 하자
    - 이진수로 바꾸면 100
    - dp[4][1] = dp[1][1] +2
    - dp[4][0] = d][1[]0]
- dp테입르 탐색
    - 처음에만 제거된 0의 개수를 기록한다. 
    - 1의 개수를 세서, dp테이블에서 찾는다

"""

def solution(s):
    dp = [[0,0] for i in range(150001)]
    for i in range(2,150001):
        bin_str = bin(i)[2:]
        next = bin_str.count('1')
        deleted = bin_str.count('0')
        dp[i][0] = dp[next][0] +1 # 필요한 변환 횟수
        dp[i][1] = dp[next][1] +deleted # 제거되는 0의 개수
    

    next = s.count("1")
    deleted = s.count("0")

    return dp[next][0]+1, dp[next][1]+deleted

# 테스트 케이스
print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
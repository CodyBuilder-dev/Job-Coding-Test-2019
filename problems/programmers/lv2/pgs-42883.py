"""
제목 : 큰 수 만들기

접근법 1: 브루트 포스
1. 2개를 임의로 뽑는다( 100만C2 = 시간 초과!)
2. 리스트에 보관한다
3. 최종적으로 보관된 리스트를 정렬 
-> number의 자리수가 10^6이므로, 완전탐색을 쓰지 말라는 소리다

접근법 2 : 그리디
- 길이가 n인데 k개를 제거한다 -> n-k개를 뽑는다
- 아래의 순서대로 숫자를 뽑는다
    - 제일 큰 수를 찾아 뽑는다
    - 해당 수 앞의 수와 뒤의 수 개수를 본다
        - 뒤에 충분한 수가 있는 경우, 해당 수 뒷부분에서 다음 큰수를 찾는다
        - 뒤에 충분한 수가 없는 경우 해당 뒤의 수를 모두 포함시킨 후 앞부분에서 다음으로 큰 수를 찾는다

구현 : 숫자와 인덱스를 저장한 tuple로 구현



"""

def solution(number, k):
    a
    return a

# 테스트케이스
print(solution("1924",2),"94")
print(solution("1231234", 3),"3234")
print(solution("4177252841",4),"775841")
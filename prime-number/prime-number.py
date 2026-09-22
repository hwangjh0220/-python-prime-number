# prime-number.py - 소수 구하기 프로그램 기본 틀
print("1부터 100 사이의 소수를 구합니다.")
for num in range(1, 101):
    is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
    if is_prime:
        print(num, end=" ")
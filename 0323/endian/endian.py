import sys
print(sys.byteorder)
a = 1234 # 정수 12를 8bit little endian으로 표기하기
n = int.to_bytes(a, byteorder='little', length=4)
print(n)
# 정수 12를 8bit big endian으로 표기하기
n = int.to_bytes(a, byteorder='big', length=4)
print(n)
print(int.from_bytes(n, byteorder='big'))   # 다시 읽기
print(int.from_bytes(n, byteorder='little')) # little로 읽기

# 10진수 2진수로 변환하기
num = 10; binary = ''
while num != 0:
    binary = str(num % 2) + binary
    num = num // 2
print(binary)   # 타 진수는 2대신 해당 수

# 10진수로 재변환
result = 0
for i in range(len(binary)):
    result = result * 2 + int(binary[i])
print(result)

# 함수로 2진법 변환
no = 10
binary = bin(no); print(binary)
octal = oct(no); print(octal.replace('0o', '')) # 숫자앞 제거
hexademical = hex(no); print(hexademical.replace('0x', ''))

# 타진법을 10진법으로 변환
dec = int(binary, base=2) # 기본값 base =10을 2로 변환
text = '0b1010'; print(int(text, base=2)) # '0b' 없이 '1010'도 가능
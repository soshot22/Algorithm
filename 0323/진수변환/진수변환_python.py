num = 10


# 2진법 변환
binary = bin(num)
print(binary.replace('0b', ''))

# 8진법 변환
octal = oct(num)
print(octal.replace('0o', ''))

# 16진법 변환
hexademical = hex(num)
print(hexademical.replace('0x', ''))


# 2진법을 10진법으로 변환...?
dec = int(binary, base=2)
print(dec)

text = '0b1010'
print(int(text, base=2))

text = '1010'
print(int(text, base=2))
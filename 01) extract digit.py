# Extract digits in list
def extract_digit( num)->li
    digits =[]
    while num>0:
        digit=num %10
        digits.append(digit
        num=num//10
    return digits[::-1]

print(extract_digit(19238))
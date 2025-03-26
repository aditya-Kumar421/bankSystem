# Convert Doller to Indian Currency

n = float(input("Enter the amount in dollars: "))
    
str_n = str(n)
is_decimal = False
last_part = ""
first_part = ""

for char in str_n:
    if char == '.' or is_decimal:
        last_part += char
        is_decimal = True
    else:
        first_part += char

if len(first_part) > 3:
    first_part = first_part[::-1]
    temp = ""
    for i in range(len(first_part)):
        temp += first_part[i]
        if i % 2 == 0 and i != 0 and i != len(first_part) - 1:
            temp += ','
    first_part = temp[::-1]

first_part += last_part
print(f"Amount in Indian currency: Rs. {first_part}")
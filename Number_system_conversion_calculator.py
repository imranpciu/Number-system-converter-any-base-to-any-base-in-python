def decimal_to_any_base(nums, base):
    hexa_dict= {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    res = ''
    num = int(nums)
    while(num!=0):
        remainder = num % base
        num= num // base
        if remainder in hexa_dict:
            remainder = hexa_dict[remainder]
        res = str(remainder) + res
    return res

def any_base_to_decimal(nums, base):
    hexa_dict= {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    num = str(nums)
    i = 1
    cal = 0
    for bit in num:
        if bit in hexa_dict:
            bit = hexa_dict[bit]
        equation = int(bit) * base**(len(num) - i)
        cal = cal + equation 
        i +=1 
    return cal


input_num = (input("Enter a number: "))
base = int(input("Enter the base of this number: "))
convert_into = int(input("Convert into to desier base number: ")) 

convert_to_decimal = any_base_to_decimal(input_num, base)
convert_to_desier = decimal_to_any_base(convert_to_decimal, convert_into)

print(f"the conversion result of {base} to {convert_into} is: " + convert_to_desier)

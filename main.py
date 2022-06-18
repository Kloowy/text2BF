def divisorsGen(n):
    list = []
    for i in range(1, v+1):
        if n % i == 0 : list.append(i)
    return list

def text2bf(text):
    bf_code = ""
    for sym in text:
        num = ord(sym)
        print(str(num) + " = " + sym)
        code_block = ""
        for i in range(255):
            divisors = divisorGen(256-i)
            for divider in divisors:
                coeff = int((255/divider)//num+(((255/divider)//num)-1)%2)
                if 255//coeff - num >= 0:
                    sign = "-"
                else:
                    sign = "+"
                if len("-"*i + "[>" + "+"*divider + "<" + str("-"*coeff) + "]>" + sign*abs(255//coeff-num) + ".>")<len(code_block) or code_block == "":
                    code_block = "-[>" + "+"*divider + "<" + str("-"*coeff) + "]>" + sign*abs(255//coeff-num) + ".>"
        bf_code += code_block

    return bf_code

if __name__ == '__main__':
    while True:
        text = input()
        print(text2bf(text))

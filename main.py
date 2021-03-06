def divisorsGen(n):
    list=[]
    for i in range(1,n+1):
        if n%i==0:list.append(i)
    return list
def text2bf(text):
    bf_code=""
    for sym in text:
        num=ord(sym);
        if len("+"*num)>len("-"*(256-num)):code_block="+"*num+".>"
        else:code_block="-"*(256-num)+".>"
        for fs in ["-", "+"]:
            for i in range(1, 255):
                divisors=divisorsGen(256-i)
                for divider in divisors:
                    coeff=int((255/divider)//num+(((255/divider)//num)-1)%2)
                    if 255//coeff-num>=0:sign="-"
                    else:sign="+"
                    if len("+"*divider)<=len("-"*(256-divider)):seg="+"*divider
                    else:seg="-"*(256-divider)
                    if len("+"*coeff)<=len("-"*(256-coeff)):seg2="+"*coeff
                    else:seg2="-"*(256-coeff)
                    if len(fs*i+"[>"+seg+"<"+seg2+"]>"+sign*abs(255//coeff-num)+".>")<len(code_block):code_block=fs*i+"[>"+"+"*divider+"<"+str("-"*coeff)+"]>"+sign*abs(255//coeff-num)+".>"
        bf_code+=code_block
    return bf_code
if __name__=='__main__':
    while True:text=input();print(text2bf(text))

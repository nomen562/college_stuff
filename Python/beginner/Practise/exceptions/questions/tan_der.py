import re


def diff(st):
    if '^' not in st:
        if st == 'tan(x)':
            return 'sec^2(x)'
        if st == 'sin(x)':
            return 'cos(x)'
        if st == 'cos(x)':
            return '-sin(x)'
        if st == 'sec(x)':
            return 'sec(x)*tan(x)'
    else:
        n = int(st[st.index('^')+1])
        carrot_n = '^'+str(n-1) if n > 2 else ''
        t = str(n)+f'*{st[0:3]}{carrot_n}(x)'
        ex = '(x)'
        t += f'*{diff(st[0:3]+ex)}'


def d_tanx(n):
    d = '2*sec^2(x)*tan(x)'

    if n == 1:
        return 'sec^2(x)'
    if n == 2:
        return d
    if n > 2:
        terms = re.findall(r"\b[a-z] +\^?\d?\(x\)|\d+\b", d)
        for x in terms:
            if x.isnumeric():

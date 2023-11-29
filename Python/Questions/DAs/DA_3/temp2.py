import re


def d_sec(trig):
    if trig == "sec(x)":
        return "sec(x)*tan(x)"


def d_tan(trig):

    if trig == "tan(x)":
        return "sec^2(x)"
    if trig == "sec^2(x)":
        return "2*sec^2(x)*tan(x)"
    else:
        match = re.search("\d", trig)
        s = int(trig[match.start()])-1  
        return f"{s+1}*{re.search}"


print(d_tan("sec^3(x)"))

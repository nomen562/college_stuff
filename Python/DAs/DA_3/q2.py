all = {'s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10'}
Sci_pass = {'s1', 's2', 's3', 's5', 's7'}
Sci_fail = {'s4', 's6', 's8', 's9', 's10'}
Math_80_plus = {'s3', 's5', 's9', 's10'}
Maths_below_60 = {'s1', 's2', 's7', 's8'}
english_70_plus = {'s3', 's4', 's9'}
English_below_40 = {'s1', 's2'}


def fun1():
    return (Sci_fail & Math_80_plus)


def fun2():
    return (Sci_pass | English_below_40)


def fun3():
    return (((all - Math_80_plus) & (all-Maths_below_60)) & (all - English_below_40))


print(f"The students who failed in science and got 80 + in maths: {fun1()}")
print(
    f"The students who passed in science or got below 40 in English: {fun2()}")
print(
    f"The students who got marks from 60 to 80 in maths and above 40 in English: {fun3()}")

l = {}
per = {}
f = open("/home/malik/Dev/college_stuff/Python/Questions/DAs/DA_4/marks.txt","r")
for line in f:
    n, a, b, c = line.split()
    a, b, c = int(a), int(b), int(c)
    l[n] = (a, b, c)
print(l)
def class_average():
    e_av = s_av = m_av = 0
    for key in l:
        per[key] = (l[key][0] + l[key][1] + l[key][2])/3
        e_av += l[key][0]/5
        s_av += l[key][1]/5
        m_av += l[key][2]/5
    return e_av,s_av,m_av
ca = class_average()
f.close()
perc = dict(sorted(per.items(), key=lambda x:x[1], reverse=True))
print(perc)
def file_write():
    f1 = open("/home/malik/Dev/college_stuff/Python/Questions/DAs/DA_4/class_average.txt","w")
    f1.write(f"Class average in English is {ca[0]}\n")
    f1.write(f"Class average in Science is {ca[1]}\n")
    f1.write(f"Class average in Maths is {ca[2]}\n")
    f1.close()
    f2 = open("/home/malik/Dev/college_stuff/Python/Questions/DAs/DA_4/percentage.txt","w")
    for key in perc:
        f2.write(f"Average of {key} is {perc[key]}\n")
    f2.close()
file_write()
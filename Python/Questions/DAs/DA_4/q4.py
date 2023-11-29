import math
import os

def trig():
    a = float(input('Enter a number for a'))
    b = float(input('Enter another for b'))
    c=1
    
    # pi = math.pi  # Uncomment this line if you want to use pi as one of the inputs
    s1 = math.sin(a + b)
    s2 = math.sin(a - b)
    s3 = math.sin(a)
    s4 = math.sin(b)
    c1 = math.cos(a + b)
    c2 = math.cos(a - b)
    c3 = math.cos(a)
    c4 = math.cos(b)
    t1 = math.tan(a + b)
    t2 = math.tan(a - b)
    t3 = math.tan(a)
    t4 = math.tan(b)
    if math.isclose(s1, s3 * c4 + s4 * c3):
        file.write(f'identity {c} is valid\n')
    c+=1
    if math.isclose(s2, s3 * c4 - s4 * c3):
        file.write(f'identity {c} is valid\n')
    c+=1
    if math.isclose(c1, c3 * c4 - s4 * s3):
        file.write(f'identity {c} is valid\n')
    c+=1
    if math.isclose(c2, c3 * c4 + s4 * s3):
        file.write(f'identity {c} is valid\n')
    c+=1
    if math.isclose(t1, (t3 + t4) / (1 - t3 * t4)):
        file.write(f'identity {c} is valid\n')
    c+=1
    if math.isclose(t2, (t3 - t4) / (1 + t3 * t4)):
        file.write(f'identity {c} is valid')

def log():
    x = int(input('enter x>'))
    y = int(input('enter y>'))
    b = int(input('enter base '))
    c=1
    i1 = math.log((x * y), b)
    i2 = math.log((x / y), b)
    i3 = math.log((x ** y), b)
    i4 = math.log((x ** (1 / y)), b)
    i5 = math.log(x, b)
    i6 = math.log(y, b)
    if math.isclose(i1, i5 + i6):
        file.write(f'identity {c} is valid\n')
    c+=1
    if math.isclose(i2, i5 - i6):
        file.write(f'identity {c} is valid\n')
    c+=1
    if math.isclose(i3, i5 * y):
        file.write(f'identity {c} is valid\n')
    c+=1
    if math.isclose(i4, i5 / y):
        file.write(f'identity {c} is valid')

if not os.path.exists("log_res"):
    os.mkdir("log_res")
    
if not os.path.exists("tri_res"):
    os.mkdir("tri_res")
    
os.chdir("/home/malik/Dev/college_stuff/Python/Questions/DAs/DA_4/log_res")
file = open("log_results.txt",'w') 
file.write("The results of the given logarithmic identites are as \n")
# file.close()
# file = open("log_results.txt",'a')
log()
file.close()
file = open("log_results.txt",'r')
x=file.read()
print(x)
file.close()

os.chdir("/home/malik/Dev/college_stuff/Python/Questions/DAs/DA_4/tri_res")
file = open("tri_results.txt",'w')
file.write("The results of the given logarithmic identites are as \n")
# file.close()
# file = open("tri_results.txt",'a')
trig()
file.close
file = open("tri_results.txt",'r')
x=file.read()
print(x)
file.close()
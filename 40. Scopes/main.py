#variable scope where a variable is visible and accessible
#scope resolution = (LEGB) Local -> Enclosed-> Global -> Built-in

def fn1():
    a = 1
    print(a)
def fn2():
    b = 2
    print(b)

fn1()
fn2() #variable scope


def fn1():
    a = 1
    print(b)
def fn2():
    b = 2
    print(a)
# will raise error - bcz they are not anywhere in legb

a = 2
def fn1():
    a = 1
    print(a)
def fn2():
    print(a)

fn1() #found in local
fn2() # no local, no enclosed, so go to global


from math import pi

def fn1():
    print(pi)
def fn2():
    pi  = 3.14
    print(pi)

fn1() #no local, no enclosed, no global, built in
fn2() #local
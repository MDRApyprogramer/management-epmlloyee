# Management of workers and employees
print('hello')
print('wellcom')

# imports

import sqlite3
from tabulate import tabulate

# sql_تمامی فانکشن های مربوط به دیتابیس , با داک استرینگ مشخص شده
# connected sql
conn = sqlite3.connect('emp_sql.db')
c = conn.cursor()

def init():
    c.execute('''CREATE TABLE IF NOT EXISTS emps (
                fname TEXT,
                lname TEXT,
                pay INTEGER,
                job TEXT,
                bio TEXT
                )''')
    conn.commit()
try :
    c.execute('SELECT * FROM emps')
    print(tabulate(c.fetchall()))
except sqlite3.OperationalError:
    print('')
#defines

def add(fname,lname,job,pay : int,bio = None):

    'add sql'

    c.execute('INSERT INTO emps VALUES (:fname , :lname , :job , :pay ,:bio )' , {'fname' : fname , 'lname' : lname ,'job' : job , 'pay' : pay , 'bio' : bio})
    conn.commit()

def show_name(emp_name):

    'sql'
    'show first names'

    c.execute('SELECT * FROM emps WHERE fname = (:first_name)',{'first_name' : emp_name})
    print(tabulate(c.fetchall()))

def show_job(emp_job):

    'sql'
    'show jobs'

    c.execute('SELECT * FROM emps WHERE job = (:the_job)',{'the_job' : emp_job})
    print(tabulate(c.fetchall()))
    

def show_pay(emp_pay):

    'sql'
    'show pays'

    c.execute('SELECT * FROM emps WHERE pay = (:the_pay)',{'the_pay' : emp_pay})
    print(tabulate(c.fetchall()))

def show_lname(emp_name):

    'sql'
    'show last names'

    c.execute('SELECT * FROM emps WHERE lname = (:last_name)',{'last_name' : emp_name})
    
    print(tabulate(c.fetchall()))

def update_pay(pay : int , fname ,lname):

    'sql'

    c.execute('''UPDATE emp SET pay = :pay
    WHERE fname = :fname AND lname = :lname'''
    ,{'pay' : pay,'fname' : fname , 'lname' : lname})

def update_job(job , fname ,lname):

    'sql'

    c.execute('''UPDATE emp SET job = :job
    WHERE fname = :fname AND lname = :lname'''
    ,{'job' : job,'fname' : fname , 'lname' : lname})

def delet(fname , lname):
    c.execute('''DELETE FROM emps WHERE
     fname = :fname AND lname = :lname''',
     {'fname' : fname , 'lname' : lname})

def add_emp():
    fname = input('first name : ')
    lname = input('last name : ')
    pay = int(input('pay : '))
    job = input('job : ')
    bio = input('bio(voluntary) : ')
    global add
    add(fname,lname,pay,job,bio)

def show_emp():
    global show_pay , show_job , show_lname , show_name
    list1 = ['first name','last name','job','pay']
    print(list1)
    a = input('What should I show? ')

    if a == 'last name' :
        vriable = input('last name : ')
        show_lname(vriable)
    
    if a == 'first name' :
        vriable = input('first name : ')
        show_name(vriable)
    
    if a == 'job' :
        vriable = input('job : ')
        show_job(vriable)

    if a == 'pay' :
        vriable = input('pay : ')
        show_pay(vriable)

def update():
    list_update = ('update job','update pay')
    print(list_update)
    a = input('/')
    
    if a == 'update job' :
        first_name = input('first name ? ')
        last_name = input('last name ? ')
        job = input('new job ? ')

        update_job(job , first_name , last_name)

    elif a == 'update pay' :
        first_name = input('first name ? ')
        last_name = input('last name ? ')
        pay = input('new pay ? ')

        update_pay(pay , first_name , last_name)
    
    else :
        print('I did not understand what you meant')

def delet_emp():
    fname = input('first name : ')
    lname = input('last name : ')
    delet(fname , lname)

def add_emp():
    fname = input('first name : ')
    lname = input('last name : ')
    pay = int(input('pay : '))
    job = input('job : ')
    bio = input('bio(voluntary) : ')
    global add
    add(fname,lname,pay,job,bio)

def show_emp():
    global show_pay , show_job , show_lname , show_name
    list1 = ['first name','last name','job','pay']
    print(list1)
    a = input('What should I show? ')

    if a == 'last name' :
        vriable = input('last name : ')
        show_lname(vriable)
    
    if a == 'first name' :
        vriable = input('first name : ')
        show_name(vriable)
    
    if a == 'job' :
        vriable = input('job : ')
        show_job(vriable)

    if a == 'pay' :
        vriable = input('pay : ')
        show_pay(vriable)

def update():
    list_update = ('update job','update pay')
    print(list_update)
    a = input('/')
    
    if a == 'update job' :
        first_name = input('first name ? ')
        last_name = input('last name ? ')
        job = input('new job ? ')

        update_job(job , first_name , last_name)

    elif a == 'update pay' :
        first_name = input('first name ? ')
        last_name = input('last name ? ')
        pay = input('new pay ? ')

        update_pay(pay , first_name , last_name)
    
    else :
        print('I did not understand what you meant')

def delet_emp():
    fname = input('first name : ')
    lname = input('last name : ')
    delet(fname , lname)

def ing():
    global add_emp , show_emp
    
    list_menu = ['add employee','show employee','update employee','delete employee','exit']
    
    print('******************************************************')

    for a in list_menu :
        print(a, end = ' /\ ')

    print('******************************************************')

    menu = input('/')

    if menu == 'add employee' or menu == 'a':
        add_emp()
    
    elif menu == 'update employee' or menu == 'u':
        update()

    elif menu == 'show employee' or menu == 's':
        show_emp()

    elif menu == 'delete employee' or menu == 'd':
        delet_emp()

    elif menu == 'exit' or menu == 'e':
        exit()

    else :
        print('I did not understand what you meant')

while True :
    init()
    print('please wait')
    ing()
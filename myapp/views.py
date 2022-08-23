from ast import NotIn
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import emp_table
import pymysql
import mysql.connector as mysql
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def index(request):
    conn = pymysql.connect(host='127.0.0.1', user='root',
                           password='test', db='myapp_data')
    cur = conn.cursor()
    l = []
    cur.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema = 'myapp_data'")
    for table in [tables[0] for tables in cur.fetchall()]:
        if table.startswith('myapp'):
            l.append(table)
    context = {'tables': l}
    if request.method == 'POST':
        return l
    return render(request, 'home.html', context)


def home1(request):
    # print(request.POST)
    db = mysql.connect(host='127.0.0.1', user='root',
                       password='test', db='myapp_data')
    cursor = db.cursor()
    try:
        global table_name
        table_name = request.POST['q']
        print("asdf" + " " + table_name)
    except:
        pass 
    cursor.execute("SELECT * FROM {};".format(table_name))
    records = cursor.fetchall()
    print(records)
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    print(field_names)
    tables = index(request)
    print(tables)
    context1 = {'employe': records,
                'emp_header': field_names, 'tables': tables}

    return render(request, 'home.html', context1)

def home2(request):
    db = mysql.connect(host='127.0.0.1', user='root',
                       password='test', db='myapp_data')
    cursor = db.cursor()
    table_name = table_name_for_del
    cursor.execute("SELECT * FROM {};".format(table_name))
    records = cursor.fetchall()
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    tables = index(request)
    print(tables)
    context1 = {'employe': records,
                'emp_header': field_names, 'tables': tables}
    return context1

def delete(request):
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        password="test",
        db="myapp_data"
    )
    l = request.POST['c'].split(", ")
    dele = l[0][1:]
    cursor = db.cursor()
    print(table_name)
    global table_name_for_del
    table_name_for_del = table_name
    cursor.execute("DELETE FROM {} WHERE id = '{}'".format(
        table_name, dele))
    db.commit()
    context1=home2(request)
    return render(request, 'home.html', context1)


def edit(request):
    # print(request.POST["b"]
    return render(request, 'edit.html', {})


def update(request):
    print(request.POST)
    db = mysql.connect(
        host="127.0.0.1",
        user="root",
        password="test",
        database="myapp_data"
    )
    cursor = db.cursor()
    if request.POST['emp_id'] != '':
        cursor.execute("UPDATE {} SET emp_id = {} WHERE id = '{}'".format(
            table_name, request.POST['emp_id'], request.POST['id']))
        # print(request.POST['emp_id'])
    if request.POST['emp_first_name'] != '':
        print(table_name)
        cursor.execute("UPDATE {} SET emp_first_name = '{}' WHERE id = '{}'".format(
            table_name, request.POST['emp_first_name'], request.POST['id']))
        #print(request.POST['emp_first_name']+" asdf")
    if request.POST['emp_last_name'] != '':
        cursor.execute("UPDATE {} SET emp_last_name = '{}' WHERE id = '{}'".format(
            table_name, request.POST['emp_last_name'], request.POST['id']))

    db.commit()
    return redirect("/polls")


from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from reg_info.models import RegInfo

def IndexPage(request):
    data={
        'title':'Interview Blog App',
    }
    return render(request,"index.html",data)

def Register(request):
    data = {}
    try:
        if request.method=="POST":
            if request.POST.get('fname')=="":
                return render(request, "register.html", {'error':True})
            fname = request.POST.get('firstname')

            if request.POST.get('lname')=="":
                return render(request, "register.html", {'error':True})
            lname = request.POST.get('lastname')

            if request.POST.get('email')=="":
                return render(request, "register.html", {'error':True})
            email = request.POST.get('email')

            if request.POST.get('pwd')=="":
                return render(request, "register.html", {'error':True})
            pwd = request.POST.get('password')

            if request.POST.get('cpwd')=="":
                return render(request, "register.html", {'error':True})
            cpwd = request.POST.get('conf_password')

            if request.POST.get('sel_deg')=="":
                return render(request, "register.html", {'error':True})
            sel_deg = request.POST.get('sel_deg')

            if request.POST.get('pos')=="":
                return render(request, "register.html", {'error':True})
            pos = request.POST.get('pos')

            if request.POST.get('grad_year')=="":
                return render(request, "register.html", {'error':True})
            grad_year = request.POST.get('grad_year')

            data = {
                'title': 'Interview Blog App',
                'fname': fname,
                'lname': lname,
                'email': email,
                'pwd': pwd,
                'cpwd': cpwd,
                'sel_deg': sel_deg,
                'pos': pos,
                'grad_year': grad_year
            }
            url = "/register/home"

            return redirect(url)

    except:
        pass

    return render(request,"register.html",data)

def Reg_Info(request):
    n = ''
    if request.method=="POST":
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        cpwd = request.POST.get('conf_password')
        sel_deg = request.POST.get('sel_deg')
        pos = request.POST.get('pos')
        grad_year = request.POST.get('grad_year')
        rg = RegInfo(firstname=fname,lastname=lname,email=email,password=pwd,conf_password=cpwd,sel_deg=sel_deg,pos=pos,grad_year=grad_year)
        rg.save()
        n = 'Data Registered'

    return render(request,"/register/home",{'n':n})

def Login(request):
    data = {}
    try:
        if request.method=="POST":
            if request.POST.get('email')=="":
                return render(request, "login.html", {'error':True})
            email = request.POST.get('email')

            if request.POST.get('password')=="":
                return render(request, "login.html", {'error':True})
            pwd = request.POST.get('password')

            data = {
                'title': 'Interview Blog App',
                'email': email,
                'pwd': pwd,
            }
            url = "/login/home"

            return redirect(url)

    except:
        pass

    return render(request,"login.html",data)

def Home(request):
    data={
        'title':'Interview Blog App',
    }
    return render(request,"home.html",data)

def Explore(request):
    data={
        'title':'Interview Blog App',
    }
    return render(request,"explore.html",data)

def Add_New_Exp(request):
    data={
        'title':'Interview Blog App',
    }
    return render(request,"add_new_exp.html",data)

def My_Exp(request):
    data={
        'title':'Interview Blog App',
    }
    return render(request,"my_exp.html",data)

def Bookmarks(request):
    data={
        'title':'Interview Blog App',
    }
    return render(request,"bookmarks.html",data)


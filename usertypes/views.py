from django.shortcuts import render,HttpResponse
# from .serializers import *
from .models import *
def home(request):
    return render(request,"index.html")

def main(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        picture=request.FILES.get('picture')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        address=request.POST.get('address')
        type=request.POST.get('type')
        if cpassword==password:
            obj=User.objects.filter(username=uname).first()
            if obj:
                return HttpResponse("Username Already Exists")
            serializer=User(firstname=fname,lastname=lname,picture=picture,username=uname,email=email,password=password,address=address,type=type)
            serializer.save()
            return render(request,"login.html")
        return HttpResponse("Password Didn't Match")
    
def new(request):
    uname=request.GET.get('uname')
    password=request.GET.get('password')
    obj=User.objects.filter(username=uname).first()
    if not obj:
        return HttpResponse("User Not Found!!")
    obj1=User.objects.filter(username=uname,password=password).first()
    if obj1:
        fname=obj1.firstname
        lname=obj1.lastname
        email=obj1.email
        address=obj1.address
        type=obj1.type
        url=str('https://logincheck-apmj.onrender.com'+obj1.picture.url)
        return render(request,"new.html",{'fname':fname,'lname':lname,'email':email,'address':address,'type':type,'url':url})
    else:
        return HttpResponse("Invalid Password!!")
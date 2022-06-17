from collections import UserDict
from urllib import response
from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from .forms import Register
from django.contrib.auth.decorators import login_required
from .models import Data
import pdfkit
from django.template import loader
import io


import os, sys, subprocess, platform

# Create your views here.
def index(request):
    data = None
    if request.user.is_authenticated:
        current_user = request.user
        try:
            data = Data.objects.get(username = current_user.username)
        except Data.DoesNotExist:
            data = None
        
    if request.method == "POST":
        username = request.POST.get('username', "")
        name = request.POST.get('name', "")
        intro = request.POST.get('intro' "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "0")
        school = request.POST.get('school',"")
        branch = request.POST.get('branch',"")
        college = request.POST.get('college', "")
        address = request.POST.get('address', "")
        codeforces = request.POST.get('codeforces', "")
        codechef = request.POST.get('codechef', "")
        leetcode = request.POST.get('leetcode', "")
        github = request.POST.get('github', "")
        projects = request.POST.get('projects', "")
        skills = request.POST.get('skills',"")
        achievement = request.POST.get('achievement', "")
        experience = request.POST.get('experience', "")
        # print(school)
        # print(branch)
        if data is None:
            ins = Data(username = username, name = name, intro = intro, email = email, phone = phone, school = school, branch = branch, college = college, address = address, codeforces = codeforces, codechef = codechef, leetcode = leetcode, github = github, projects = projects, skills = skills, achievement = achievement, experience = experience)
            ins.save() 
        else: 
            data.username = username
            data.name = name
            data.intro = intro
            data.email = email
            data.phone = phone
            data.school = school
            data.college = college
            data.branch = branch
            data.address = address
            data.codeforces = codeforces
            data.codechef = codechef
            data.leetcode = leetcode
            data.github = github
            data.projects = projects
            data.skills = skills
            data.achievement = achievement
            data.experience = experience
            data.save() 
    return render(request,'index.html',{'data':data})

@login_required
def dark(request):
    current_user = request.user
    user_id = current_user.id
    try:
        data = Data.objects.get(username = current_user.username)
    except Data.DoesNotExist:
        data = None
    print(user_id)
    print(data)
    template = loader.get_template('dark.html')
    html = template.render({'data':data})
    options = {
        'page-size':'Letter',
        'encoding' : "UTF-8"
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type = 'application/pdf')
    response['Content-Diposition'] = 'attachment'
    filename = "resume.pdf"
    return response
    # return render(request,'generate.html',{'data':data})

def light(request):
    current_user = request.user
    user_id = current_user.id
    try:
        data = Data.objects.get(username = current_user.username)
    except Data.DoesNotExist:
        data = None
    print(user_id)
    print(data)
    template = loader.get_template('light.html')
    html = template.render({'data':data})
    options = {
        'page-size':'Letter',
        'encoding' : "UTF-8"
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type = 'application/pdf')
    response['Content-Diposition'] = 'attachment'
    filename = "resume.pdf"
    return response

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username} your account is created.... Please login to continue')
            return redirect('index')
    else:
        form = Register()
    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    current_user = request.user
    try:
        data = Data.objects.get(username = current_user.username)
    except Data.DoesNotExist:
        data = None
    return render(request,'profile.html',{'data':data})

def choose(request):
    return render(request,'choose.html')



if platform.system() == "Windows":
        pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
else:
        os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable) 
        WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], 
            stdout=subprocess.PIPE).communicate()[0].strip()
        pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)

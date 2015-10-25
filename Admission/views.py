from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Students,chat
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
# Create your views here.

def institute(request):
	return render(request,'Admission/institute.html')

def index(request):
	return render(request,'Admission/index.html')

def register(request):
	return render(request,'Admission/register.html')

def register_user(request):
	if request.method == "POST":
		user = request.POST['E']
		u = Students.objects.filter(email=user)
		if len(u) == 0:
			u = Students()
			u.Enrollment = request.POST['enroll']
			u.age = request.POST['D']
			u.name = request.POST['F']
			u.email = request.POST['E']
			u.password = request.POST['P']
			u.contact = request.POST['C']
			u.save()
			return HttpResponseRedirect(reverse('Admission:home_page',args=(u.id,)))
		else:
			return HttpResponseRedirect(reverse('Admission:register'))

def login(request):
	if request.method == "POST":
		user = request.POST['E']
		u = Students.objects.get(email=user)
		if u != None:
			if u.password == request.POST['P']:
				return HttpResponseRedirect(reverse('Admission:home_page',args=(u.id,)))
			else:
				return HttpResponseRedirect(reverse('Admission:register'))
		else:
			return HttpResponseRedirect(reverse('Admission:register'))

def home_page(request,id):
	u = get_object_or_404(Students,pk=id)
	return render(request,'Admission/home_page.html',{'user':u})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('Admission:register'))

def update(request,id):
	u = get_object_or_404(Students,pk=id)
	return render(request,'Admission/update.html',{'user':u})

def update_user(request,id):
	if request.method == "POST":
		user = Students.objects.get(pk=id)
		if len(request.POST['F']) != 0:
			user.name = request.POST['F']
		if len(request.POST['E']) != 0:
			user.email = request.POST['E']
		if len(request.POST['P']) != 0:
			user.password = request.POST['P']
		if len(request.POST['D']) != 0:
			user.age = request.POST['D']
		if len(request.POST['C']) != 0:
			user.contact = request.POST['C']
		user.save();
	u = Students.objects.get(pk=id)
	return HttpResponseRedirect(reverse('Admission:home_page',args=(u.id,)))

def update_profile(request,id):
	if request.method == "POST":
		user = Students.objects.get(pk=id);
		user.avatar = request.POST.get['file1']
		user.save();
	cloudinary.uploader.upload('/media/shishir/1F793FC47EA87EC1/CollegeAdmission/Admission/static/Admission/profiles/'+request.POST['file1'])
	u = Students.objects.get(pk=id)
	return HttpResponseRedirect(reverse('Admission:home_page',args=(u.id,)))

def message(request,ids):
	if request.method == "POST":
		sender = Students.objects.get(pk=ids)
		receiver = get_object_or_404(Students,email=request.POST['E'])
		u = chat()
		u.sender = sender.name
		u.receiver = receiver.name
		u.senderemail = sender.email
		u.receiveremail = receiver.email
		u.message = request.POST['M']
		u.save()
		return HttpResponseRedirect(reverse('Admission:messages',args=(sender.id,)))

def messages(request,id):
	u = Students.objects.get(pk=id)
	u1 = chat.objects.all()
	u2 = Students.objects.all()
	return render(request,'Admission/messages.html',{'user':u,'chat':u1,'friends':u2})
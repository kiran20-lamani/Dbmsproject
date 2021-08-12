from django.shortcuts import render,redirect
from hospital.forms import instrumentsform
from hospital.forms import departmentsform
from hospital.forms import contractsform
from hospital.forms import orderform
from hospital.forms import stockform
from hospital.models import instruments
from hospital.models import departments
from hospital.models import contracts
from hospital.models import order
from hospital.models import stock
from django.http import HttpResponse


# Create your views here.
def ins(request):
	if request.method == "POST":
		form = instrumentsform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("/show")
			except:
				pass
	else:
		form= instrumentsform()
	return render(request,"instruments.html", {'form':form})

def show(request):
	instrumenti= instruments.objects.all()
	return render(request,"show.html",{'instrumenti':instrumenti})

def edit(request, inst_id):
	insti= instruments.objects.get(inst_id=inst_id)
	return render(request,"edit.html",{'insti':insti})

def update(request, inst_id):
	insti= instruments.objects.get(inst_id=inst_id)
	form= instrumentsform(request.POST, instance= insti)
	if form.is_valid():
		form.save()
		return redirect('/show')
	return render(request,"edit.html",{'insti':insti})
	
def delete(request, inst_id):
	insti= instruments.objects.get(inst_id=inst_id)
	insti.delete()
	return redirect("/show")


def dep(request):
	if request.method == "POST":
		form = departmentsform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("/show1")
			except:
				pass
	else:
		form= departmentsform()
	return render(request,"departments.html", {'form':form})

def show1(request):
	departmenti= departments.objects.all()
	return render(request,"show1.html",{'departmenti':departmenti})

def edit1(request,dept_id):
	depti= departments.objects.get(dept_id=dept_id)
	return render(request,"edit1.html",{'depti':depti})
def update1(request,dept_id):
	depti= departments.objects.get(dept_id=dept_id)
	form= departmentsform(request.POST, instance= depti)
	if form.is_valid():
		form.save()
		return redirect('/show1')
	return render(request,"edit1.html",{'depti':depti})
def delete1(request, dept_id):
	depti= departments.objects.get(dept_id=dept_id)
	depti.delete()
	return redirect("/show1")


def login_form(request):
	return render(request, 'login_register.html')

def submit_form(request):
	username= request.GET['username']
	password= request.GET['password']
	if username == "Akmsinv" and password == "Akms@2020":
		return render(request, 'main.html')
	else:
		return HttpResponse('Invalid username or password')

def go(request):
	return render(request, 'inventory_main.html')

def invoice(request):
	return render(request,'invoice.html')

def main(request):
	return render(request, 'main.html')

def log(request):
	return render(request, 'login_register.html')

def con(request):
	if request.method == "POST":
		form = contractsform(request.POST)
		if form.is_valid():  
			try:
				form.save()
				return redirect("/show2")
			except:
				pass
	else:
		form= contractsform()
	return render(request,"contracts.html", {'form':form})

def show2(request):
	contracti= contracts.objects.all()
	return render(request,"show2.html",{'contracti':contracti})

def edit2(request,con_id):
	coni= contracts.objects.get(con_id=con_id)
	return render(request,"edit2.html",{'coni':coni})

def delete2(request,con_id):
	coni= contracts.objects.get(con_id=con_id)
	coni.delete()
	return redirect("/show2")


def ord(request):
	if request.method == "POST":
		form = orderform(request.POST)
		if form.is_valid():  
			try:
				form.save()
				return redirect("/show3")
			except:
				pass
	else:
		form= orderform()
	return render(request,"orders.html", {'form':form})

def show3(request):
	orderi= order.objects.all()
	return render(request,"show3.html",{'orderi':orderi})

def delete3(request,ord_id):
	ordi= order.objects.get(ord_id=ord_id)
	ordi.delete()
	return redirect("/show3")


def sto(request):
	if request.method == "POST":
		form = stockform(request.POST)
		if form.is_valid():  
			try:
				form.save()
				return redirect("/show4")
			except:
				pass
	else:
		form= stockform()
	return render(request,"stocks.html", {'form':form})

def show4(request):
	stocki= stock.objects.all()
	return render(request,"show4.html",{'stocki':stocki})

def delete4(request,st_id):
	stoi= stock.objects.get(st_id=st_id)
	stoi.delete()
	return redirect("/show4")
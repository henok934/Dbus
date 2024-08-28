from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser

"""
def home(request):
    return render(request, 'users/index.html')
def about(request):
    return render(request, 'users/about.html')
def offers(request):
    return render(request, 'users/cheeckrout.html')
def login(request):
    return render(request, 'users/login.html')

def profile(request):
    return render(request, 'users/profile.html')
def root(request):
    return render(request, 'users/checkroot.html')
def  users(request):
    return render(request, 'users/users.html')

def  comments(request):
    return render(request, 'users/comments.html')

def  routes(request):
    return render(request, 'users/routes.html')

def  selectbus(request):
    return render(request, 'users/route.html')
def  ticket(request):
    return render(request, 'users/ticket.html')

def  businsert(request):
    return render(request, 'users/Businsert.html')
def  comment(request):
    return render(request, 'users/comment.html')
def  get_ticket(request):
    return render(request, 'users/getticket.html')
def  worker(request):
    return render(request, 'users/worker.html')
def  route(request):
    return render(request, 'users/route.html')
def  city(request):
    if request.method == 'POST':
        depcity = request.POST['username']
        city = City.objects.create_user(
            depcity=depcity
        )
        city.save()
        login(request, user)
        return redirect('city')
    return render(request, 'users/city.html')
def  admin(request):
    return render(request, 'users/admin.html')
def  ad(request):
    return render(request, 'users/ad.html')
def  get_user(request):
    return render(request, 'users/checkuser.html')
def  get_route(request):
    return render(request, 'users/cheeckrout.html')
def  ticketinfo(request):
    return render(request, 'users/cheeckrouteee.html')
def  ticketinfo(request):
    return render(request, 'users/cheeckrouteee.html')
def Selectbus(request):
    return render(request, 'users/rootee.html')
def  Showtickets(request):
    return render(request, 'users/rootee.html')
def  book(request):
    return render(request, 'users/cheeckroutee.html')
def  Select(request):
    return render(request, 'users/roote.html')
def  details(request):
    return render(request, 'users/details.html')
def  admindelete(request):
    return render(request, 'users/admindelet.html')
def  delete(request):
    return render(request, 'users/admindelet.html')
def  delete(request):
    return render(request, 'users/admindelet.html')
def  routedelete(request):
    return render(request, 'user/routedelete.html')
def  workerdelete(request):
    return render(request, 'users/workerdelete.html')
def  busdelete(request):
    return render(request, 'users/busdelet.html')
def  deletebus(request):
    return render(request, 'users/busdelet.html')
def citydelete(request):
    return render(request, 'users/citydelet.html')
def commentdelete(request):
    return render(request, 'users/commentdelet.html')
def updatebus(request):
    return render(request, 'users/busupdate.html')
def changebus(request):
    return render(request, 'users/buschange.html')
def changebuses(request):
    return render(request, 'users/busschange.html')
"""

def home(request):
    return render(request, 'users/index.html')
def profile(request):
    return render(request, 'users/profile.html')
def about(request):
    return render(request, 'users/about.html')
def offers(request):
    return render(request, 'users/cheeckrout.html')
def login(request):
    return render(request, 'users/login.html')

def root(request):
    return render(request, 'users/checkroot.html')
def  users(request):
    return render(request, 'users/users.html')

def  comments(request):
    return render(request, 'users/comments.html')
def  routes(request):
    return render(request, 'users/routes.html')
def  selectbus(request):
    return render(request, 'users/route.html')
def ticket(request):
    return render(request, 'users/ticket.html')
def businsert(request):
    return render(request, 'users/Businsert.html')
def comment(request):
    return render(request, 'users/comment.html')
def get_ticket(request):
    return render(request, 'users/getticket.html')
def worker(request):
    return render(request, 'users/worker.html')
def route(request):
    return render(request, 'users/route.html')
def city(request):
    return render(request, 'users/city.html')
def admins(request):
    return render(request, 'users/admin.html')
def ad(request):
    return render(request, 'users/ad.html')
def get_user(request):
    return render(request, 'users/checkuser.html')
def get_route(request):
    return render(request, 'users/cheeckrout.html')
def ticketinfo(request):
    return render(request, 'users/cheeckrouteee.html')
def Selectbus(request):
    return render(request, 'users/rootee.html')
def book(request):
    return render(request, 'users/cheeckroutee.html')
def Select(request):
    return render(request, 'users/roote.html')
def details(request):
    return render(request, 'users/details.html')
def admindelete(request):
    return render(request, 'users/admindelet.html')
def delete(request):
    return render(request, 'users/admindelet.html')
def  routedelete(request):
    return render(request, 'user/routedelete.html')
def workerdelete(request):
    return render(request, 'users/workerdelete.html')
def busdelete(request):
    return render(request, 'users/busdelet.html')
def deletebus(request):
    return render(request, 'users/busdelet.html')
def citydelete(request):
    return render(request, 'users/citydelet.html')
def commentdelete(request):
    return render(request, 'users/commentdelet.html')
def updatebus(request):
    return render(request, 'users/busupdate.html')
def changebus(request):
    return render(request, 'users/buschange.html')
def changebuses(request):
    return render(request, 'users/busschange.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']

        # Validate the input
        if password1 != password2:
            return render(request, 'users/register.html', {'error': 'Passwords do not match.'})
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password1,
            phone=phone,
            fname=fname,
            lname=lname,
            gender=gender
        )
        user.save()
        login(request, user)
        return redirect('/')
    return render(request, 'users/register.html')

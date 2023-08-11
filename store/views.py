from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import StudentForm
from .models import Department, Purpose, Course, Material
from django.contrib import messages



from django.db import IntegrityError



def home(request):
    return render(request, 'home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('new_page')  # Redirect to the new page
        else:
            messages.error(request, 'Incorrect login credentials')
    return render(request, 'login.html')




def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken. Please choose a different username.')
            return render(request, 'register.html')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful. Please login.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'An error occurred while registering. Please try again.')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')


def dashboard(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = StudentForm()

    return render(request, 'dashboard.html', {'form': form})


def form_view(request):
    form = StudentForm(request.POST or None)
    order_confirmed = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            order_confirmed = True
            messages.success(request, 'Order Confirmed')  # Add this line to show the success message

            if 'submit_logout' in request.POST:
                logout(request)

    departments = Department.objects.all()
    purposes = Purpose.objects.all()
    materials = Material.objects.all()

    context = {'form': form, 'departments': departments, 'purposes': purposes, 'materials': materials, 'order_confirmed': order_confirmed}
    return render(request, 'form.html', context)








def confirmation_view(request):
    return render(request, 'confirmation.html', {'message': 'Order Confirmed'})



def get_courses(request):
    department_id = request.GET.get('department')
    if department_id:
        courses = Course.objects.filter(department_id=department_id).values('id', 'name')
        return JsonResponse({'courses': list(courses)})
    return JsonResponse({'courses': []})


def new_page(request):
    return render(request, 'new_page.html')
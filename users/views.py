from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from users.models import User


# Create your views here.


def register_user(request):
    template = 'users/register_user.html'
    return render(request, template)


def confirm_register_user(request):
    if request.method == 'POST':
        new_user = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        new_user.save()

        return HttpResponseRedirect(reverse('users:login'))
    return HttpResponse('Error: method not allowed.')


def login_user(request):
    template = 'users/form_user.html'
    return render(request, template)


def confirm_login_user(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
        except User.DoesNotexist:
            return HttpResponse('User does not exist!!!')

        return HttpResponseRedirect(reverse('tows:page', kwargs={'user_id': user.id}))
    return HttpResponse('Error: method not allowed!!!')
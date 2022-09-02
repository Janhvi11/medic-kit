from tabnanny import check
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.views import LoginView #
from django.contrib.auth import authenticate, login
from ..models import user
# from django.shortcuts import 
# from ..forms import LoginUserForm #

from ..forms import LoginUserForm

def login_home(request):
    return render(request, "login-main.html")

##

# def login_request(request):
#     # template_name = "login.html"
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             # password = form.cleaned_data.get('password')
#             password = form.cleaned_data['password']
#             # return render(request, 'demo.html') #, {'access':check_password}
#             user = authenticate(username=username, password=password)
            
            
#             if user is None:
#                 messages.error(request, "Invalid username or password.")
#             else:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}")
#                 return redirect('reg/main/')
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request = request,
#                     template_name = "login.html",
#                     context={"form":form})

def login_request(request):
    # template_name = "login.html"
    # form_class = LoginUserForm
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        # form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username_got = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            #     # password = make_password(request.POST['password'])
            #     # return render(request, 'demo.html') #, {'access':check_password}
            
            obj = get_object_or_404(user, username=username_got)
            res = check_password(password,obj.password1)
            
            if res == True:
                # login(request, user_check)
                messages.info(request, f"You are now logged in as {username_got}")
                return HttpResponseRedirect('/reg/login/')
            else:
                messages.error(request, "Invalid username or password.")
                
    else:
        form = LoginUserForm()
        # messages.error(request, "error 2.")
    # form = AuthenticationForm()
    return render(request, template_name = "login.html", context = {"form":form})
    
# class UserLoginView(LoginView):
#     form_class = LoginUserForm
#     # initial = {'key': 'value'}
#     template_name = 'login.html'

#     def form_valid(self, form):
#         # return redirect('/reg/main')
#         remember_me = form.cleaned_data.get('remember_me')

#         if not remember_me:
#             # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
#             self.request.session.set_expiry(0)

#             # Set session as modified to force data updates/cookie to be saved.
#             self.request.session.modified = True

#         # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
#         return super(UserLoginView, self).form_valid(form)
#         # return redirect(to='/reg/main')
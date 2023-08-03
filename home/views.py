from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from home.models import *
from home.forms import*
# Create your views here.
def home(request):
    context={}
    if request.user.is_authenticated and not request.user.is_superuser:
        recrute=profile.objects.filter(user=request.user)
        context['recruiter']=recrute[0].recruited()
    return render(request, 'home/index.html',context)

def SignUp(request,pk):
    if request.method == 'POST':
        user_form=UserCreateForm(request.POST)
        pro_form=profile_form(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            profile_=pro_form.save(commit=False)
            profile_.user=user
            print(type(pk))
            if int(pk)==1:
                profile_.recruiter=True
            else:
                profile_.finder=True
            profile_.save()
            return redirect(reverse_lazy("login"))
    return render(request, 'home/signup.html',{'Userform':UserCreateForm,'Profile':profile_form})

def Login(request):
    return HttpResponse('hello worked')

def skilltest(request):
    scoor=0
    if request.method == 'POST':
        que1=request.POST.get('option1')
        que2=request.POST.get('option2')
        if que1=='A':
            scoor+=1
        if que2=='A':
            scoor+=1
        return render(request, 'home/success_skilltest.html',{'scoor':scoor})
    return render(request, 'home/skilltest.html')


class postlist(ListView):
    model=posts

class createpost(CreateView,LoginRequiredMixin):
    template_name='home/post_form.html'
    form_class=post_form
    model=posts
    success_url=reverse_lazy('home')
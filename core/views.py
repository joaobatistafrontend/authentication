from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView,CreateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context ['cont'] = User.objects.count()
        return context
# def home(request):
#     cont = User.objects.count()
#     return render(request,'home.html',{'cont':cont})



def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST )
        if form.is_valid():
            user = form.save()
            return redirect ('home')
    else:
        form = UserCreationForm()
    return render(request,'registration/singup.html',{
        'form':form
        })

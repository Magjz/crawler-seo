# accounts/views.py
from .forms import RegisterForm, ProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView

User = get_user_model()

class SignUp(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class Profile(UpdateView): 
    template_name = 'registration/profile.html' 
    form_class = ProfileForm

    # def get_queryset(self):
    #     self.profile = get_object_or_404(User, id = self.kwargs['id'] )
    #     # return User.objects.filter(username=self.toto)
    
    #     return reverse('author-detail', kwargs={'id': self.profile})

    def get_object(self, queryset=None): 
        if request.method == "POST": 
            form = profileForm(data=request.POST, instance=request.user)
            update = form.save()
            update.user = request.user
            update.save()
        else:
            form = profileForm(instance=request.user)

        return render(request, 'registration/profile.html', {'form': form})
    
# class Profile(UpdateView):
#     template_name = 'registration/profile.html' 
#     form_class = ProfileForm

#     def get_object(self, queryset=None):
#         profile = get_object_or_404(User, pk = self.kwargs['id'])
#         return profile



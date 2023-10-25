from django.shortcuts import render, redirect
from django.views import View
from .forms import CreateUserProfileForm


class CreateUserProfileView(View):
    def get(self, request):
        form = CreateUserProfileForm()
        return render(
            request,
            'user_profile/create_user_profile.html',
            {'form': form})

    def post(self, request):

        submitted_form = CreateUserProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            print(submitted_form)
            submitted_form.save()
            print('form saved')
        else:
            print('form not saved, not valid')
            print(form.errors)
        return redirect('home')


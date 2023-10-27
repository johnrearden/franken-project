from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CreateUserProfileForm
from .models import UserProfile


class UserProfileView(View):
    def get(self, request):
        if (request.user.is_authenticated):
            try:
                existing_profile = UserProfile.objects.get(user=request.user)
                print(existing_profile)
                form = CreateUserProfileForm(instance=existing_profile)
            except UserProfile.DoesNotExist:
                existing_profile = None
                print('no user exists')
                form = CreateUserProfileForm()
        return render(
            request,
            'user_profile/create_user_profile.html',
            {'form': form, 'existing_profile': existing_profile})

    def post(self, request):

        submitted_form = CreateUserProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            new_profile = submitted_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            print('form saved')
        else:
            print('form not saved, not valid')
            return render(
                request,
                'user_profile/create_user_profile.html',
                {'form': form}
            )
        return redirect('home')


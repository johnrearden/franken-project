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
                print(form.fields['nickname'])
        return render(
            request,
            'user_profile/create_user_profile.html',
            {'form': form, 'existing_profile': existing_profile})

    def post(self, request):

        # Check for an existing profile
        existing_profile = UserProfile.objects.filter(user=request.user).first()
        if existing_profile:
            submitted_form = CreateUserProfileForm(
                request.POST,
                request.FILES,
                instance=existing_profile)
        else:
            submitted_form = CreateUserProfileForm(
                request.POST,
                request.FILES)

        if submitted_form.is_valid():
            profile = submitted_form.save(commit=False)
            profile.user = request.user
            profile.save()
        
        else: # form not valid
            print('form not saved, not valid')
            return render(
                request,
                'user_profile/create_user_profile.html',
                {'form': submitted_form}
            )
        return redirect('home')

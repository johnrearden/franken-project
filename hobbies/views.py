from django.shortcuts import render, reverse
from django.views import View
from .models import Hobby
from .forms import HobbyForm
from django.http import HttpResponseRedirect


class HobbyList(View):
    def get(self, request):
        hobbies = Hobby.objects.all()
        form = HobbyForm()
        context = {
            'hobbies': hobbies,
            'form': form,
        }

        return render(request, 'hobbies/hobby_list.html', context)

    def post(self, request):
        form = HobbyForm(request.POST, request.FILES)
        if form.is_valid():
            hobby = form.save(commit=False)
            hobby.owner = request.user
            print(hobby)
            hobby.save()
            return HttpResponseRedirect(reverse('hobby_list'))
        else:
            print('problem!')
            hobbies = Hobby.objects.all()
            context = {
                'hobbies': hobbies,
                'form': form,
            }
            return render(request, 'hobbies/hobby_list.html', context)
            
            



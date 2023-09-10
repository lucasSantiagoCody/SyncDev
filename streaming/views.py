from django.shortcuts import render
from accounts.models import Profile


def index(request):
    context = {}
    if request.method == 'GET':
        if request.user.id != None:
            context['profile'] = Profile.objects.get(user=request.user)
        return render(request, 'index.html', context )
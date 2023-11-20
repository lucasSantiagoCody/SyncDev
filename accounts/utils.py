from django.http import JsonResponse, HttpResponse
from .models import CustomUser


def verify_years_old(date_of_birth):
    from datetime import date 

    if date_of_birth:
        year_atual = date.today().year
        date_of_birth_year = int(date_of_birth.split('-' if '-' in date_of_birth else '/')[0])
        years_old = year_atual - date_of_birth_year

        if years_old >= 13:
            return 'valid'
        else:
            return 'invalid'  
    else:
        return 'invalid'

def validate_email(request):
    import re
    email = request.POST.get('email')
    valid_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if re.search(valid_email, email):
        user = CustomUser.objects.filter(email=email)
        if user:
            return JsonResponse({'email_status': 'this emeail already exists'})
        else:
            return JsonResponse({'email_status': 'valid'})
    else:
        return JsonResponse({'email_status': 'this email is invalid'})
    
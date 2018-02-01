import csv
from django.http import HttpResponse
from django.contrib.auth.models import User


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']= 'attachment; filename="users.csv"'

    write = csv.writer(response)
    write.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        write.writerow(user)

    return response
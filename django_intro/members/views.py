from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
# Create your views here.
def members(request):
  members = Members.objects.all()
  
  return render(request,'all_members.html', {'members': members})

def details(request, member_id):
  member = Members.objects.get(id=member_id)
  return render(request, 'details.html', {'member': member})

def main(request):
  return render(request, 'main.html')

def testing(request):
  members = Members.objects.all()
  context={'members': members}
  return render(request, 'template.html', context)
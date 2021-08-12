from django.http import response
from django.shortcuts import render
import requests
import json

# Create your views here.
def All_search_users():
    request = requests.get('https://api.github.com/users')
    all = json.loads(request.content)
    return render(request ,'Components/home.html',{
        'usuario':all['users'],
        'Nome':all['name']
    })

def get_user(users):
    request = requests.get(f'https://api.github.com/users/{users}')
    us = json.loads(request.content)
    print(us)


def get_user_repos(users):
    request = requests.get(f'https://api.github.com/users/{users}/repos')
    repos = json.loads(request.content)
    print(repos)
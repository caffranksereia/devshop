import requests
import json

class gitMember():
        def __init__(self,users):
                self._users = users


        def All_search_users():
                request = requests.get('https://api.github.com/users')
                all = json.loads(request.content)
                print(all)

        def get_user(users):
                
                request = requests.get(f'https://api.github.com/users/{users}')
                us = json.loads(request.content)
                print(us)

        def get_user_repos(users):
                request = requests.get(f'https://api.github.com/users/{users}/repos')
                repos = json.loads(request.content)
                print(repos)    
                
            

gitMember.get_user(users='caffranksereia')
gitMember.get_user_repos(users='caffranksereia')
        



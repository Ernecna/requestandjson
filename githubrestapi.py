import requests
import json

class Github:
    
    def __init__(self):
        self.api_url='https://api.github.com'
        self.token=''
        self.headers = {'Authorization': 'token ' + self.token}
    
    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
    
    def getRepo(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()
    
    def createRepo(self, name):
        payload = {
            "name": name,
            "description": "try desc",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
        response = requests.post(self.api_url + '/user/repos', headers=self.headers, json=payload)
        return response.json()
        
github = Github()

while True:
    choice = input("1-Find user\n2-Get Repositories\n3-Create Repository\n4-Exit\nChoice:")
    username = input("Username:")
    
    if choice == '4':
        break
    elif choice == '1':
        result = github.getUser(username)
        print(f'name: {result["name"]} public repos: {result["public_repos"]} followers: {result["followers"]}')
    elif choice == '2':
        res = github.getRepo(username)
        for repo in res:
            print('Repo name:' + repo['name'])
    elif choice == '3':
        reponame = input('Repository name:')
        res = github.createRepo(reponame)
        print(res)
    else:
        print("Wrong choice")

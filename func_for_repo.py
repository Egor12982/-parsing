def repo():
    import requests
    import json
    user = input("Type nickname of user: ")
    link = f"https://api.github.com/users/{user}/repos"
    r = requests.get(link)
    data = r.json()
    x = 0
    for x in range(0,len(data)):
        s = print("Name of repository:", data[x]['name'])
        x = x + 1
    return print(f"Amount number of repo: {x}")

repo()

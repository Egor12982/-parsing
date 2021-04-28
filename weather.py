def weather():
    import requests
    from pprint import pprint
    user = input("Type your city: ")
    home = f"https://api.openweathermap.org/data/2.5/weather?q={user}&appid=58c18eeee64a1b9ce3882a851ec2bdf1"
    r = requests.post(home)
    return pprint(r.text)

weather()
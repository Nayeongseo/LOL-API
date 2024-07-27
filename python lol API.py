import requests
from urllib import parse

def GetUrl():
    url = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+username+'?api_key='+apiKey
    r = requests.get(url)
    return r

def Getpuuid(r):
    r = r.json()
    puuid = r["puuid"]

    print("\n\n\npuuid는 ", puuid)
    return puuid

def get_normalID(puuid, count, start):
    type = 'normal'

    normalUrl = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid+'/ids?type='+type+'&start='+str(start)+'&count='+str(count)+'&api_key='+apiKey
    r = requests.get(normalUrl)
    r = r.json()

    normalId = r

    print("아이디는", normalId)

    return normalId

#경로 : info 안에 participants 안에 10명의 사람 중 win에 들어있는 True or False
def Win(normalId):
    win = 0

    for i in range(len(normalId)):
        winUrl = 'https://asia.api.riotgames.com/lol/match/v5/matches/'+normalId[i]+'?api_key='+apiKey
        r = requests.get(winUrl)
        r = r.json()
    
        info = r["info"]["participants"]

        for i in range(10):
            Array = info[i]

            if(Array["summonerName"] == username):
                RankWin = Array['win']

                if(RankWin == True):
                    win = win +1

    print(win)

    return win

apiKey = '' # Key 붙여넣기
username = 'Amelia00'
count = 20
start = 0

r = GetUrl()

puuid = Getpuuid(r)

normalId = get_normalID(puuid, count, start)

win = Win(normalId)

print(username,"의", count,"회 무작위 총력전 게임 승률은: ", win/count*100, "% 입니다.")
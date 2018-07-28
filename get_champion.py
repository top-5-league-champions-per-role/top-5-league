import requests
import json

#limit = 10
debug = True
api_key = "3260c726f51f9331cea75a9279392f78"

def request_by_role(role, limit="5", elo=""):
    '''Get champions based on {role}
    Optional {limit}, default 5
    Optional {elo} argument
    url rgs are auto-capitilized to matc champion.gg format'''
    #role = role.capitalize()
    #matchup:
    url = "http://api.champion.gg/v2/champions/1/{}/matchups?limit={}&api_key={}".format(role,limit,api_key)
    if elo != "":
        elo = elo.capitalize()
        url = url + "&elo={}".format(elo)
    # get the details from url
    r = requests.get(url)
    #convert to json
    as_json =r.json()
    if debug:
        #print(as_json)
        print(r)
        print("url:\t{}".format(url))
    print(json.dumps(as_json, indent=4, sort_keys=True))


def request_champ_details(champ_id, limit = "5", elo = ""):
    #url = "http://api.champion.gg/v2/champions/1?elo=SILVER&limit=200&champData=kda,damage,averageGames,totalHeal,killingSpree,minions,gold,positions,normalized,groupedWins,trinkets,runes,firstitems,summoners,skills,finalitems,masteries,maxMins,matchups&api_key={}".format(api_key)
    url = "http://api.champion.gg/v2/champions/{}?limit={}&sort=winRate-desc&api_key={}".format(champ_id, limit,api_key)
    if elo != "":
        elo = elo.capitalize()
        url = url + "&elo={}".format(elo)

    r = requests.get(url)
    #convert to json
    as_json =r.json()
    if debug:
        #print(as_json)
        print(r)
        print("url:\t{}".format(url))
        print(json.dumps(as_json, indent=4, sort_keys=True))


if __name__ == '__main__':
    #request_by_role("MIDDLE", 5, "SILVER")
    #request_by_role("MIDDLE")
    request_champ_details(202)


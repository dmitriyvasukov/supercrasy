import requests as r
from datetime import datetime,timezone




def interpret(result):
    if result < 7: 
        return "ты говно"

def process_user(user):
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1NjkxNSIsImp0aSI6ImFlOTE1ZTM0MDMzZTUyM2U5MjIxZjlmY2RiZmVkOWZlM2VmYWEzNjBhNTczNGVmMzVkYzIyMDAyNjNkNjFlOTQyNTQzZWU1OWY1NjNmNjY3IiwiaWF0IjoxNzg4MDA4NzA4LjM5Nzc3LCJuYmYiOjE3ODgwMDg3MDguMzk3NzczLCJleHAiOjE3ODgwOTUxMDguMzg4ODQ3LCJzdWIiOiIiLCJzY29wZXMiOlsicHVibGljIl19.bSx39zYl2kIsbWxd1Of6xcGaeUNdIbqwL0Cf35VcF6Dq0CowmNf5M0azOiyrrEkqeMfKYmie2L4cCtB3smiIux53XbXY8xV0RRd0FXX2vPznGnRv_UxK8iz91uk54A-d54fCAvrj1Y-cnS9xdkA1O6mWlpcf97rMcuaWPlwibQ9gHwbs-7oFVNZv5bPCZUhyTbsnzJk6u-Rrmpe2KD-o0XWFigi6YZ7lNgFf52mMntFhv3jT8bZKXhwqzCnTQZnEy1kBM4Qx3wz9iUHakQ6qM3YaPzo_a2F3scKzZAoFYW9gt1dFeMtzjALe36sJYly3dhJGG_KO6Khqdchwi9pNxaDOEaIZ-lcSYwrtfDqdHfEvzHCW8ffaO0jZkz3jKxyZJiiBs-hSXKvhOCy-RGlDXuoD7oTwvLBBa9eNhxgg9yG_oPdgrC9BW0JPe2yBoLdLnQbahlzyYwZN-KfvSud7qEX1lbjrjwSCjsgy0-ocLsJ-nzDQdngn0Yz85Y-ZeotcLEH4dvYgGxdUcY5Y3wHgv4gOPCV0puZfSlO5J8qkoUZx66jGpqvzDeTNrv8QzZgYbu_Fc8LuYzPei06DCvCxFaEbpOGyGmisRpZ2XcQ3d8aSRPR0aHkV92TkEyCHowLyR34cLYivnpWK36Z0whQyDCFNFQEUtSdpX3yasmTFv34"
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

    body = {
    "limit" : "3"
    }
    res = r.get(f"https://osu.ppy.sh/api/v2/users/{user}/beatmapsets/most_played", headers=headers, params=body).json()


    user_stats = r.get(f'https://osu.ppy.sh/api/v2/users/{user}/osu', headers=headers).json()

    user_pp = user_stats['statistics']['pp']
    username = user_stats['username']
    user_playtime = user_stats['statistics']['play_time']
    print(user_pp, username)

    result = 0
    for item in res: 
        bm = item['beatmap_id']
        score = r.get(f'https://osu.ppy.sh/api/v2/beatmaps/{bm}/scores/users/{user}', headers=headers).json()
        if score.get('score') is None:
            continue
        if score['score']['pp'] is None:
            continue
        pp = score['score']['pp']
        score_time = score['score']['created_at']
        normal_format = datetime.fromisoformat(score_time.replace("Z", "+00:00"))
        current_time = datetime.now(timezone.utc)
        deltat = current_time - normal_format
        result+=(pp/item['count'] * (deltat.total_seconds() / 3600)) / user_pp
        


    loh_count = ((user_playtime)/3600 / user_pp) * result 
    return {"username" : username, "loh_count" : loh_count, "summary" : interpret(loh_count)}


import requests as r
from datetime import datetime,timezone




def interpret(result):
    if result < 7: 
        return "ты говно"

def process_user(user):
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1NjkxNSIsImp0aSI6IjZhZWM4M2JmYTFkZGFkNmQ3NmJhNTYzOWY0Yzk0MWE1NmJhNjQ3NDVmMDljNWM0NGM0NGE0MDU4M2I2MTI4ZjViNjQ4MTdmOGJkMjg4MGIxIiwiaWF0IjoxNzg4MTE2MDI5LjQ1MTIxNCwibmJmIjoxNzg4MTE2MDI5LjQ1MTIxNywiZXhwIjoxNzg4MjAyNDI5LjQzMDIzMiwic3ViIjoiIiwic2NvcGVzIjpbInB1YmxpYyJdfQ.DpT8ZibekjwoXdN_XuMg3CS-xe9zZ7XYjzemtEYsKN-VF4O1jJ2kkjtTfpQi-nhTkWyvErq_XfeYhCXWDoeGcstDGVg_62nRC6lTyKiQTV3aWdQiZOGttgLTp2AczerQzc2o5VvACxvmkok_kp9NkBTzHKhUp5ufQOyzX0sp3d8TxWUGbuYEf9vYq6u3cDStZ2EjqSoj1kQEjEpll0HPK4DPEUR-PjfBL0gR6jib7E7xJ-uxXa_Mn9pzDNdmVgh6MTMxAWOcLUhXBnR5lS-YISyMsgH5HikVTKDrl63st0ybRJCWgc-Dz72LZk_CCYOMll5vmDc2Xn8CU3jQvhSe1NREXjUs7Qm8vfpKYRvkGvvJycz_RHcYEDN9g3HG-OxhUrwK77sNLc2KrSCjVPffmn8Xj4lH-QCU6max6CbMYKEBB8uO5ruxHpaRWkzciqKlfelZaKynNKCNePZBWJ6BVXES6PRsJvwfqWjm1Pu-Twko0nPMF106f2UsEvKsqEUMX1PthKAPY7nQIF2l96z9foPqA35BR_l3wfJInXzDl3tYgir-ge4THxB5_z5T0quzBTEzMH5JJTVKqFA40_JUVb3feWi3H0D8rc9PxcKcpb6obfHfnnIO04_X2raYzwMLZnAOpXbsGvyjQyJu9Rvq0Knjtc_lj9jMwJPZZs91KoY"
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

    body = {
    "limit" : "100"
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


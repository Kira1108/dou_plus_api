import pandas as pd
import json

def clean_live_fans(data):

    results = []
    for d in data['live_fans_analysis']:

        blogger_id = d['user_id']
        live_id = d['live_id']
        fans_city = json.dumps({'data': d['data']['city']}, ensure_ascii=False)
        fans_gender = json.dumps({'data': d['data']['gender']}, ensure_ascii=False)
        fans_province = json.dumps({'data': d['data']['province']}, ensure_ascii=False)
        fans_age = json.dumps({'data': d['data']['age']}, ensure_ascii=False)
        results.append([blogger_id, live_id, fans_city, fans_gender, fans_province, fans_age])

    return pd.DataFrame(results, columns = ['blogger_id',"live_id",'fans_city','fans_gender','fans_province','fans_age'])

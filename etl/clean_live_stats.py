import pandas as pd



def clean_live_stats(data):

    col_names = ['blogger_id','live_count','live_product_count','total_ticket',
     'avg_ticket','total_volume','avg_volume','total_amount',
     'avg_amount','product_size','product_rate',
     'total_user','avg_uv']


    results = []
    for d in data['live_overview']:


        summary = d['data']['summary']

        result = dict(blogger_id = d['user_id'],
        live_count = summary.get('live_count',None),
        live_product_count= summary.get('live_product_count',None),
        total_ticket = summary.get('total_ticket',None),
        avg_ticket = summary.get('avg_ticket',None),
        total_volume = summary.get('total_volume',None),
        avg_volume = summary.get('avg_volume',None),
        total_amount = summary.get('total_amount',None),
        avg_amount = summary.get('avg_amount',None),
        product_size = summary.get('product_size',None),
        product_rate = summary.get('product_rate',None),
        total_user = summary.get('total_user',None),
        avg_uv = summary.get('avg_uv',None))
        results.append(list(result.values()))

    return pd.DataFrame(results, columns = col_names)

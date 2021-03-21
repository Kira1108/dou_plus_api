import pandas as pd

def clean_live_info(data):

    room_keys = ['room_id', 'room_title', 'live_cover', 'begin_time', 'room_finish_time',
    'product_size', 'status', 'user_count', 'has_volume', 'is_predicted',
    'total_user', 'watch_cnt', 'user_peak', 'gift_uv_count', 'is_take_product',
    'volume', 'reputation', 'amount', 'room_ticket_count', 'crawl_time', 'share_url',
    'barrage_author_count', 'increment_follower_count', 'average_residence_time',
    'average_user_count', 'city_watch_ucnt', 'dou_plus_enter_cnt', 'live_live_watch_ucnt',
    'others_watch_ucnt', 'video_detail_watch_ucnt', 'like_count', 'room_ticket_percent',
    'amount_percent', 'average_online_percent', 'play_url', 'user_value', 'purchase_count',
    'is_support', 'conversion_rate_percent', 'interaction_percent', 'fans_num', 'fans_num_rate']


    author_keys = ['author_id', 'nickname', 'birthday', 'province', 'city', 'avatar', 'unique_id',
     'short_id', 'gender', 'follower_count', 'following_count', 'total_favorited',
     'pay_score', 'total_room_ticket_count', 'is_fav']

    results = []
    for d in data['live_info']:

        room = [d['data']['room'].get(k, None) for k in room_keys]
        author = [d['data']['author'].get(k, None) for k in author_keys]


        results.append([d['user_id'],d['live_id']] + room + author)

    return pd.DataFrame(results, columns = ['blogger_id','live_id'] + room_keys + author_keys)

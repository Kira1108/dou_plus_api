import pandas as pd

def json_map(data):

    blogger = {'blogger_id': data['author_id'],
     'blogger_name': data['nickname'],
     'avatar': data['avatar'],
     'signature': data['signature'],
     'birthday': data['birthday'],
     'province': data['province'],
     'city': data['city'],
     'gender': data['gender'],
     'total_comment': data['total_comment'],
     'follower_count': data['follower_count'],
     'total_share': data['total_share'],
     'total_room_ticket_count': data['total_room_ticket_count'],
     'total_favorited': data['total_favorited'],
     'fans_club_total': data['fans_club_total'],
     'history_aweme_count': data['history_aweme_count'],
     'tag_first': data['single_tags']['first'],
     'tag_second': ', '.join(data['single_tags']['second']),
     'mcn_name': data['mcn_name'],
     'mcn_id': data['mcn_id'],
    }
    return list(blogger.values())


def clean_blogger(data):
    col_names = ['blogger_id','blogger_name','avatar','signature',
                 'birthday','province','city','gender','total_comment',
                 'follower_count','total_share','total_room_ticket_count',
                 'total_favorited','fans_club_total','history_aweme_count',
                 'tag_first','tag_second','mcn_name','mcn_id']

    bloggers = []
    for blogger in data['base_user_info']:
        d = blogger['data']
        bloggers.append(json_map(d))

    return pd.DataFrame(bloggers, columns = col_names)

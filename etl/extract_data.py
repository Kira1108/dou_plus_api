from dbconfig import db

def extract_data(limit = 1000):
    return dict(live_overview = db.query('live_overview',limit),
                base_user_info = db.query('base_user_info',limit),
                user_fans_analysis = db.query('user_fans_analysis',limit),
                live_fans_analysis = db.query('live_fans_analysis',limit),
                live_info = db.query('live_info',limit),
                live_goods = db.query('live_goods',limit))

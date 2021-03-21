from etl.extract_data import extract_data
from etl.clean_fans import clean_fans
from etl.clean_blogger import clean_blogger
from etl.clean_live_stats import clean_live_stats
from etl.clean_live_info import clean_live_info
from etl.clean_live_goods import clean_live_goods
from etl.clean_live_fans import clean_live_fans
from .dbconfig import get_mysql_conn
from collections import Counter


NROWS = 1000000

def pipeline():
    engine = get_mysql_conn(engine = True)
    data = extract_data(NROWS)
    clean_fans(data).to_sql('user_fans', con = engine, if_exists = 'replace')
    clean_blogger(data).to_sql('blogger', con = engine, if_exists = 'replace')
    clean_live_stats(data).to_sql('live_stats', con = engine, if_exists = 'replace')
    clean_live_info(data).to_sql('live_info', con = engine, if_exists = 'replace')
    clean_live_goods(data).to_sql('live_goods', con = engine, if_exists = 'replace')
    clean_live_fans(data).to_sql('live_fans', con = engine, if_exists = 'replace')

    df = pd.read_sql_query("select user_id, v2_category_big from live_goods",get_mysql_conn())
    get_mysql_conn(engine=True)
    df.groupby('user_id')['v2_category_big']\
        .apply(lambda x:','.join([t[0] for t in Counter(list(x)).most_common()[:3] if t[1] > 3]))\
        .reset_index().rename(columns = {"user_id":'blogger_id'})\
        .to_sql('blogger_tags',get_mysql_conn(engine=True), if_exists = 'replace')


    good_sql = '''select
    	product_id as id,
    	product_title as name,
    	v2_category_big as tag,
    	brand_name as brand,
    	avg(final_price) as price,
    	count(distinct user_id) as related_blogger,
    	count(distinct live_id) as related_live,
    	sum(volume) as live_sales_count,
    	sum(amount) as live_sales_money
    from live_goods
    group by product_id, product_title, tag, brand'''

    pd.read_sql_query(good_sql, get_mysql_conn()).to_sql('goods_stats',get_mysql_conn(engine = True), if_exists='replace')

if __name__ == '__main__':
    pipeline()

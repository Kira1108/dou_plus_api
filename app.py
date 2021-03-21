
from flask import Flask,jsonify,request
from dbconfig import execute_sql


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/tags')
def get_tags():
    tags = {'message':"successful", "code":200, "sucess":True,'data':{}}
    try:
        sql_blogger_tag = '''select distinct tag_first from blogger
        union all
        select distinct tag_second from blogger'''

        blogger_tags = list(set([tt.strip() for t in execute_sql(sql_blogger_tag) for tt in t[0].split(',') ]))
        blogger_tags = {'blogger_tags':blogger_tags}
        sql_good_tag = 'select distinct v2_category_big from live_goods'
        good_tags = [t[0] for t in execute_sql(sql_good_tag)]
        good_tags = {'goods_tags':good_tags}


        tags['data'].update(blogger_tags)
        tags['data'].update(good_tags)

    except Exception as e:
        tags['message'] = 'failure'
        tags['code'] = 500
        tags['sucess'] = False
    return jsonify(tags)


def paging(page = 2, size = 30):
    page = int(page)
    size = int(size)
    page -= 1
    where = ' where b.`index` >= {} and b.`index` < {}'.format(page*size, (page+1) * size)
    return where



# @app.route('/blogger/rank/live')
# def blogger_list():
#     try:
#         page = request.args.get('page', 1)
#         size = request.args.get('size', 30)
#         field_names = [f[0] for f in execute_sql("show columns from blogger")]
#         blogger_sql = "select * from blogger {}".format(paging(page, size))
#         data = [dict(zip(field_names, r)) for r in list(execute_sql(blogger_sql))]
#         return jsonify({'data':data, "message":"successful","code": 200,"success": True})
#     except Exception as e:
#         print(e)
#         return jsonify({"message":"failure","code": 400,"success": False})



@app.route('/blogger/rank/live')
def blogger_list():

    page = request.args.get('page', 1)
    size = request.args.get('size', 30)
    tag = request.args.get("tag",None)
    tag = " and tag_first = '{}'".format(tag) if tag else ''

    blogger_sql = '''select
    b.blogger_id as blogger_id,                   # 主播id
	b.blogger_name as name,                       # 主播名称
	b.follower_count as fans,                     # 粉丝数
	s.total_volume as live_sales_count,           # 总销量
	s.total_amount as live_sales_money,           # 总金额
	s.total_user as total_viewer,                 # 总观看
	i.max_viewer as max_viewer,                   # 最大观看
	s.product_size as total_goods_count,          # 商品数量
	t.v2_category_big as tags                     # 商品标签
    from blogger b
    left join live_stats s on b.blogger_id = s.blogger_id
    left join (select blogger_id, max(total_user) as max_viewer from live_info
    	group by blogger_id) i on b.blogger_id = i.blogger_id
    left join blogger_tags t on t.blogger_id = b.`blogger_id`
    {}'''.format(paging(page, size) + tag).strip()

    field_names = ['blogger_id','name','fans','live_sales_count','live_sanles_money',
    'total_viewer','max_viewer','total_goods_count','tags']
    try:
        data = [dict(zip(field_names, r)) for r in list(execute_sql(blogger_sql))]
        return jsonify({'data':data, "message":"successful","code": 200,"success": True})
    except Exception as e:
        print(e)
        return jsonify({"message":"failure","code": 400,"success": False})



@app.route('/goods/rank/live')
def good_list():
    try:
        page = request.args.get('page', 1)
        size = request.args.get('size', 30)
        tag = request.args.get("tag",None)
        tag = " and tag = '{}'".format(tag) if tag else ''

        field_names = ['id', 'name', 'tag', 'brand',
            'price', 'related_blogger', 'live_sales_count', 'live_sales_money']
        goods_sql = '''
            select id, name, tag, brand, price, related_blogger, live_sales_count, live_sales_money
            from goods_stats b
            {}
        '''.format(paging(page, size) + tag)
        data = [dict(zip(field_names, r)) for r in list(execute_sql(goods_sql))]
        return jsonify({'data':data, "message":"successful","code": 200,"success": True})
    except Exception as e:
        print(e)
        return jsonify({"message":"failure","code": 400,"success": False})


app.run('0.0.0.0',port = 8080)

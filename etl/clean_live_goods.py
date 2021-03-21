
import pandas as pd

def clean_live_goods(data):
    product_keys = ['product_title', 'amount', 'volume', 'final_price', 'category',
    'platform', 'commission_rate', 'image', 'product_id', 'has_volume',
     'source', 'is_predicted', 'brand_name', 'v2_category',
    'dy_promotion_id', 'start_time', 'stop_time', 'initial_sales', 'final_sales',
     'sales', 'for_sale', 'ext_info', 'sub_title', 'returned_rate']

    result_keys = ['user_id','live_id', 'product_title', 'amount', 'volume', 'final_price', 'category',
    'platform', 'commission_rate', 'image', 'product_id', 'has_volume',
     'source', 'is_predicted', 'brand_name', 'v2_category_big', 'v2_category_first','v2_category_second','v2_category_third',
    'dy_promotion_id', 'start_time', 'stop_time', 'initial_sales', 'final_sales',
     'sales', 'for_sale', 'ext_info', 'sub_title', 'returned_rate']


    results = []
    for d in data['live_goods']:

        for prod in d['data']['list']:

            vals = [d['user_id'],d['live_id']]

            for k in product_keys:

                if not k.startswith("v2_category"):
                    vals.append(prod.get(k, None))

                else:
                    big = prod['v2_category'].get('big',None)
                    first = prod['v2_category'].get('first',None)
                    second = prod['v2_category'].get('second',None)
                    third = prod['v2_category'].get('third',None)

                    vals += [big, first, second, third]
            results.append(vals)

    return pd.DataFrame(results,columns = result_keys)

######etsy_商品信息########
create_etsy_goods_des_table = """
state int COMMENT '商品状态',
product_id int PRIMARY KEY COMMENT '商品id' , 
product_url varchar(512) NOT NULL COMMENT '商品链接',
product_image varchar(512) NOT NULL COMMENT '商品图片',
product_name  mediumtext COMMENT '商品标题',
video varchar(512) COMMENT '商品视频',
category_id varchar(256)  COMMENT '行业id',
category_path varchar(256)  COMMENT '行业路径',
ships_from varchar(256)  COMMENT '发货地址',
keywords mediumtext COMMENT '关键词',
store_id int COMMENT '店铺ID',
store_name varchar(256) COMMENT '店铺名称',
homepage varchar(256) COMMENT '店铺链接',
ad tinyint COMMENT '是否存在广告',
ad_days int COMMENT '广告天数',
created_time varchar(256) COMMENT '创建时间',
rare_find varchar(256) COMMENT '稀有品',
best_seller  tinyint COMMENT '最佳销售',
reviews_total int COMMENT '评论量',
favorites_total int COMMENT '收藏量',
real_carts_total int COMMENT '真实的购物车量',
carts_total int COMMENT '购物车量',
offer_price float  COMMENT '打折价',
max_price float  COMMENT '最大价格',
min_price float COMMENT '最小价格',
est_sales_total int COMMENT 'ets 销量',
sales_total int COMMENT '销售总量',
date varchar(256) COMMENT '数据获取日期'
"""



create_etsy_goods_url_table = """
goodsid varchar(256) COMMENT '商品id',
shopid varchar(256)  COMMENT '店铺id',
path varchar(256)  COMMENT '商品路径',
title varchar(1024)  COMMENT '商品标题',
picture_url varchar(256)  COMMENT '图片链接',
is_ad varchar(256)  COMMENT '是否付费广告',
shopname varchar(256) COMMENT '店铺名称',
date varchar(256)  COMMENT '抓取时间'
"""

create_etsy_keywords_alura_table ="""
id int COMMENT '唯一id标识',
keyword varchar(256) COMMENT '关键词',
avg_monthly_searches varchar(256)  COMMENT '关键词的每月平均搜索次数',
three_months_change varchar(256) COMMENT '过去三个月搜索量或者受欢迎程度的变化:单位%',
competing_listings_etsy varchar(256)  COMMENT 'etsy 竞争商品数量',
keyword_score varchar(256) COMMENT '关键词得分',
monthly_search_volumes varchar(1024)  COMMENT '过去一年每月的搜索量',
avg_conversion_rate  varchar(256)  COMMENT '平均转化率',
competition_etsy varchar(256) COMMENT 'etsy  竞争',
competition_google varchar(256) COMMENT  '谷歌竞争',
long_tail_keyword bool,
year_average_change varchar(256) COMMENT '年平均变化:单位%',
search_competition_ratio varchar(256) COMMENT '搜索竞争比例',
avg_listing_age  varchar(256)  ,
competition_index_google varchar(256) COMMENT '谷歌竞争指数',
average_google_cpc varchar(256) COMMENT '谷歌点击平均成本',
low_top_of_page_bid_micros varchar(256) ,
high_top_of_page_bid_micros varchar(256),
trend varchar(256) COMMENT '趋势',
character_length  varchar(256) COMMENT '字符长度',
etsy_tag varchar(256),
avg_sales varchar(256) COMMENT '平均销售量',
tot_sales  varchar(256) COMMENT '最大销售量',
stemmed_array varchar(256),
last_fetch_update varchar(256) COMMENT '最后一次提取更新时间',
date varchar(256) COMMENT '抓取时间'
"""


create_etsy_keywords_alura_keysear_table ="""
id int COMMENT '唯一id标识',
keyword varchar(256) COMMENT '关键词',
avg_monthly_searches varchar(20)  COMMENT '关键词的每月平均搜索次数',
three_months_change varchar(20) COMMENT '过去三个月搜索量或者受欢迎程度的变化:单位%',
competing_listings_etsy varchar(20)  COMMENT 'etsy 竞争商品数量',
keyword_score varchar(20) COMMENT '关键词得分',
monthly_search_volumes varchar(1024)  COMMENT '过去一年每月的搜索量',
avg_conversion_rate  varchar(20)  COMMENT '平均转化率',
competition_etsy varchar(20) COMMENT 'etsy  竞争',
competition_google varchar(20) COMMENT  '谷歌竞争',
long_tail_keyword varchar(256),
year_average_change varchar(20) COMMENT '年平均变化:单位%',
search_competition_ratio varchar(20) COMMENT '搜索竞争比例',
avg_listing_age  varchar(20)  ,
competition_index_google varchar(20) COMMENT '谷歌竞争指数',
average_google_cpc varchar(20) COMMENT '谷歌点击平均成本',
low_top_of_page_bid_micros varchar(256) ,
high_top_of_page_bid_micros varchar(256),
trend varchar(20) COMMENT '趋势',
character_length  varchar(20) COMMENT '字符长度',
etsy_tag varchar(256),
avg_sales varchar(20) COMMENT '平均销售量',
tot_sales  varchar(20) COMMENT '最大销售量',
stemmed_array varchar(1024),
last_fetch_update varchar(50) COMMENT '最后一次提取更新时间',
avg_shop_conversion_rate varchar(20)  COMMENT '平均店铺转化率',
avg_shop_review_rate varchar(20)  COMMENT '平均店铺评价率',
avg_shop_review_average varchar(20)  COMMENT '平均店铺评分',
avg_shop_review_count varchar(20)  COMMENT '平均店铺评价数',
avg_listing_active_count  varchar(20) COMMENT  '平均店铺活跃商品数',
avg_shop_sales varchar(20) COMMENT  '平均店铺店铺销售量',
avg_shop_age varchar(20) ,
tot_revenue varchar(20) COMMENT '店铺总收入',
avg_revenue varchar(20) COMMENT '平均收入',
avg_shop_score varchar(20) COMMENT '平均店铺得分',
avg_review_average varchar(20)  ,
avg_review_count varchar(20),
avg_review_rate varchar(20),
avg_views varchar(20),
total_views varchar(20),
supply_ratio varchar(20),
vintage_ratio varchar(20),
physical_ratio varchar(20),
customizable_ratio varchar(20),
personalizable_ratio  varchar(20),
avg_processing varchar(20),
avg_processing_max varchar(20),
avg_processing_min varchar(20),
avg_lqs varchar(20),
opportunity_score varchar(20),
avg_price_usd varchar(20),
avg_num_favorites varchar(20),
related_keywords mediumtext,
added_to_database varchar(256),
updated_to_database varchar(256),
processing_duration varchar(256),
etsy_related_keywords mediumtext COMMENT 'ETsy 相关关键词',
gpt_related_keywords mediumtext COMMENT 'gpt 相关关键词',
avg_monthly_sales varchar(20) COMMENT '平均月销售',
last_searched_date varchar(50),
update_progress_percentage varchar(256),
keyword_status varchar(20),
similar_keyword_status varchar(20),
date varchar(256) COMMENT '抓取时间',
keyword_search varchar(256) COMMENT '关键词搜索词'
"""

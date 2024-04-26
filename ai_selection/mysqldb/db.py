import pandas as pd
import pymysql
from sqlalchemy import create_engine
import os
from urllib.parse import quote_plus as urlquote
from ai_selection.mysqldb import sql_mess


workpath = os.path.dirname(os.path.abspath(__file__))
import json

sql_host = 'localhost_goods'

with open(workpath + '/conf.json') as j:
    db_cfg = json.load(j)[sql_host]


class MysqlDbUtils():
    def __init__(self, host, port, user, passwd, db):
        self.conn = pymysql.connect(host=host  # 连接名称，默认127.0.0.1
                                    , port=port  # 端口，默认为3306
                                    , user=user  # 用户名
                                    , passwd=passwd  # 密码
                                    , database=db  # 数据库名称
                                    , charset='utf8'
                                    )

        self.cursor = self.conn.cursor()
        DB_CONNECT = f'mysql+pymysql://{user}:{urlquote(passwd)}@{host}:{port}/{db}?charset=utf8'

        self.engine = create_engine(DB_CONNECT)

    def create_table(self, tbname, content, comment):
        try:
            sql = "CREATE TABLE IF NOT EXISTS " + tbname + " (" + content + ") comment = '" + comment + "';"

            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)

    def delete_table(self, tbname):
        try:
            self.cursor.execute('DROP TABLE ' + tbname)
            self.conn.commit()
        except Exception as e:
            print(e)

    def query(self, sql, col_names=None):
        try:
            self.cursor.execute(sql)
            result = list(self.cursor.fetchall())
            columnDes = self.cursor.description
            columnNames = [columnDes[i][0] for i in range(len(columnDes))]
            return pd.DataFrame([list(i) for i in result], columns=columnNames)
        except Exception as e:
            print(e)

    def insert(self, tbname, names, values):
        try:
            self.cursor.execute("INSERT INTO " + tbname + "(" + names + ") VALUES (" + values + ");")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            return e

    def pd_to_table(self, df, tbname, mode):
        df.to_sql(name=tbname,
                  con=self.engine,
                  if_exists=mode,
                  index=False,
                  index_label=None, chunksize=None, dtype=None)

    #
    def update(self, tbname, alteration, condition):
        try:
            self.cursor.execute("UPDATE " + tbname + " SET " + alteration + " WHERE " + condition + ";")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def delete(self, tbname, condition):
        try:
            self.cursor.execute("DELETE FROM " + tbname + " WHERE " + condition + ";")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def close(self):
        self.cursor.close()
        self.conn.close()



c = MysqlDbUtils(db_cfg['host'], db_cfg['port'], db_cfg['user'], db_cfg['password'], db_cfg['database'])

# mess=c.insert("Web_task_process"
#               ,"desType, forward, markImgUrl, modelAge, modelExpression, modelImgId, modelSex, modelSkin, modelTemperament, modelUploadUrl, name, ordinal, ordinalImgResultList, originImgUrl, referedTaskId, reverse, remark, sceneImgId, sceneType, shortCutDesc, status, taskId, taskOrdinalId, type, userId, weight"
#               ,"'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 0, '[{follow: 0, imageId: 0, progress: 0, queue: 0, resImgUrl: string, resSmallImgUrl: string, taskId: 0,taskOrdinalId: 0, userId: 0, zan: 0}]', 'string', 0, 'string', 'string', 'string', 0, 'string', 0, 0, 0, 0, 0, 0")
#

# print("mess",mess)
# except pymysql.IntegrityError as e:
#


# def create_model_table():
#     create_etsy_goods_des_table=sql_mess.create_etsy_goods_des_table
#     c.create_table("etsy_goods_ixspy",create_etsy_goods_des_table,"ixspy")
#
# create_model_table()

# def create_etsy_goods_url_table():
#     create_etsy_goods_url_table=sql_mess.create_etsy_goods_url_table
#     c.create_table("etsy_goods_url",create_etsy_goods_url_table,"etsy品类页列表")
#
# create_etsy_goods_url_table()

#
# def create_etsy_keywords_alura_table():
#     create_etsy_keywords_alura_table=sql_mess.create_etsy_keywords_alura_table
#     c.create_table("etsy_keywords_alura",create_etsy_keywords_alura_table,"alura 首页数据")
#
# create_etsy_keywords_alura_table()


# def create_etsy_keywords_alura_keysear_table():
#     create_etsy_keywords_alura_keysear_table=sql_mess.create_etsy_keywords_alura_keysear_table
#     c.create_table("etsy_keywords_alura_keysear",create_etsy_keywords_alura_keysear_table,"alura 通过关键词搜索的相关关键词")
#
# create_etsy_keywords_alura_keysear_table()


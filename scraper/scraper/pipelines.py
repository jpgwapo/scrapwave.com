# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
import os
import environ

env = environ.Env()

BASE_DIR = environ.Path(__file__) - 1  # three levels up from settings.py


class ScraperPipeline(object):
    
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = psycopg2.connect(
            host=os.getenv('DATABASE_HOST'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            dbname=os.getenv('DATABASE_NAME')
        )
        # self.conn = psycopg2.connect(
        #     host='localhost',
        #     user='paul',
        #     password='',
        #     dbname='scrapwave'
        # )
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS properties_property""")
        self.curr.execute("""CREATE TABLE properties_property(
            id TEXT,
            name TEXT,
            url TEXT,
            price TEXT,
            image_url TEXT
            )""")
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO properties_property VALUES (%s, %s, %s, %s, %s)""", (
            item['id'][0],
            item['name'][0],
            item['url'][0],
            item['price'][0],
            item['image_url'][0]
        ))
        self.conn.commit()

import json

import simplejson as sjson
import psycopg2
from psycopg2.extras import RealDictCursor


class PostgresWrapper:
    def __init__(self, **args):
        self.user = args.get('user', 'postgres')
        self.password = args.get('password', 'Kulkarni@10')
        self.port = args.get('port', 5432)
        self.dbname = args.get('dbname', 'postgres')
        self.host = args.get('host', 'localhost')
        self.connection = None

    def connect(self):
        pg_conn = psycopg2.connect(
            user=self.user,
            password=self.password,
            port=self.port,
            dbname=self.dbname,
            host=self.host
        )
        self.connection = pg_conn

    def get_json_cursor(self):
        return self.connection.cursor(cursor_factory=RealDictCursor)

    @staticmethod
    def execute_and_fetch(cursor, query):
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res

    def get_json_response(self, query):
        cursor = self.get_json_cursor()
        response = self.execute_and_fetch(cursor, query)
        print(type(response))
        return response
        # return json.dumps(response, indent=2)

    def get_json(self, slotname = 'test_slot'):

        query = "SELECT data FROM pg_logical_slot_get_changes('" + slotname + "', NULL, NULL);"
        # with open('stuff.json', 'w') as json_file:
        #     json.dump(self.get_json_response(query), fp=json_file)
        return self.get_json_response(query)

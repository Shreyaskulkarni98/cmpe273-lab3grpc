import logging
import urllib
import json
from concurrent import futures
import grpc
import pymongo as pymongo
import DBreplicator_pb2
import DBreplicator_pb2_grpc


class ReplicatorService(DBreplicator_pb2_grpc.ReplicatorServiceServicer):
    def Replicate(self, request, context):
        # json_obj = json.loads(request.json_string)
        # print(json_obj['change'][0]['kind'])
        print(request.json_string)
        return DBreplicator_pb2.ReplicateReply(message='hellooo ')

def sent_to_atlas(self):
    #shift main() code here
    return


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DBreplicator_pb2_grpc.add_ReplicatorServiceServicer_to_server(ReplicatorService(), server)
    server.add_insecure_port('localhost:50051')
    print("Replicator is running at port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    # username = urllib.parse.quote_plus("shreyas")
    # password = urllib.parse.quote_plus("Kulkarni@10")
    # client = pymongo.MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0.lgfur.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # db = client['college']
    # col = db['students']
    # data = str([{"data": "{\"change\":[{\"kind\":\"insert\",\"schema\":\"college\",\"table\":\"students\",\"columnnames\":[\"id\",\"first_name\",\"last_name\",\"sjsu_id\",\"email\",\"create_timestamp\",\"update_timestamp\"],\"columntypes\":[\"integer\",\"character varying\",\"character varying\",\"character varying\",\"character varying\",\"timestamp without time zone\",\"timestamp without time zone\"],\"columnvalues\":[25,\"ccc\",\"ddd\",\"111\",\"bbb@gmail.com\",\"2021-09-21 15:35:51.716527\",\"2021-09-21 15:35:51.716527\"]}]}"}])
    # dic = json.loads(data)
    # print(dic)
    # print(client.list_database_names())
    # print(db.list_collection_names())
    serve()

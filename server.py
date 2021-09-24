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
        username = urllib.parse.quote_plus("shreyas")
        password = urllib.parse.quote_plus("Kulkarni@10")
        client = pymongo.MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0.lgfur.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        json_obj = json.loads(request.json_string)
        # print(json_obj)
        if(json_obj['change'][0]['kind'] == 'insert'):
            print("insert operation reached")
            print("Updating schema: " + json_obj['change'][0]['schema'])
            print("Updating table: " + json_obj['change'][0]['table'])
            db = client[json_obj['change'][0]['schema']]
            coll = db[json_obj['change'][0]['table']]
            # print("connected: " + str(coll))

            doc = {}
            for i in range(0, len(json_obj['change'][0]['columnnames'])):
                doc[json_obj['change'][0]['columnnames'][i]] = json_obj['change'][0]['columnvalues'][i]

            coll.insert_one(doc)
            print("Inserted values into MongoDB Atlas: " + str(json_obj['change'][0]['columnvalues']))

        elif(json_obj['change'][0] == []):
            print("delete operation reached")
        else:
            print("I can replicate only insert and delete operations")

        return DBreplicator_pb2.ReplicateReply(message='Duplicated in mogngoDB Atlas: %s' % str(json_obj))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DBreplicator_pb2_grpc.add_ReplicatorServiceServicer_to_server(ReplicatorService(), server)
    server.add_insecure_port('localhost:50051')
    print("Replicator is running at port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

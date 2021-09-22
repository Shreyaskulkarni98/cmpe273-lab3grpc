import logging
from grpc_requests import StubClient
import psycopg2

import DBreplicator_pb2
from wrapper import PostgresWrapper
from DBreplicator_pb2 import DESCRIPTOR
import json
import DBreplicator_pb2_grpc


def run(json_string):
    service_descriptor = DESCRIPTOR.services_by_name['ReplicatorService']
    client = StubClient.get_by_endpoint("localhost:50051", service_descriptors=[service_descriptor])
    # print(client.service_names)
    assert client.service_names == ["ReplicatorService"]
    replicator = client.service("ReplicatorService")

    # json_obj = json.loads(json_string)
    # print(json_obj)
    result = replicator.Replicate(DBreplicator_pb2.ReplicateRequest(json_string=json_string))
    # print(result)


if __name__ == '__main__':
    logging.basicConfig()

    # dbconn = PostgresWrapper()
    # dbconn.connect()
    # json_obj = dbconn.get_json()


import sys
import psycopg2
import psycopg2.extras
import json
from grpc_requests import StubClient
import psycopg2
import DBreplicator_pb2
from DBreplicator_pb2 import DESCRIPTOR

dbname = 'postgres'
user = 'postgres'
password = 'kulkarni@10'


conn = psycopg2.connect('dbname=postgres user=postgres password=Kulkarni@10', connection_factory=psycopg2.extras.LogicalReplicationConnection)
cur = conn.cursor()

try:
    # test_decoding produces textual output
    cur.start_replication(slot_name='pytest6',decode=True)
except psycopg2.ProgrammingError:
    cur.create_replication_slot('pytest6', output_plugin='wal2json')
    cur.start_replication(slot_name='pytest6', decode=True)

def run(json_string):
    service_descriptor = DESCRIPTOR.services_by_name['ReplicatorService']
    client = StubClient.get_by_endpoint("localhost:50051", service_descriptors=[service_descriptor])
    # print(client.service_names)
    assert client.service_names == ["ReplicatorService"]
    replicator = client.service("ReplicatorService")

    result = replicator.Replicate(DBreplicator_pb2.ReplicateRequest(json_string=json_string))
    print(result)


class DemoConsumer(object):
    def __call__(self, msg):
        # msg.payload is a string
        run(msg.payload)
        msg.cursor.send_feedback(flush_lsn=msg.data_start)

democonsumer = DemoConsumer()

print("Starting streaming, press Control-C to end...", file=sys.stderr)
try:
   cur.consume_stream(democonsumer)
except KeyboardInterrupt:
   cur.close()
   conn.close()
   print("The slot 'pytest' still exists. Drop it with "
      "SELECT pg_drop_replication_slot('pytest'); if no longer needed.",
      file=sys.stderr)
   print("WARNING: Transaction logs will accumulate in pg_xlog "
      "until the slot is dropped.", file=sys.stderr)
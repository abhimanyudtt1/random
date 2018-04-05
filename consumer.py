from kafka import KafkaConsumer
import sys
import avro.schema
import avro.io
import io

if len(sys.argv) != 4 :
 print "Syntax error. Syntax : %s <kakfa Topic to be read> <bootstartServer> <schema_path>"
 exit(1)




from pprint import pprint
consumer = KafkaConsumer(sys.argv[1],
bootstrap_servers=['%s:9092' % sys.argv[2]])

consumer.seek_to_beginning()

schema_path="%s" % sys.argv[3]  # This is the schema path for a kafka topic o/p.
schema = avro.schema.parse(open(schema_path).read())
for msg in consumer:
	bytes_reader = io.BytesIO(msg.value)
	decoder = avro.io.BinaryDecoder(bytes_reader)
	reader = avro.io.DatumReader(schema)
	user1 = reader.read(decoder)
	pprint(user1)

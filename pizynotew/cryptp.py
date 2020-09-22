
import base64

def encode(msg):
	msg_bytes = msg.encode('ascii')
	base64_bytes = base64.b64encode(msg_bytes)
	res = base64_bytes.decode('ascii')
	return res
	

#print(type(en))

def decode(msg):
	b64_bytes = msg.encode('ascii')
	msg_bytes = base64.b64decode(b64_bytes)
	res = msg_bytes.decode('ascii')
	return res

#print(decode(encode("Hello World")))



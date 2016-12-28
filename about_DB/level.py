import leveldb
import sys
import struct
db = leveldb.LevelDB('.')


for key,value in db.RangeIter():
	print("key",len(key))
	print("value",len(value))
	print("hex key",struct.pack(str(len(key))+"s",key).encode('hex'))
	print("hex value",struct.pack(str(len(value))+"s",value).encode('hex'))


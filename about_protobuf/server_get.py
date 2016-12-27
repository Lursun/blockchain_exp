#-*- coding: utf-8 -*-　
#!/usr/bin/python
import sys
import io
import threading
import time
import socket 
import message_pb2


def send():
	global s
	data=message_pb2.Person()#[建立]尚未設定Person
	data.name=raw_input("what your name:")#給予姓名
	data.age=int(raw_input("what your age:"))#給予年齡
	send_data=data.SerializeToString();#[序列化]
	s.sendall(send_data)#[送出]

def get():
	global s
	while (True):
		data=message_pb2.Person()#[建立]尚未設定Person
		get_data=s.recv(1024)#[讀取] 最大1024byte
		data.ParseFromString(get_data);#[反序列化]
		print data


if __name__ == "__main__": 
	server= socket.socket(socket.AF_INET,socket.SOCK_STREAM);#總之就是TCP協定 
	try:#例外處理
		server.bind(('', 6666))#使用port 6666
		server.listen(1)#只允許一個連線
		print "please wait connect"
		(s,adr)=server.accept()#[發生連線] 取得連線物件
		
	except:#發生例外
		print "error"
		sys.exit(0)#程式結束

	get_thread=threading.Thread(target = get)#[建立]取得的執行緒
	get_thread.start()#[執行]
	while(True):
		choose=raw_input("choose you want to do\n1.send 2.quit")
		if(choose=="1"):
			send_thread = threading.Thread(target = send)#[建立]取得的執行緒
			send_thread.start()#[執行]
			time.sleep( 1 )    #確保線程thread1已經啟動
			send_thread.join() #[等待]send_thread結束
		elif(choose=="2"):
			s.close()#[關閉]連線
			server.close()#釋放連線資源
			sys.exit(0)#程式結束


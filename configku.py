ENCODING='utf-8'
SIZE=1024
#SERVERMU
#SERVER_IP='192.168.0.100'
SERVER_IP='127.0.0.1'
#SERVER_IP='192.168.115.42'
#192.168.0.100
PORT=10061
WAIT_SERVER_INPUT=7
#MULAI THREAD SEND/REC SOCKET DENGAN CLIENT
TOTAL_CLIENT=1
#KONEKSI JARINGAN
JARINGAN=(SERVER_IP,PORT)
#---PYSERIAL
BAUDRATE=38400
PYSERIAL_COM='COM4'
CONN_SERIAL=(PYSERIAL_COM,BAUDRATE)
ENCODING_FORMAT='ASCII'
FILE_KOMPAS='kompaslog.txt'
WRITE_FILE='w'
READ_FILE='r'
#KOMPAS SETTING
BASE_MUSUH=355
if BASE_MUSUH>180:
	BASE_MARKAS=(BASE_MUSUH-180)
else:
	BASE_MARKAS=(BASE_MUSUH+180)
ERROR_RATE=15
#COM
PYSERIAL_COM='COM4'#KOMPAS
ARDUINO_COM_PORT='COM3'#FIRMATA
#
ENCODING='utf-8'
SIZE=1024
#SERVERMU
#SERVER_IP='192.168.0.101'
SERVER_IP='127.0.0.1'
#SERVER_IP='192.168.115.42'
PORT=10061
WAIT_SERVER_INPUT=7
#MULAI THREAD SEND/REC SOCKET DENGAN CLIENT
TOTAL_CLIENT=2
#KONEKSI JARINGAN
JARINGAN=(SERVER_IP,PORT)
#---PYSERIAL
BAUDRATE=38400
CONN_SERIAL=(PYSERIAL_COM,BAUDRATE)
ENCODING_FORMAT='ASCII'
FILE_KOMPAS='kompaslog.txt'
WRITE_FILE='w'
READ_FILE='r'
#KOMPAS SETTING
global RESET_LOG_KOMPAS,ERROR_RATE,BASE_MUSUH,BASE_MUSUH_MIN,BASE_MUSUH_MAX
RESET_LOG_KOMPAS=4
ERROR_RATE=10

BASE_MUSUH=200
BASE_MUSUH_MIN=(BASE_MUSUH-ERROR_RATE)%360
BASE_MUSUH_MAX=(BASE_MUSUH+ERROR_RATE)%360
if BASE_MUSUH>180:
	BASE_MARKAS=(BASE_MUSUH-180)
else:
	BASE_MARKAS=(BASE_MUSUH+180)
	
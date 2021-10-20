import socket
import threading
import time

ip = '127.0.0.1'
thred_array = []
closed_array = []


def port_scan(ip, port_name):
    global thred_array, closed_array
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connect = sockt.connect((ip, port_name))
        print(f'Порт: {port_name} открыт')
        thred_array.append(port_name)
        sockt.close()
    except:
        print(f'Порт: {port_name} закрыт')
        closed_array.append(port_name)
        sockt.close()


def open_ports():
    global thred_array
    print('Открытые порты: ')
    print(thred_array)


def closed_ports():
    global closed_array
    closed_array.sort()
    print('Закрытые порты: ')
    print(closed_array)


for p_name in range(3000):
    thred = threading.Thread(target=port_scan, args=(ip, p_name))
    thred.start()

time.sleep(3)
sec_thred = threading.Thread(target=open_ports)
sec_thred.start()

thrd_th = threading.Thread(target=closed_ports)
thrd_th.start()

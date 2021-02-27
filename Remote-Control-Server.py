
import socket
import logging
import threading

from mcdreforged.api.decorator import new_thread

PLUGIN_METADATA = {
    'id': 'remote_control',
    'version': '1.0.0',
    'name': 'Remote Control MCDR',
    'author': 'shenjack and DXbai_zhou'
}

@new_thread('contorl_thread')
def dispose_client_request(server, *args, **kargs):
    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ts.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    ts.bind(("127.0.0.1",12212))
    ts.listen(1)
    while True:
        tcp_client, tcp_client_address = ts.accept()
        while True:
            command = tcp_client.recv(1024).decode()
            if command == "exit":
                break
            server.execute(command)


def on_load(server, *args, **kargs):
    logging.debug('onload1')
    dispose_client_request(server)
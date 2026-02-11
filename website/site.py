import socket
import select
from http.server import BaseHTTPRequestHandler,HTTPServer

class APIHandler(BaseHTTPRequestHandler):
    u="username"
    p="password"

if __name__=="__main__":
    listener_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    address_port=("127.0.0.1", 8080)
    listener_socket.bind(address_port)
    listener_socket.listen(1)
    print("Server listening @ 127.0.0.1:8080")

    while True:
        read_ready_sockets, _, _=select.select([listener_socket],[],[],0)
        if read_ready_sockets:
            for ready_socket in read_ready_sockets:
                client_socket, client_address=ready_socket.accept()
                client_msg=client_socket.recv(4096)
                print(f"Client message: {client_msg.decode('utf-8')}")
                client_socket.sendall(
                        bytes(f"""HTTP/1.1 200 OK\r\nContent-type: text/html\r\nSet-Cookie: ServerName=wyattserver\r\r\n
                        <!doctype html>
                        <html>
                            <head/>
                            <body>
                                <h1>Connection to server successful.</h1>
                                <h2>Server address: {address_port[0]}:{address_port[1]}</h2>
                                <h3>Connected through address: {client_address[0]}:{client_address[1]}</h3>
                                <body>
                                    <pre>{client_msg.decode("utf-8")}<pre>
                                </body>
                            </body>
                        </html>
                        \r\n\r\n
                        """, "utf-8")
                    )
                try:
                    client_socket.close()
                except OSError:
                    pass

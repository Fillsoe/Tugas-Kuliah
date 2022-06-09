import socket

def client_program():
    host = socket.gethostname()
    port = 8000  # nomor port server soket

    client_socket = socket.socket()
    client_socket.connect((host, port))  #melakukan koneksi ke server
    print("Terhubung dengan server")
    print("==========================================================")
    print("Selamat datang di server kami")
    message = input(" Masukkan pesan : ")  #menginput pesan

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  #mengirim pesan ke server
        data = client_socket.recv(1024).decode()  #menerima pesan dari server

        print('Pesan dari server : ' + data)  #menampilkan pesan dari server

        message = input(" Masukkan pesan : ")  #menginput pesan lagi

    client_socket.close()  #menutup koneksi dengan server

if __name__ == '__main__':
    client_program()
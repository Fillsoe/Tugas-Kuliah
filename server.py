import socket

def server_program():
    #mendapatkan nama host
    host = socket.gethostname()
    port = 8000  #memulai port dengan angka 8000

    server_socket = socket.socket()  
    server_socket.bind((host, port))  #bind host dan port secara bersamaan

    # konfigurasikan berapa banyak klien yang dapat didengarkan server secara bersamaan
    server_socket.listen(2)
    conn, address = server_socket.accept()  #menerima koneksi baru
    print("Terhubung dari : " + str(address))
    while True:
        #menerima data
        data = conn.recv(1024).decode()
        if not data:
            #jika data tidak masuk, maka terjadi break
            break
        print("Pesan dari client : " + str(data))
        data = input(' Masukkan pesan : ')
        conn.send(data.encode())  #mengirim pesan ke client

    conn.close()  #menutup koneksi dengan client

if __name__ == '__main__':
    server_program()
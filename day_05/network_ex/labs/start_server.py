import socket


def server_program():
    # get the hostname
    host = '127.0.0.1'
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)

    # -------------------------------------------------------------------
    # accept new connection
    
    # print connection details
    

    while True:
        
        # receive data stream. it won't accept data packet greater than 1024 bytes
        
        # if data is not received break
        
        # Print received data
        
        # input the data from the user
        
        
        # send data to the client
        
        
    # ------------------------------------------------------------------------

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
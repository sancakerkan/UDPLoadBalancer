import socket

class UDPLoadBalancer:
    def __init__(self, lb_address, server_addresses):
        self.lb_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.lb_socket.bind(lb_address)  # Bind the socket to the address and port
        self.server_addresses = server_addresses  # List of server addresses
        self.current_server = 0  # Index to keep track of the current server

    def get_next_server_address(self):
        # Get the next server address in a round-robin fashion and update the index
        server_address = self.server_addresses[self.current_server]
        self.current_server = (self.current_server + 1) % len(self.server_addresses)
        return server_address

    def start(self):
        print(f"Load balancer started on {self.lb_socket.getsockname()}")
        try:
            while True:
                # Receive messages from the client
                message, client_address = self.lb_socket.recvfrom(1024)
                server_address = self.get_next_server_address()  # Get the next server
                print(f"Forwarding message to server: {server_address}")

                # Forward the message to the selected server
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                server_socket.sendto(message, server_address)

                # Receive the server's response and forward it back to the client
                server_socket.settimeout(1)  # Set a timeout for receiving response
                try:
                    response, _ = server_socket.recvfrom(1024)
                    self.lb_socket.sendto(response, client_address)
                    print(f"Received and forwarded response from server: {server_address}")
                except socket.timeout:
                    print(f"Timeout while waiting for response from server: {server_address}")

                server_socket.close()

        except KeyboardInterrupt:
            self.lb_socket.close()  # Close the socket when interrupted
            print("Load balancer stopped.")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.lb_socket.close()

if __name__ == "__main__":
    LB_IP = "127.0.0.1"  # IP address for the load balancer
    LB_PORT = 12345  # Port for the load balancer
    LB_ADDRESS = (LB_IP, LB_PORT)

    # Server addresses and ports
    SERVER_ADDRESSES = [
        ('127.0.0.1', 2526),  # Server1
        ('127.0.0.1', 2527),  # Server2
        ('127.0.0.1', 2528),  # Server3
    ]

    # Initialize and start the load balancer
    load_balancer = UDPLoadBalancer(LB_ADDRESS, SERVER_ADDRESSES)
    load_balancer.start()

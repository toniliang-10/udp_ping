import sys
import socket

def main():
    """Main server function - binds UDP socket and echoes datagrams."""
    
    # Validate command-line arguments (5 points)
    # - Check if exactly 2 arguments are provided (host and port)
    # - Print usage message if incorrect number of arguments
    # - Usage: python udp_server.py <host> <port>
    # Example: python udp_server.py 127.0.0.1 9999
    if len(sys.argv) != 3:
        # Print usage message and exit with error code 1
        print("Usage: python udp_server.py <host> <port>")
        print("Example: python udp_server.py 127.0.0.1 9999")
        sys.exit(1)

    
    host = sys.argv[1]
    
    # TODO: Validate and convert port number (5 points)
    # - Convert port from string to integer
    # - Check if port is between 1 and 65535
    # - Print error message for invalid port
    # - Exit with error code 1 for invalid input
    try:
        port = int(sys.argv[2])
        # Validate port range
        if not (1 <= port <= 65535):
            # Print error and exit
            print(f"Error: Port must be between 1 and 65535, got {port}")
            sys.exit(1)

    except ValueError:
        # Handle non-integer port
        print(f"Error: Port must be an integer, got '{sys.argv[2]}'")
        sys.exit(1)

    
    # TODO: Create UDP socket (5 points)
    # - Use socket.AF_INET for IPv4
    # - Use socket.SOCK_DGRAM for UDP
    # - Handle socket creation errors
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # TODO: Create UDP socket here
    except socket.error as e:
        # TODO: Print error message and exit
        print(f"Error: Could not create socket: {e}")
        sys.exit(1)

    
    # TODO: Bind socket to host:port (5 points)
    # - Bind the socket to the specified host and port
    # - Print error message if bind fails
    # - Print success message when bound
    try:
        # TODO: Bind socket here
        server_socket.bind((host, port))
        # TODO: Print listening message
        print(f"UDP Echo Server listening on {host}:{port}")
        print("Press Ctrl+C to stop the server")
    except socket.error as e:
        # TODO: Print error, close socket, and exit
        print(f"Error: Could not bind to {host}:{port}: {e}")
        server_socket.close()
        sys.exit(1)

    
    # TODO: Main echo loop 
    # - Create infinite loop to handle datagrams
    # - Use recvfrom() to receive data and client address
    # - Use sendto() to echo exact data back to client
    # - Handle KeyboardInterrupt to stop gracefully
    try:
        while True:
            try:
                # TODO: Receive datagram (max 4096 bytes recommended)
                data, client_address = server_socket.recvfrom(4096)
                # TODO: Print received message info

                # TODO: Echo exact data back to sender
                server_socket.sendto(data, client_address)
                # TODO: Optional - Print echo confirmation
                print(f"Echoed {len(data)} bytes to {client_address}")
            except socket.error as e:
                # TODO: Handle socket errors within the loop
                print(f"Error: {e}")
                continue
                
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    finally:
        # TODO: Close socket before exiting
        server_socket.close()
        print("Socket closed")

if __name__ == "__main__":
    main()

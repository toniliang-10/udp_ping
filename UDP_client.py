import sys
import socket
import time

def validate_arguments():
    """Parse and validate command-line arguments (15 points)"""
    # The client should accept exactly 5 arguments:
    # python udp_client.py <server_host> <server_port> <N> <interval> <timeout>
    
    # Check for exactly 6 arguments (script name + 5 parameters)
    # If incorrect, print usage message and exit
    if len(sys.argv) != 6:
        # Print detailed usage message
        print("Usage: python udp_client.py <server_host> <server_port> <N> <interval> <timeout>")
        print("Example: python udp_client.py 127.0.0.1 9999 10 0.5 1.0")
        sys.exit(1)
    
    server_host = sys.argv[1]

    # Validate server_port (integer between 1-65535)
    try:
        server_port = int(sys.argv[2])
        if not (1 <= server_port <= 65535):
            print(f"Error: server_port must be between 1 and 65535, got {server_port}")
            sys.exit(1)
    except ValueError:
        print(f"Error: server_port must be an integer, got '{sys.argv[2]}'")
        sys.exit(1)

    # Validate N (integer >= 1)
    try:
        N = int(sys.argv[3])
        if N < 1:
            print(f"Error: N must be >= 1, got {N}")
            sys.exit(1)
    except ValueError:
        print(f"Error: N must be an integer, got '{sys.argv[3]}'")
        sys.exit(1)

    # Validate interval (float > 0)
    try:
        interval = float(sys.argv[4])
        if interval <= 0:
            print(f"Error: interval must be > 0, got {interval}")
            sys.exit(1)
    except ValueError:
        print(f"Error: interval must be a number, got '{sys.argv[4]}'")
        sys.exit(1)

    # Validate timeout (float > 0)
    try:
        timeout = float(sys.argv[5])
        if timeout <= 0:
            print(f"Error: timeout must be > 0, got {timeout}")
            sys.exit(1)
    except ValueError:
        print(f"Error: timeout must be a number, got '{sys.argv[5]}'")
        sys.exit(1)

    return server_host, server_port, N, interval, timeout

def create_ping_message(seq_num):
    """Create ping message (10 points)"""
    # Construct a ping message with sequence number and timestamp
    # Format: "PING <sequence_number> <timestamp>"
    # Example: "PING 1 1681234567.891234"
    
    # Get current time with microsecond precision    
    timestamp = time.time()
    # Format the message string    
    message = f"PING {seq_num} {timestamp}"
    # Encode to bytes for UDP transmission    
    return message.encode()

def main():
    """Main client function - sends pings and collects statistics."""
    # Parse and validate arguments
    server_host, server_port, N, interval, timeout = validate_arguments()
    print(f"PING {server_host}:{server_port}")
    print(f"Sending {N} ping messages with {interval}s interval, {timeout}s timeout...")

    # Statistics tracking
    packets_sent = 0
    packets_received = 0
    rtt_times = []  # Store RTTs in seconds
    
    # Create UDP socket and set timeout (10 points)
    try:
        # Create UDP socket (AF_INET, SOCK_DGRAM)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set socket timeout (in seconds)        
        client_socket.settimeout(timeout)
    except socket.error as e:
        print(f"Socket creation failed: {e}")
        sys.exit(1)
    
    # Main ping loop 
    for seq_num in range(1, N + 1):
        # Sleep between pings (except before first one)
        if seq_num > 1:
            # Sleep for 'interval' seconds
            time.sleep(interval)
        
        # Create ping message        
        ping_message = create_ping_message(seq_num)
        # Record send time (use time.perf_counter() for precision)        
        send_time = time.perf_counter()
        try:
            # Send ping message to server
            client_socket.sendto(ping_message, (server_host, server_port))
            packets_sent += 1

            # Try to receive response with timeout
            try:
                # Receive response (max 4096 bytes recommended)
                response, addr = client_socket.recvfrom(4096)
                # Calculate RTT
                recv_time = time.perf_counter()
                rtt = recv_time - send_time
                # Verify response (optional but good practice)
                # - Check if response matches what we sent
                # - You can compare response == ping_message
                # - Or extract sequence number from response
                if response != ping_message:
                    print(f"\tWarning - (PING #{seq_num}): response mismatch ")
                # Update statistics             
                packets_received += 1
                rtt_times.append(rtt)
                # Print success message with RTT in millisecond   
                print(f"PING #{seq_num}: Reply from {server_host}:{server_port}, RTT={rtt * 1000:.3f} ms")
            except socket.timeout:
                # Handle timeout - print timeout message
                print(f"PING #{seq_num}: Request timed out")
        except socket.error as e:
            # Handle other socket error
            print(f"PING #{seq_num}: Socket error: {e}")

    # Close socket
    client_socket.close()
    # Calculate and display statistics (10 points)    
    # Print packets transmitted and received    
    # Calculate and print packet loss percentage    
    loss_pct = ((packets_sent - packets_received) / packets_sent * 100) if packets_sent > 0 else 0.0
    print("--- Ping Statistics ---")
    print(f"{packets_sent} packets transmitted, {packets_received} packets received, {loss_pct:.1f}% packet loss")

    # Calculate and print RTT statistics (if any successful pings)        
        # Calculate min, avg, max RTT
    if rtt_times:       #if there are RTTs from sent to received 
        min_rtt = min(rtt_times) * 1000
        avg_rtt = (sum(rtt_times) / len(rtt_times)) * 1000
        max_rtt = max(rtt_times) * 1000
        print("Round-trip times (ms):")
        print(f"Minimum = {min_rtt:.3f} ms")
        print(f"Average = {avg_rtt:.3f} ms")
        print(f"Maximum = {max_rtt:.3f} ms")
if __name__ == "__main__":
    main()



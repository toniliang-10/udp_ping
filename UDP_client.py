import sys
import socket
import time

def validate_arguments():
    """TODO: Parse and validate command-line arguments (15 points)"""
    # The client should accept exactly 5 arguments:
    # python udp_client.py <server_host> <server_port> <N> <interval> <timeout>
    
    # TODO: Check for exactly 6 arguments (script name + 5 parameters)
    # If incorrect, print usage message and exit
    if len(sys.argv) != 6:
        # TODO: Print detailed usage message
        
        sys.exit(1)
    
    server_host = sys.argv[1]
    # TODO: Validate server_port (integer between 1-65535)
    try:
        server_port = int(sys.argv[2])    
    # TODO: Validate N (integer >= 1)    
    # TODO: Validate interval (float > 0)
    try:
    
    # TODO: Validate timeout (float > 0)
    try:
    return server_host, server_port, N, interval, timeout

def create_ping_message(seq_num):
    """TODO: Create ping message (10 points)"""
    # Construct a ping message with sequence number and timestamp
    # Format: "PING <sequence_number> <timestamp>"
    # Example: "PING 1 1681234567.891234"
    
    # TODO: Get current time with microsecond precision    
    # TODO: Format the message string    
    # TODO: Encode to bytes for UDP transmission    

def main():
    """Main client function - sends pings and collects statistics."""
    # Parse and validate arguments    
    # Statistics tracking
    packets_sent = 0
    packets_received = 0
    rtt_times = []  # Store RTTs in seconds
    
    # TODO: Create UDP socket and set timeout (10 points)
    try:
        # TODO: Create UDP socket (AF_INET, SOCK_DGRAM)
        
        # TODO: Set socket timeout (in seconds)        
    except socket.error as e:
        print(f"Socket creation failed: {e}")
        sys.exit(1)
    
    # TODO : Main ping loop 
    for seq_num in range(1, N + 1):
        # TODO: Sleep between pings (except before first one)
        if seq_num > 1:
            # TODO: Sleep for 'interval' seconds
            pass
        
        # TODO: Create ping message        
        # TODO: Record send time (use time.perf_counter() for precision)        
        try:
            # TODO: Send ping message to server
            
            # TODO: Try to receive response with timeout
            try:
                # TODO: Receive response (max 4096 bytes recommended)
                # TODO: Calculate RTT
                # TODO: Verify response (optional but good practice)
                # - Check if response matches what we sent
                # - You can compare response == ping_message
                # - Or extract sequence number from response
                # TODO: Update statistics                
                # TODO: Print success message with RTT in millisecond   
               # TODO: Handle timeout - print timeout message
                # TODO: Handle other socket error
    # TODO: Close socket
    # TODO : Calculate and display statistics (10 points)    
    # TODO: Print packets transmitted and received    
    # TODO: Calculate and print packet loss percentage    
    # TODO: Calculate and print RTT statistics (if any successful pings)        
        # TODO: Calculate min, avg, max RTT
if __name__ == "__main__":
    main()

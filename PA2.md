PA2 – UDP Ping and RTT Measurement

Overview (100 points total)
Objective: Implement a UDP-based ping tool and echo server to demonstrate connectionless
communication, packet loss simulation, and network latency measurement. This assignment
teaches UDP socket programming, statistical analysis of network performance, and handling of
unreliable datagram delivery.

Learning Goals:
● Create UDP client/server using socket.AF_INET, SOCK_DGRAM
● Understand connectionless communication vs TCP's connection-oriented model
● Measure round-trip time (RTT) using precise timestamps
● Handle packet loss and timeouts in unreliable protocols
● Collect and analyze network performance statistics
● Implement robust error handling for datagram protocols

Protocol Specification
UDP Ping Protocol
Client Server
| ----- Ping #1 -----> |
| <---- Echo #1 ----- | (if received)
| ----- Ping #2 -----> |
| (lost) |
| ----- Ping #3 -----> |
| <---- Echo #3 ----- |
Key characteristics:
● Connectionless: No handshake, each datagram is independent
● Unreliable: Packets may be lost, duplicated, or arrive out-of-order
● Stateless server: Echoes exact payload without tracking sessions
● Timeout-based: Client waits finite time for each response

Detailed Requirements
1. Command-line Interface

Server:
python udp_server.py <host> <port>
Requirements:
● Accept exactly 2 positional arguments
● Bind to specified host:port
● Handle invalid port numbers gracefully


Client:
python udp_client.py <server_host> <server_port> <N> <interval> <timeout>
Parameters:
● server_host: Server's hostname or IP address
● server_port: Server's UDP port number
● N: Number of ping messages to send (integer ≥ 1)
● interval: Time between pings in seconds (float > 0)
● timeout: Time to wait for each reply in seconds (float > 0)
Requirements:
● Validate all 5 arguments with helpful error messages
● Convert numeric arguments to appropriate types
● Check for valid ranges (e.g., positive N, positive interval/timeout)


2. Server Implementation
Core functionality:
● Create UDP socket with socket.SOCK_DGRAM
● Bind to specified host and port
● Infinite loop to receive and echo datagrams
● Echo exact payload bytes back to sender
● Handle multiple clients simultaneously (implicitly via UDP)
Expected output:
text
UDP Echo Server listening on 127.0.0.1:9999
Echoed 64 bytes to ('127.0.0.1', 54321)
Echoed 64 bytes to ('127.0.0.1', 54321)
...


3. Client Implementation
Ping Packet Format:

PING sequence_number timestamp

Where:
● sequence_number: Integer from 1 to N
● timestamp: Client's send time (e.g., 1681234567.891234)
Client Workflow:
1. Setup:
o Create UDP socket
o Set socket timeout (in seconds)
o Initialize statistics counters
2. Ping Loop (N iterations):
o Sleep for interval seconds (except before first ping)
o Construct ping message with sequence number and send time
o Record send timestamp with microsecond precision
o Send to server
o Wait for reply with timeout
o If reply received:
    ▪ Calculate RTT = receive_time - send_time
    ▪ Validate echo matches sent payload
    ▪ Print success message with RTT
o If timeout:
    ▪ Print timeout message
    ▪ Count as lost packet
3. Statistics Display:
o Total packets sent
o Total packets received
o Packet loss percentage
o Minimum RTT
o Average RTT
o Maximum RTT
o All times in milliseconds with appropriate precision


File Structure
udp_ping/
├── udp_server.py # UDP echo server (30 pts)
├── udp_client.py # UDP ping client (70 pts)


Running the Assignment
Terminal 1: Start Server

python udp_server.py 127.0.0.1 9999

Output:
UDP Echo Server listening on 127.0.0.1:9999

Terminal 2: Run Client

python udp_client.py 127.0.0.1 9999 10 0.5 1.0

This sends 10 pings, with 0.5 seconds between each, waiting up to 1.0 second for each reply.
Expected Client Output:
PING 127.0.0.1:9999
Sending 10 ping messages with 0.5s interval, 1.0s timeout...
PING #1: Reply from 127.0.0.1:9999, RTT=1.234 ms
PING #2: Reply from 127.0.0.1:9999, RTT=1.567 ms
PING #3: Request timed out
PING #4: Reply from 127.0.0.1:9999, RTT=1.891 ms
...
PING #10: Reply from 127.0.0.1:9999, RTT=2.345 ms
--- Ping Statistics ---
10 packets transmitted, 8 packets received, 20.0% packet loss
Round-trip times (ms):
Minimum = 1.234 ms
Average = 1.789 ms
Maximum = 2.345 ms


Detailed TODO Breakdown
Server (udp_server.py) - 30 points
1. Argument Parsing (5 pts)
o Parse host and port from command line
o Validate port number (1- 65535)
2. Socket Setup (10 pts)
o Create UDP socket (socket.SOCK_DGRAM)
o Bind to specified host and port
o Print listening message
3. Echo Loop (15 pts)
o Infinite loop receiving datagrams
o Extract client address from recvfrom()
o Echo exact payload back using sendto()
o Optional: Log each echo operation
Client (udp_client.py) - 70 points
1. Argument Processing (10 pts)
o Parse and validate 5 command-line arguments
o Convert to appropriate types (int, float)
o Range validation for all numeric parameters
2. Socket Configuration (5 pts)
o Create UDP socket
o Set timeout using socket.settimeout()
3. Ping Message Construction (10 pts)
o Format: PING sequence_number timestamp
o Include microsecond precision in timestamp
o Encode to bytes for transmission
4. Main Ping Loop (25 pts)
o Loop N times with proper interval timing
o Record precise send timestamp (time.time() or time.perf_counter())
o Send datagram, wait for reply with timeout
o Calculate RTT for successful replies
o Handle timeout exceptions
o Print real-time status for each ping
5. Statistics Calculation (10 pts)
o Count sent/received/lost packets
o Calculate loss percentage
o Compute min, avg, max RTT from successful pings
o Handle case with 0 successful replies
6. Results Display (10 pts)
o Format statistics clearly
o Display times in milliseconds
o Round to appropriate precision (e.g., 3 decimal places)

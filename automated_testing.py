import subprocess
import time
import socket

def test_basic():
    """Basic functionality test"""
    print("Testing UDP Ping assignment...")
    print("-" * 40)
    
    # Test 1: Check both files exist
    files = ['udp_server.py', 'udp_client.py']
    for f in files:
        try:
            with open(f, 'r') as file:
                print(f"✅ Found {f}")
        except FileNotFoundError:
            print(f"❌ Missing {f}")
            return False
    
    # Test 2: Check server starts
    print("\nStarting server...")
    server = subprocess.Popen(['python', 'udp_server.py', '127.0.0.1', '9999'],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    time.sleep(1)
    
    if server.poll() is not None:
        print("❌ Server didn't start properly")
        return False
    print("✅ Server started")
    
    # Test 3: Quick client test
    print("\nRunning client test...")
    try:
        client = subprocess.run(['python', 'udp_client.py', '127.0.0.1', '9999', '3', '0.2', '0.5'],
                               capture_output=True,
                               text=True,
                               timeout=3)
        
        print("Client output preview:")
        print("-" * 30)
        for line in client.stdout.split('\n')[:10]:  # Show first 10 lines
            if line:
                print(f"  {line}")
        print("-" * 30)
        
        if client.returncode == 0:
            print("✅ Client completed successfully")
        else:
            print(f"❌ Client exited with code {client.returncode}")
            
    except subprocess.TimeoutExpired:
        print("❌ Client timed out")
    
    # Cleanup
    server.terminate()
    server.wait()
    
    print("\n" + "=" * 40)
    print("Basic test complete!")
    print("For full testing, run: python test_udp_ping.py")
    
    return True

if __name__ == "__main__":
    test_basic()

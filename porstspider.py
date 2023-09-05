import socket
print("")

def scan_port(target_ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        # Attempt to connect to the target IP and port
        result = sock.connect_ex((target_ip, port))

        # Check if the connection was successful
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        # Close the socket
        sock.close()

    except socket.error:
        print(f"Could not connect to {target_ip}:{port}")

def main():
    target_ip = input("Enter the target IP address: ")
    target_ports = input("Enter the ports to scan (comma-separated): ").split(',')

    for port_str in target_ports:
        port = int(port_str.strip())
        scan_port(target_ip, port)

if __name__ == "__main__":
    main()

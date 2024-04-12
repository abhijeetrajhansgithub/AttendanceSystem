import socket


def find_available_ports(start_port, end_port):
    available_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()

        if result != 0:  # Port is available if connect_ex returns a non-zero result
            available_ports.append(port)

    return available_ports


# Specify the range of ports to check
start_port = 8000
end_port = 8100

# Find available ports in the specified range
available_ports = find_available_ports(start_port, end_port)

if available_ports:
    print(f"Available ports: {available_ports}")
else:
    print("No available ports in the specified range.")

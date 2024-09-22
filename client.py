import socket

def query_dns_server():
    # Set up the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # Prompt the user for hostname and query type
        query_input = input("Enter hostname and query type (e.g., deakin.edu,A): ")
        try:
            hostname, query_type = query_input.split(',')
        except ValueError:
            print("Invalid input format. Use 'hostname,query_type'")
            continue

        # Validate query type
        if query_type.upper() not in ('A', 'CNAME'):
            print("Invalid query type. Use 'A' or 'CNAME'")
            continue

        # Send the DNS query to the server
        client_socket.sendto(query_input.encode(), ('localhost', 53))

        # Receive the server's response
        response, _ = client_socket.recvfrom(1024)
        print(f"Server response: {response.decode()}")

        # Ask user if they want to continue
        choice = input("Press 'y' to send another query or any other key to exit: ")
        if choice.lower() != 'y':
            break

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    query_dns_server()

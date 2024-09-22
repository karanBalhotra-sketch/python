import socket

# DNS records with fake data
dns_records = {
    'deakin.edu': {'A': '192.168.1.1'},
    'www.deakin.com': {'A': '192.168.1.2'},
    'mail.outlook.com': {'A': '192.168.1.3'},
    'alias.deakin.edu': {'CNAME': 'www.deakin.edu.au'}
}

def resolve_A_record(hostname):
    """
    Resolve A record for the given hostname.
    """
    if hostname in dns_records and 'A' in dns_records[hostname]:
        return dns_records[hostname]['A']
    else:
        return "Host not found"

def resolve_CNAME_record(hostname):
    """
    Resolve CNAME record for the given hostname.
    """
    if hostname in dns_records and 'CNAME' in dns_records[hostname]:
        return dns_records[hostname]['CNAME']
    else:
        return "Host not found"

def create_dns_response(response_data):
    """
    Create DNS response message.
    """
    return response_data

def reply_to_client(response_message, client_address, server_socket):
    """
    Send response message back to the client.
    """
    server_socket.sendto(response_message.encode(), client_address)

def start_dns_server():
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 53))  # Using port 5353 for testing

    print("DNS server is operational...")

    while True:
        # Receive data from the client
        data, client_address = server_socket.recvfrom(1024)
        query = data.decode()

        # Print the received query
        print("Query received:", query)

        # Parse the query to get hostname and query type
        query_parts = query.split(',')
        if len(query_parts) != 2:
            # Error for invalid format
            response_message = "Invalid query format. Use 'hostname,query_type'"
            reply_to_client(response_message, client_address, server_socket)
            continue

        hostname, query_type = query_parts

        # Handle the query based on type
        if query_type == 'A':
            response_data = resolve_A_record(hostname)
        elif query_type == 'CNAME':
            response_data = resolve_CNAME_record(hostname)
        else:
            # Error for unknown query type
            response_message = "Unsupported query type. Use 'A' or 'CNAME'"
            reply_to_client(response_message, client_address, server_socket)
            continue

        # Create DNS response message
        response_message = create_dns_response(response_data)

        # Send response to the client
        reply_to_client(response_message, client_address, server_socket)

if __name__ == "__main__":
    start_dns_server()

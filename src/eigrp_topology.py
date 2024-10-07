from netmiko import ConnectHandler

def fetch_eigrp_topology(ip, username, password):
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': username,
        'password': password
    }
    
    try:
        connection = ConnectHandler(**device)
        output = connection.send_command("show ip eigrp topology")
        print(output)
        return output
    except Exception as e:
        print(f"Error: {e}")

# Example Usage
if __name__ == "__main__":
    fetch_eigrp_topology('192.168.1.1', 'admin', 'password')

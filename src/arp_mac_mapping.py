from netmiko import ConnectHandler

def fetch_arp_mac(ip, username, password):
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': username,
        'password': password
    }
    
    try:
        connection = ConnectHandler(**device)
        output = connection.send_command("show mac address-table")
        print(output)
        return output
    except Exception as e:
        print(f"Error: {e}")

# Example Usage
if __name__ == "__main__":
    fetch_arp_mac('192.168.1.1', 'admin', 'password')

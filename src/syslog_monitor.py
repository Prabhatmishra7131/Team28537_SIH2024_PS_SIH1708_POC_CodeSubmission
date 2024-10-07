from syslog_parser import SyslogMessage, parse_message

def monitor_syslog(log_file):
    try:
        with open(log_file, 'r') as f:
            for line in f:
                syslog_msg = parse_message(line)
                print(f"Timestamp: {syslog_msg.timestamp} - Message: {syslog_msg.message}")
    except Exception as e:
        print(f"Error reading syslog: {e}")

# Example Usage
if __name__ == "__main__":
    monitor_syslog('path_to_syslog_file')

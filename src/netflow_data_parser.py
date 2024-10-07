import pyNetFlow

def parse_netflow(file_path):
    try:
        flows = pyNetFlow.NetFlow(file_path)
        for flow in flows:
            print(f"Source: {flow.srcaddr} -> Destination: {flow.dstaddr}")
    except Exception as e:
        print(f"NetFlow parsing error: {e}")

# Example Usage
if __name__ == "__main__":
    parse_netflow('path_to_netflow_file')

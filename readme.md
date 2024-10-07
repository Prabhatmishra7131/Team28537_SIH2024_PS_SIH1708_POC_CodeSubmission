# Team28537_SIH2024_PS_SIH1708_POC_CodeSubmission

# **TopoSecure - Secure EIGRP-Based Network Topology Discovery Tool**

## **Project Overview**
**TopoSecure** is a secure, real-time, and scalable network topology discovery tool designed for SCADA systems using the Enhanced Interior Gateway Routing Protocol (EIGRP). It eliminates the reliance on insecure protocols like Cisco Discovery Protocol (CDP) and Link Layer Discovery Protocol (LLDP), leveraging secure methods such as SNMPv3, ARP/MAC tables, NetFlow, routing protocol data, and syslog data to map network devices and connections.

## **Key Features**
- **Secure and Real-Time Discovery**: Uses SNMPv3, ARP/MAC tables, NetFlow, and EIGRP routing information to create secure, dynamic topology maps.
- **No CDP/LLDP Dependence**: Avoids vulnerabilities associated with CDP/LLDP.
- **Scalable**: Efficient for both small and large SCADA networks.
- **Security-Focused**: Identifies unauthorized devices and changes in network topology.

## **Project Structure**
The repository is organized as follows:

```
TopoSecure/
│
├── src/
│   ├── snmp_discovery.py
│   ├── arp_mac_mapping.py
│   ├── netflow_data_parser.py
│   ├── eigrp_topology.py
│   ├── syslog_monitor.py
│   ├── network_visualization.py
│   └── main.py
│
├── README.md
├── requirements.txt
└── LICENSE
```

## **Folder and Code Descriptions**

### **1. `src/snmp_discovery.py`**
This file contains the code for secure **SNMPv3 polling** and traps, which are used to gather device information such as IP addresses, system details, and interface statuses securely.
- **Functionality**: Establishes SNMPv3 sessions, polls devices, and collects traps for topology discovery.
- **Tech Stack**: Uses the `pysnmp` library.

### **2. `src/arp_mac_mapping.py`**
This file is responsible for **mapping ARP/MAC tables** to build a Layer 2 physical topology.
- **Functionality**: Analyzes ARP and MAC tables to identify the physical links between devices.
- **Tech Stack**: Utilizes `Netmiko` to interact with network devices.

### **3. `src/netflow_data_parser.py`**
This code parses **NetFlow data** to map the logical connections and traffic flows at Layer 3.
- **Functionality**: Collects and parses NetFlow records to monitor IP traffic and connections.
- **Tech Stack**: Implements `pyNetFlow`.

### **4. `src/eigrp_topology.py`**
This file gathers **EIGRP routing table information** to map logical connections between Layer 3 devices.
- **Functionality**: Queries EIGRP-enabled devices for routing table data, creating logical topologies.
- **Tech Stack**: Uses `Netmiko` for device interaction.

### **5. `src/syslog_monitor.py`**
This script continuously monitors **Syslog data** to track real-time network events and update the topology dynamically.
- **Functionality**: Collects and parses syslog events, detecting device or connection changes.
- **Tech Stack**: Leverages the `syslog-parser` library.

### **6. `src/network_visualization.py`**
This file provides a **visual representation of the network topology** using libraries like **NetworkX** and **D3.js**.
- **Functionality**: Creates a dynamic network graph, illustrating device connections and updating as changes occur.
- **Tech Stack**: Combines `NetworkX` for graph generation and `D3.js` for visualization.

### **7. `src/main.py`**
This is the **main execution file** that integrates all the above components to form the full topology discovery system.
- **Functionality**: Coordinates SNMPv3, ARP/MAC table collection, NetFlow analysis, EIGRP data parsing, and real-time Syslog monitoring to create and update the network map.

## **Getting Started**

### **Prerequisites**
Before running the project, ensure you have the following installed:

- Python 3.x
- Required Python packages (install using `pip`):
  ```
  pip install -r requirements.txt
  ```

### **Installation**
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/TopoSecure.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### **Running the Project**
- To start the topology discovery process, run the `main.py` file:
  ```
  python src/main.py
  ```

### **Configuration**
Ensure you configure SNMPv3 credentials, device IPs, and other necessary parameters in the respective files before running the tool. Example configurations for SNMPv3 and NetFlow should be included within the respective Python files.

## **References**
- RFCs for SNMPv3, EIGRP, and NetFlow.
- Open-source libraries: `pysnmp`, `Netmiko`, `pyNetFlow`, and `syslog-parser`.
- Research on SCADA security guidelines.

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

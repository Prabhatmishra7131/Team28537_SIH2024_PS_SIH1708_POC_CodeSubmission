from pysnmp.hlapi import *

def snmp_v3_poll(ip, user, auth_key, priv_key, oid):
    try:
        iterator = getCmd(
            SnmpEngine(),
            UsmUserData(user, auth_key, priv_key),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )
        
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        
        if errorIndication:
            print(f"SNMP Error: {errorIndication}")
        elif errorStatus:
            print(f"{errorStatus.prettyPrint()} at {errorIndex}")
        else:
            for varBind in varBinds:
                print(f'{varBind[0]} = {varBind[1]}')
    
    except Exception as e:
        print(f"Exception occurred: {e}")

# Example Usage
if __name__ == "__main__":
    snmp_v3_poll('192.168.1.1', 'snmp_user', 'auth_key', 'priv_key', '1.3.6.1.2.1.1.1.0')

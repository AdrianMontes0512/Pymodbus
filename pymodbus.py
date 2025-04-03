import time
from pymodbus.client import ModbusTcpClient
from pymodbus.framer.rtu_framer import ModbusRtuFramer

HOST = ""
PORT = 

client = ModbusTcpClient(HOST, port=PORT, framer=ModbusRtuFramer)
client.connect()

try:
    while True:
        response = client.read_holding_registers(address=0, count=1, unit=1)
        
        # Intentamos acceder a los registros
        try:
            valor = response.registers[0]
            print("Valor de resistencia:", valor)
        except:
            # Si hay un error (por ejemplo, ModbusIOException),
            # ignoramos este ciclo y seguimos
            pass
        
        time.sleep(3)

except KeyboardInterrupt:
    print("Cerrando conexión...")

finally:
    client.close()

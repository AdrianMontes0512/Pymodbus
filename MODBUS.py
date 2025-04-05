import time
from pymodbus.client import ModbusTcpClient
from pymodbus.framer.rtu_framer import ModbusRtuFramer

HOST = "192.168.0.234"
PORT = 4196

client = ModbusTcpClient(HOST, port=PORT, framer=ModbusRtuFramer)
client.connect()

try:
    while True:
        response = client.read_holding_registers(address=1, count=1, unit=1)
        try:
            valor = response.registers[0]
            print(f"Valor de resistencia: {valor/100}Ω")
        except:
            pass

        time.sleep(0)

except KeyboardInterrupt:
    print("Cerrando conexión...")

finally:
    client.close()
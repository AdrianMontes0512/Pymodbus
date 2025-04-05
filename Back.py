from flask import Flask, request, jsonify
from flask_cors import CORS
from pymodbus.client import ModbusTcpClient
from pymodbus.framer.rtu_framer import ModbusRtuFramer

app = Flask(__name__)
CORS(app)

@app.route('/sensor-data', methods=['POST'])
def get_sensor_data():
    try:
        data = request.json
        ip = data.get("ip")
        port = int(data.get("port"))

        if not ip or not port:
            return jsonify({"error": "Faltan IP o puerto"}), 400

        client = ModbusTcpClient(ip, port=port, framer=ModbusRtuFramer)
        client.connect()

        response = client.read_holding_registers(address=1, count=1, unit=1)

        if not response.isError():
            valor = response.registers[0] / 100
            client.close()
            return jsonify({"valor": f"{valor} Ω"})
        else:
            client.close()
            return jsonify({"error": "Error al leer datos del sensor"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
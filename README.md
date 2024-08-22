# Usage

This lib allow to connect a Growatt hybrid inverter and retrieve some datas via usb/modbus.

It also provide a command-line command to query the inverter

# Command Line example :
``` $ growatt -d /dev/ttyUSB1
{'GRID_VOLTAGE': 0.0, 'GRID_FREQUENCY': 0.0, 'GRID_ACTIVE_POWER': 0.0, 'GRID_APP_POWER': 0.0}
{'AC_OUTPUT_VOLTAGE': 229.4, 'AC_OUTPUT_CURRENT': 1.4, 'AC_OUTPUT_FREQUENCY': 49.99, 'AC_OUTPUT_ACTIVE_POWER': 262.0, 'AC_OUTPUT_APP_POWER': 321.0, 'AC_OUTPUT_LOAD_PERCENT': 5.2}
{'BAT_VOLTAGE': 52.39, 'BAT_CAPACITY': 100, 'BAT_WATT': 324.0, 'BAT_CHARGE_CURRENT': 0.0, 'BAT_DISCHARGE_CURRENT': 6.2}
{'BUS_VOLTAGE': 418.9}
{'INV_TEMP': 30.8, 'DCDC_TEMP': 25.4, 'BUCK1_TEMP': 26.2, 'BUCK2_TEMP': 31.2}
{'PV1_INPUT_POWER': 0.0, 'PV2_INPUT_POWER': 0.0, 'PV1_INPUT_VOLTAGE': 0.0, 'PV2_INPUT_VOLTAGE': 0.0}
{'FAN_SPEED_MPPT': 0, 'FAN_SPEED_INV': 26}
```

# Python Example :
```from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from growatt import Growatt

client = ModbusClient(method='rtu', port="/dev/ttyUSB0", baudrate=9600, stopbits=1, parity='N', bytesize=8, timeout=1)
client.connect()
inverter = Growatt(client,"Inverter",1)
# Read inverter's settings and display them
inverter.readSettings()
settings = inverter.getAllSettings()
print("==== Settings ====")
for i in settings :
  print ('%02d = %-30s : %s' % (i,'%s %s' % (settings[i]['value'],settings[i]['unit']),settings[i]['description']))
# Read inverter's status and display them
inverter.readStatus()
print("==== Status ====")
status = inverter.getAllStatus()
for i in status :
  print ('%02d = %-30s : %s' % (i,'%s %s' % (status[i]['value'],status[i]['unit']),status[i]['description']))

print("==== Advanced ====")
# Some more specific functions
print (inverter.getInfosGrid())
print (inverter.getInfosOutput())
print (inverter.getInfosBattery())
print (inverter.getInfosBus())
print (inverter.getInfosTemp())
print (inverter.getInfosPV())
print (inverter.getInfosFan())
```





# Improvements
Please note that some input registers lack of documentation. The following input registers have been deducted by observation :
* 83 : Battery Charge Current
* 84 : Battery Discharge Current
* 90 : Probably Total Battery Charge Current (sum of all inverters)

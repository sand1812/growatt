from pymodbus.client.sync import ModbusSerialClient as ModbusClient
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

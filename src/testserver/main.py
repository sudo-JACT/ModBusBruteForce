from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

server = ModbusServer("127.0.0.1",12345,no_block=True)

try:
    print("Starting server...")
    server.start()
    print("Server is running...")
    state=[0]
    while True:
        DataBank.set_words(0, [int(uniform(0,200))])
        DataBank.set_words(1, [int(uniform(0,200))])
        DataBank.set_words(2, [int(uniform(0,200))])
        DataBank.set_words(0, [int(uniform(1,200))])
        DataBank.set_words(1, [int(uniform(1,200))])
        DataBank.set_words(2, [int(uniform(1,200))])
        #DataBank.set_bits(0,[int(uniform(0,200))])
        if state!=DataBank.get_words(1):
            print(f"State: {state}")
            state=DataBank.get_words(1)
            print(f"State: {state}")
            sleep(0.5)
            
except:
    print("Server is not running...")
    server.stop()
    print("Server is stopped...")

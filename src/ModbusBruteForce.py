from pyModbusTCP.client import ModbusClient

client=ModbusClient(host="127.0.0.1", port=12345)

b=client.open()

print(b)

global a

a=0

for x in range(256):
    if a > 0:
        v=client.read_holding_registers(a,125)
        k=client.read_input_registers(a,125)
        l=client.read_discrete_inputs(a,2000)
        print(f"Address: {a}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n")
       
        
        file=open("log.txt","a+")
        file.write(f"Address: {a}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n")
        file.close()
    else:
        v=client.read_holding_registers(a,125)
        k=client.read_input_registers(a,125)
        l=client.read_discrete_inputs(a,2000)
        print(f"Address: {a}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n")
        
        
        file=open("log.txt","w")
        file.write(f"Address: {a}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n")
        file.close()
        
        
    a+=1

    
    


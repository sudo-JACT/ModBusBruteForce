from pyModbusTCP.client import ModbusClient

client=ModbusClient(host="127.0.0.1", port=12345) #--> specify the host and port where the client connect


#open connection
b=client.open()

print(b) #--> print the connection status True if the connection is ok else return False

global a

a=0

#for loop
for x in range(256):
    if a > 0:
        v=client.read_holding_registers(a,125) #holding registers data
        k=client.read_input_registers(a,125) #input registers data
        l=client.read_discrete_inputs(a,2000) #discrete inputs data
        print(f"Address: {a}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n") #print in the console
       
        
        file=open("log.txt","a+")
        file.write(f"Address: {a}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n") #save in a file
        file.close()
    else:
        v=client.read_holding_registers(a,125)
        k=client.read_input_registers(a,125)
        l=client.read_discrete_inputs(a,2000)
        print(f"Address: {a}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n") #print in the console
        
        
        file=open("log.txt","w")
        file.write(f"Address: {a}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n") #save in a file
        file.close()
        
        
    a+=1

    
    


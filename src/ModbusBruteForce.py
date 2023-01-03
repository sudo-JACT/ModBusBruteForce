from pyModbusTCP.client import ModbusClient
from rich.console import Console
from art import *

console = Console()

asci=tprint("ModBus Brute Force",font="random")

host = console.input("[bold green]HOST:[/bold green] ")

port = console.input("[bold green]PORT:[/bold green] ")

ad = console.input("[bold green]MAX ADDRESS:[/bold green] ")
ad=int(ad)

ID = console.input("[bold green]UNIT ID:[/bold green] ")

if ID == "":
    ID=1

client=ModbusClient(host=host, port=port, auto_open=True, auto_close=True, timeout=10)


client.unit_id(ID)
b=client.open()



global addr

addr=0

for _ in range(ad):
    if addr == ad:
        v=client.read_holding_registers(addr,2)
        k=client.read_input_registers(addr,2)
        l=client.read_discrete_inputs(addr,2)
        err=client.last_error_txt()
        exx=client.last_except_txt(verbose=True)
        if b == False or v is None:
            console.print(f"Address: {addr}\nHolding Registers Data: [bold red]{v}[/bold red]\nInput Registers Data: [bold red]{k}[/bold red]\nDiscrete Inputs Data: [bold red]{l}[/bold red]\nConnection: [bold red]{b}[/bold red]\nError: [bold red]{err}[/bold red]\nExcept: [bold red]{exx}[/bold red]\n-------------------\n")

            file=open("log.txt","a+")
            file.write(f"Address: {addr}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\nError: {err}\nExcept: {exx}\n-------------------\n")
        else:
            
            console.print(f"Address: {addr}\nHolding Registers Data: [bold green]{v}[/bold green]\nInput Registers Data: [bold green]{k}[/bold green]\nDiscrete Inputs Data: [bold green]{l}[/bold green]\nConnection: [bold green]{b}[/bold green]\n-------------------\n")

            file=open("log.txt","a+")
            file.write(f"Address: {addr}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n")
        file.close()


        break

    if addr > 0:
        v=client.read_holding_registers(addr,2)
        k=client.read_input_registers(addr,2)
        l=client.read_discrete_inputs(addr,2)
        err=client.last_error_txt()
        exx=client.last_except_txt(verbose=True)

        if b == False or v is None:
            console.print(f"Address: {addr}\nHolding Registers Data: [bold red]{v}[/bold red]\nInput Registers Data: [bold red]{k}[/bold red]\nDiscrete Inputs Data: [bold red]{l}[/bold red]\nConnection: [bold red]{b}[/bold red]\nError: [bold red]{err}[/bold red]\nExcept: [bold red]{exx}[/bold red]\n-------------------\n")

            file=open("log.txt","a+")
            file.write(f"Address: {addr}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\nError: {err}\nExcept: {exx}\n-------------------\n")
        else:
            
            console.print(f"Address: {addr}\nHolding Registers Data: [bold green]{v}[/bold green]\nInput Registers Data: [bold green]{k}[/bold green]\nDiscrete Inputs Data: [bold green]{l}[/bold green]\nConnection: [bold green]{b}[/bold green]\n-------------------\n")

            file=open("log.txt","a+")
            file.write(f"Address: {addr}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n")
    else:
        v=client.read_holding_registers(addr,2)
        k=client.read_input_registers(addr,2)
        l=client.read_discrete_inputs(addr,2)
        err=client.last_error_txt()
        exx=client.last_except_txt(verbose=True)

        if b == False or v is None:
            console.print(f"Address: {addr}\nHolding Registers Data: [bold red]{v}[/bold red]\nInput Registers Data: [bold red]{k}[/bold red]\nDiscrete Inputs Data: [bold red]{l}[/bold red]\nConnection: [bold red]{b}[/bold red]\nError: [bold red]{err}[/bold red]\nExcept: [bold red]{exx}[/bold red]\n-------------------\n")

            file=open("log.txt","w")
            file.write(f"Address: {addr}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\nError: {err}\nExcept: {exx}\n-------------------\n")
        else:
            console.print(f"Address: {addr}\nHolding Registers Data: [bold green]{v}[/bold green]\nInput Registers Data: [bold green]{k}[/bold green]\nDiscrete Inputs Data: [bold green]{l}[/bold green]\nConnection: [bold green]{b}[/bold green]\n-------------------\n")

            file=open("log.txt","w")
            file.write(f"Address: {addr}\nHolding Registers Data: {v}\nInput Registers Data: {k}\nDiscrete Inputs Data: {l}\nConnection: {b}\n-------------------\n")
    file.close()


    addr+=2

    
    


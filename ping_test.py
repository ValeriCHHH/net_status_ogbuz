import os


def host_ping(host):
    response = os.system(f'ping -c 2 ' + host + '>> /dev/null')
    if response == 0:
        return f'{host} is up'
    else:
        return f'{host} is down'
    
with open('list_host.txt') as file:
    host_park = file.read()
    liner = host_park.splitlines()
    for host in liner:
        print(host_ping(host))
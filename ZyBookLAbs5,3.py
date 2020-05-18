# Type your code here
services = {'-': 0, 'Oil change':35, 'Tire rotation':19, 'Car wash':7, 'Car wax':12}
service1 = ""
service2 = ""
invoice_total = 0

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

#service1 = input('Select first service:\n')
#service2 = input('Select second service:\n')

oil_change = 35
tire_rotation = 19
car_wash = 7
car_wax = 12

service1 = input('Select first service:')
print('')
service2 = input('Select second service:')
print('')
print('')

# invoice
print('Davy\'s auto shop invoice\n')

# service1
if service1 == '-':
    print('Service 1: No service')
else:
    print('Service 1: %s, $%d' % (service1, services.get(service1)))
    # service2
if service2 == '-':
    print('Service 2: No service')
else:
    print('Service 2: %s, $%d' % (service2, services.get(service2)))

invoice_total = services.get(service1) + services.get(service2)
print()
print('Total: $%d' % invoice_total)

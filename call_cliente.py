from my_package.client import Cliente

statusFlag = 'Y'

cliente1 = Cliente('2','Luan','Oliveira','luan.oliveira@github.com','Y')
notificacion_cliente2 = cliente1.send_notificaction( cliente1.__str__())

print(notificacion_cliente2)

print("###############################################")

cliente2 = Cliente('3','Ryan','Sheckler','ryan.sheckler@github.com','N')
#update_cliente = cliente2.update_enabledFlag(statusFalse)
notificacion_cliente2 = cliente2.send_notificaction( cliente2.update_enabledFlag(statusFlag))

print(cliente2)
print(notificacion_cliente2)
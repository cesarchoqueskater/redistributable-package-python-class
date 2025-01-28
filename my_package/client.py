class Cliente:
    def __init__(self, id_client = int, name_client = str, lastname_client = str,emailaddress = str, enabledFlagClient:  chr = 'Y'):

        self.id_client = id_client
        self.name_client = name_client
        self.lastname_client = lastname_client
        self.enabledFlagClient = enabledFlagClient
        self.emailaddress = emailaddress

    def __str__(self):
        return f"Se creo el Cliente[{self.id_client}]: {self.name_client} {self.lastname_client} - {self.emailaddress}"

    def update_enabledFlag(self, flag):
        if (flag == 'Y'):
            return f"El cliente {self.lastname_client} {self.name_client} se procedio a activar."
        else:
            return f"El cliente {self.lastname_client} {self.name_client} se procedio a desactivar."

    def send_notificaction(self, mensaje):
        return f"Confirmación enviada por correo a {self.emailaddress}: {mensaje}"



def create_client():
    new_cliente_default = Cliente(1, "Cesar", "Choquehuanca", "cesar.choquehuanca@github.com", 'Y')
    return new_cliente_default
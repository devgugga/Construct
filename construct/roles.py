from rolepermissions.roles import AbstractUserRole


class Gerente(AbstractUserRole):
    available_permissions = {
        "register_products": True,
        "create_discounts": True,
        "register_seller": True,
    }


class Vendedor(AbstractUserRole):
    available_permissions = {
        "sell_products": True,
    }

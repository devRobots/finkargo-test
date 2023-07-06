"""
Servicio de Endpoint que recibe una lista de meses, ventas y gastos
y devuelve el balance
"""
def make_balance_service(months, sales, expenses):
    """
    Recibe una lista de meses, ventas y gastos de data
    y devuelve el balance
    """
    balance = []

    for index, month in enumerate(months):
        balance.append({
            'mes': month,
            'Ventas': sales[index],
            'Gastos': expenses[index],
            'Balance': sales[index] - expenses[index]
        })

    return balance

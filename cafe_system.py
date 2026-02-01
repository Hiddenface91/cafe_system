class CafeManager:
    def __init__(self):
        self.inventory: Dict[str, Product] = {
            "1": Drink("Espresso", 2.50),
            "2": Drink("Matcha Latte", 4.50),
            "3": Food("Avocado Toast", 8.90)
        }
        self.tables = {i: Table(i) for i in range(1, 6)}
        self.revenue = 0.0

    def process_payment(self, table_id: int, cash: float):
        table = self.tables.get(table_id)
        if not table or not table.is_occupied:
            raise ValueError("Tisch ungültig oder leer.")
            
        if cash < table.total_sum:
            raise ValueError(f"Fehlbetrag: {table.total_sum - cash:.2f}€")

        self.revenue += table.total_sum
        change = cash - table.total_sum
        table.reset()
        return change

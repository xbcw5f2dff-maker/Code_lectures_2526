import csv
import random


class Product:
    def __init__(self, product_name, holding_cost, stockout_penalty):
        # basisinfo
        self.product_name = product_name
        self.holding_cost = holding_cost
        self.stockout_penalty = stockout_penalty

        # elke batch is een dict: {"quantity": ..., "cost_per_unit": ...}
        # laatste batch in de lijst = bovenaan de stack (LIFO)
        self.batches = []


class InventoryManager:
    def __init__(self):
        # products: dict met key = product_name, value = Product-object
        self.products = {}

    # 1) product toevoegen
    def add_product(self, product_name, holding_cost, stockout_penalty):
        if product_name in self.products:
            print("Product " + str(product_name) + " already exists.")
            return

        new_product = Product(product_name, holding_cost, stockout_penalty)
        self.products[product_name] = new_product

    # 2) nieuwe batch toevoegen (restock)
    def restock_product(self, product_name, quantity, cost_per_unit):
        if product_name not in self.products:
            print("Product " + str(product_name) + " not found")
            return

        product = self.products[product_name]
        # batch als dict opslaan
        batch = {
            "quantity": quantity,
            "cost_per_unit": cost_per_unit
        }
        # LIFO: we gebruiken .append, en nemen later altijd de laatste batch
        product.batches.append(batch)

    # 3) vraag simuleren
    def simulate_demand(self, min_demand=0, max_demand=20):
        demand = {}
        # voor elk product een random vraag
        for product_name in self.products:
            demand[product_name] = random.randint(min_demand, max_demand)
        return demand

    # 4) 1 dag simuleren
    def simulate_day(self, demand):
        total_holding_cost = 0
        total_stockout_penalty = 0

        # loop over alle producten in de voorraad
        for product_name, product_info in self.products.items():
            # vraag voor dit product (0 als het niet in demand zit)
            vraag = demand.get(product_name, 0)

            # voorraad verbruiken: LIFO → werk met de laatste batch
            while vraag > 0 and len(product_info.batches) > 0:
                batch = product_info.batches[-1]  # neem laatste batch

                if batch["quantity"] > vraag:
                    # batch heeft genoeg voorraad
                    batch["quantity"] -= vraag
                    vraag = 0
                else:
                    # batch volledig opgebruikt
                    vraag -= batch["quantity"]
                    # hoeveelheid wordt 0 → hele batch weggooien (stack pop)
                    product_info.batches.pop()

            # alles wat we niet konden leveren → stockout penalty
            if vraag > 0:
                total_stockout_penalty += vraag * product_info.stockout_penalty

            # holding cost op alle overblijvende voorraad
            for batch in product_info.batches:
                total_holding_cost += batch["quantity"] * product_info.holding_cost

        return total_holding_cost, total_stockout_penalty

    # 5) voorraad opslaan naar CSV
    def save_to_csv(self, filename):
        # Formaat per rij: product_name, batch_quantity, batch_cost_per_unit
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for product_name, product in self.products.items():
                for batch in product.batches:
                    quantity = batch["quantity"]
                    cost_per_unit = batch["cost_per_unit"]
                    writer.writerow([product_name, quantity, cost_per_unit])

    # 6) voorraad inladen uit CSV
    def load_from_csv(self, filename):
        with open(filename, "r", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                # we verwachten EXACT 3 kolommen
                if len(row) != 3:
                    continue

                product_name = row[0]
                quantity = int(row[1])
                cost_per_unit = float(row[2])

                # als product nog niet bestaat → toevoegen met dummy costs
                if product_name not in self.products:
                    self.add_product(
                        product_name,
                        holding_cost=0.0,
                        stockout_penalty=0.0
                    )

                # batch toevoegen via restock_product
                self.restock_product(product_name, quantity, cost_per_unit)

    # 7) voorraad afdrukken
    def print_inventory(self):
        print("Current Inventory:")
        for product_name, product in self.products.items():
            print("Product " + str(product_name) + ":")

            if len(product.batches) == 0:
                print("  (no batches)")
                continue

            for batch in product.batches:
                q = batch["quantity"]
                c = batch["cost_per_unit"]
                print("  Batch(quantity=" + str(q) +
                      ", cost_per_unit=" + str(c) + ")")


# 8) main-functie (NIET in de klasse, gewoon apart)
def main():
    m = InventoryManager()

    # producten toevoegen
    m.add_product("Widget", 0.5, 2.0)
    m.add_product("Gadget", 0.8, 3.0)

    # batches toevoegen
    m.restock_product("Widget", 100, 2.5)
    m.restock_product("Widget", 50, 2.0)
    m.restock_product("Gadget", 70, 3.0)
    m.restock_product("Gadget", 30, 2.8)

    # voorraad tonen
    print("Voorraad vóór simulatie:")
    m.print_inventory()

    # vraag simuleren
    demand = m.simulate_demand(0, 20)
    print("Vraag:", demand)

    # dag simuleren
    hold, penalty = m.simulate_day(demand)
    print("Holding cost:", hold)
    print("Stockout penalty:", penalty)

    # voorraad tonen na simulatie
    print("Voorraad na simulatie:")
    m.print_inventory()

    # opslaan in CSV
    m.save_to_csv("inventory.csv")
    print("CSV opgeslagen als inventory.csv")


if __name__ == "__main__":
    main()

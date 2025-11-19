import csv
from collections.abc import generator
from itertools import product, batched
from random import random


class Product:
    def __init__(self,product_name, holding_cost, stockout_penalty):
        self.product_name = product_name
        self.holding_cost = holding_cost
        self.stockout_penalty = stockout_penalty
        self.batches = [] #elk product heeft batches waarbij de laatste batch eerst gebruikt wordt dus we moeten elk product zijn batches in een aparte stack steken


class Inventory_Manager:
    def __init__(self):
        self.products =  {}

    def add_product(self, product_name, holding_cost, stockout_penalty):
        if product_name in self.products:
            print("Product",str(product_name),"already exists.")
            return
        else:
            new_product = Product(product_name, holding_cost, stockout_penalty)
            self.products[product_name] = new_product #in de dictionary steken

    def restock_product(self, product_name, quantity, cost_per_unit):
        if not product_name in self.products:
            print("Product",str(product_name),"not found.")
            return
        else:
            product = self.products[product_name] #eerst juiste product ophalen
            product.batches.append((quantity,cost_per_unit))

    import random
    def simulate_demand(self,min_demand = 0, max_demand = 20):
        demand = {}
        for product_name in self.products:
            demand[product_name] = random.randint(min_demand,max_demand)
        return demand

    def simulate_day(self, demand):
        total_holding_cost = 0
        total_stockout_penalty = 0

        for product_name, product_info in self.products.items():
            vraag = demand.get(product_name, 0)

            # voorraad verbruiken (LIFO)
            while vraag > 0 and product_info.batches:
                batch = product_info.batches[-1]  # laatste batch

                if batch["quantity"] > vraag:
                    batch["quantity"] -= vraag
                    vraag = 0
                else:
                    vraag -= batch["quantity"]
                    product_info.batches.pop()  # hele batch op

            # niet-geleverde vraag → stockout penalty
            if vraag > 0:
                total_stockout_penalty += vraag * product_info.stockout_penalty

            # holding cost op alle resterende voorraad
            for batch in product_info.batches:
                total_holding_cost += batch["quantity"] * product_info.holding_cost

        return total_holding_cost, total_stockout_penalty

    def save_to_csv(self, filename):
        """
        Schrijf alle batches uit de voorraad naar een CSV-bestand.
        Formaat per rij: product_name, batch_quantity, batch_cost_per_unit
        """
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            # voor elk product in de voorraad
            for product_name, product in self.products.items():
                # voor elke batch van dat product
                for batch in product.batches:
                    quantity = batch["quantity"]
                    cost_per_unit = batch["cost_per_unit"]
                    # schrijf één rij naar de CSV
                    writer.writerow([product_name, quantity, cost_per_unit])



    def load_from_csv(self, filename):
       with open(filename,'r', newline='') as csvfile:
           reader = csv.reader(csvfile, delimiter=',')
           for row in reader:
               if len(row) != 3:
                   continue #foute of lege rij overslaan

               product_name = row[0]
               quantity = int(row[1])
               cost_per_unit = float(row[2])

               if product_name not in self.products:
                   self.add_product(product_name, holding_cost = 0.0, stockout_penalty = 0.0)

               product = self.products[product_name]
               product.add_batch(quantity, cost_per_unit)

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
                print("  Batch(quantity=" + str(q) + ", cost_per_unit=" + str(c) + ")")


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
            print("Voorraad:")
            m.print_inventory()

            # vraag simuleren
            demand = m.simulate_demand(0, 20)
            print("Vraag:", demand)

            # dag simuleren
            hold, penalty = m.simulate_day(demand)
            print("Holding cost:", hold)
            print("Stockout penalty:", penalty)

            # opslaan in CSV
            m.save_to_csv("inventory.csv")
            print("CSV opgeslagen.")


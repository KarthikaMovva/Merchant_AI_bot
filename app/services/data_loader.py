import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"


def read_json(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)


class DatasetLoader:

    def __init__(self):

        self.categories = {}
        self.merchants = {}
        self.customers = {}
        self.triggers = {}

        self.load()

    def load(self):

        categories = DATA_DIR / "categories"

        for file in categories.glob("*.json"):
            data = read_json(file)
            self.categories[data["slug"]] = data

        merchants = read_json(DATA_DIR / "merchants_seed.json")

        for merchant in merchants["merchants"]:
            self.merchants[merchant["merchant_id"]] = merchant

        customers = read_json(DATA_DIR / "customers_seed.json")

        for customer in customers["customers"]:
            self.customers[customer["customer_id"]] = customer

        triggers = read_json(DATA_DIR / "triggers_seed.json")

        for trigger in triggers["triggers"]:
            self.triggers[trigger["id"]] = trigger

        print(f"Loaded {len(self.categories)} categories")
        print(f"Loaded {len(self.merchants)} merchants")
        print(f"Loaded {len(self.customers)} customers")
        print(f"Loaded {len(self.triggers)} triggers")

    def get_merchant(self, merchant_id):
        return self.merchants.get(merchant_id)

    def get_customer(self, customer_id):
        if customer_id is None:
            return None
        return self.customers.get(customer_id)

    def get_category(self, slug):
        return self.categories.get(slug)

    def get_trigger(self, trigger_id):
        return self.triggers.get(trigger_id)


dataset = DatasetLoader()
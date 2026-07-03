import json
from pathlib import Path

from app.models.category import CategoryContext
from app.models.merchant import MerchantContext
from app.models.customer import CustomerContext
from app.models.trigger import TriggerContext


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATASET_DIR = BASE_DIR / "data"


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


class DatasetLoader:

    def __init__(self):

        self.categories: dict[str, CategoryContext] = {}
        self.merchants: dict[str, MerchantContext] = {}
        self.customers: dict[str, CustomerContext] = {}
        self.triggers: dict[str, TriggerContext] = {}

        self.load()

    def load_categories(self):

        category_dir = DATASET_DIR / "categories"

        for file in category_dir.glob("*.json"):

            data = load_json(file)

            category = CategoryContext.model_validate(data)

            self.categories[category.slug] = category

    def load_merchants(self):

        merchant_dir = DATASET_DIR / "merchants"

        for file in merchant_dir.glob("*.json"):

            data = load_json(file)

            merchant = MerchantContext.model_validate(data)

            self.merchants[merchant.merchant_id] = merchant

    def load_customers(self):

        customer_dir = DATASET_DIR / "customers"

        for file in customer_dir.glob("*.json"):

            data = load_json(file)

            customer = CustomerContext.model_validate(data)

            self.customers[customer.customer_id] = customer

    def load_triggers(self):

        trigger_dir = DATASET_DIR / "triggers"

        for file in trigger_dir.glob("*.json"):

            data = load_json(file)

            trigger = TriggerContext.model_validate(data)

            self.triggers[trigger.id] = trigger

    def load(self):

        self.load_categories()
        self.load_merchants()
        self.load_customers()
        self.load_triggers()

    def get_category(self, slug: str):
        return self.categories.get(slug)


    def get_merchant(self, merchant_id: str):
        return self.merchants.get(merchant_id)


    def get_trigger(self, trigger_id: str):
        return self.triggers.get(trigger_id)


    def get_customer(self, customer_id: str):
        if customer_id is None:
            return None
        return self.customers.get(customer_id)


dataset = DatasetLoader()
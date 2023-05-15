# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict


class resetDynamicFormFIeldsSlots(Action):
    def name(self):
        return "action_reset_dynamic_fields_slot"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("type", None)] 
    

account_balances = {
    "bibhuti": 6000,
    "santosh": 5000,
    "bipin": 3000,
    "pramod": 2000,
    "raja": 1000,
}

user_name = {
    "9991": "bibhuti",
    "9992": "santosh",
    "9993": "bipin",
    "9994": "pramod",
    "9995": "raja",
}

transaction_records = {
"bibhuti": [
{"date": "2023-01-01", "description": "Salary Credit", "amount": 20000},
{"date": "2023-01-10", "description": "Grocery Shopping", "amount": -1500},
{"date": "2023-01-15", "description": "Rent Payment", "amount": -6000}
],
"santosh": [
{"date": "2023-01-01", "description": "Salary Credit", "amount": 15000},
{"date": "2023-01-10", "description": "Grocery Shopping", "amount": -2000},
{"date": "2023-01-15", "description": "Rent Payment", "amount": -5000}
],
"bipin": [
{"date": "2023-01-01", "description": "Salary Credit", "amount": 10000},
{"date": "2023-01-10", "description": "Grocery Shopping", "amount": -1000},
{"date": "2023-01-15", "description": "Rent Payment", "amount": -4000}
],
"pramod": [
{"date": "2023-01-01", "description": "Salary Credit", "amount": 8000},
{"date": "2023-01-10", "description": "Grocery Shopping", "amount": -500},
{"date": "2023-01-15", "description": "Rent Payment", "amount": -3000}
],
"raja": [
{"date": "2023-01-01", "description": "Salary Credit", "amount": 5000},
{"date": "2023-01-10", "description": "Grocery Shopping", "amount": -700},
{"date": "2023-01-15", "description": "Rent Payment", "amount": -4000}
]
}

class ActionAccountNumberSubmit(Action):
    def name(self) -> Text:
        return "action_submit_account_number_for_balance"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        account=tracker.get_slot("account_number_for_balance")

        name = user_name.get(account)

        balance=account_balances.get(name)

        dispatcher.utter_message(text=f"Name: {name} balance: {balance}")


class ActionTransactionHistorySubmit(Action):
    def name(self) -> Text:
        return "action_submit_account_number_for_transaction_history"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        
        account=tracker.get_slot("account_number_for_history")
        
        name = user_name.get(account)

        transaction = transaction_records.get(name)
                
        dispatcher.utter_message(text=f"account: {account} name:{name}  transaction history:{transaction}")


#clearing slots value
class resetBecameAgentForm(Action):
    def name(self):
        return "action_reset_account_number_slot"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("account_number_for_history", None),
            SlotSet("account_number_for_balance", None),
           ]
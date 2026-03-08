from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# -------------------------------------------------
# ACTION 1: SAVE THE CATEGORY USER ASKED FOR
# -------------------------------------------------

class ActionSetCategory(Action):

    def name(self) -> Text:
        return "action_set_category"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # get the user intent
        intent = tracker.latest_message["intent"].get("name")

        # save it in slot
        return [SlotSet("quote_category", intent)]


# -------------------------------------------------
# ACTION 2: SEND QUOTE BASED ON CATEGORY
# -------------------------------------------------

class ActionSendQuote(Action):

    def name(self) -> Text:
        return "action_send_quote"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # get category stored in slot
        category = tracker.get_slot("quote_category")

        if not category:
            dispatcher.utter_message(text="Please tell me which quote you want.")
            return []

        # build response name
        response_name = f"utter_{category}"

        # get quotes from domain.yml
        quotes = domain.get("responses", {}).get(response_name, [])

        if quotes:
            quote = random.choice(quotes)["text"]
            dispatcher.utter_message(text=quote)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find a quote.")

        # ask feedback again
        dispatcher.utter_message(response="utter_feedback")

        return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionQueryJudges(Action):
    def name(self) -> str:
        return "action_query_judges"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        # Query your data source or perform any logic here
        judges_info = "There are 34 judges in the Supreme Court."
        
        dispatcher.utter_message(text=judges_info)
        return []


from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted


class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "sales_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "job_function",
            "use_case",
            "budget",
            "person_name",
            "company",
            "business_email",
            ]


    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {"use_case": self.from_text(intent="inform")}


    def submit(
            self,
            dispatcher,
            tracker,
            domain,
        ):

        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []

class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
    	return "action_greet"

    def run(self, dispatcher, tracker, domain):
    	dispatcher.utter_template("utter_greet", tracker)
    	return [UserUtteranceReverted()]


import re
import random

class AlienBot:

    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_questions = (
            "Why are you here? ",
            "Are there many humans like you? ",
            "What do you consume for sustenance? ",
            "Is there intelligent life on this planet? ",
            "Does Earth have a leader? ",
            "What planets have you visited? ",
            "What technology do you have on this planet? "
        )

    def __init__(self):
        self.alienbabble = {'describe_planet_intent': r'.*your planet.*',
                            'answer_why_intent': r'why\sare.*',
                            'cubed_intent': r''
                                }

    # ---------------------------------------------------------------------------------------------------------
    def greet(self):
        self.name = input("Hello there, what's your name?")
        will_help = input(f"Hi {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet?")
        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return
        self.chat()

    # ---------------------------------------------------------------------------------------------------------
    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print("Ok, have a nice Earth day!")
                return True

    # ---------------------------------------------------------------------------------------------------------
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    # ---------------------------------------------------------------------------------------------------------
    def match_reply(self, reply):
        for intent, regex in self.alienbabble.items():

            found_match = re.match(regex, reply)

            if found_match:
                if intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'cubed_intent':
                    return self.cubed_intent()

    # ---------------------------------------------------------------------------------------------------------
    def describe_planet_intent(self):
        responses = ('My planet is a utopia of diverse organisms and species. ', 'I am from Opidipus, the capital of the Wayward Galaxies. ')
        return random.choice(responses)

    # ---------------------------------------------------------------------------------------------------------
    def answer_why_intent(self):
        responses = ('I come in peace. ', 'I am here to collect data on your planet and its inhabitants. ', 'I heard the coffee is good. ')
        return random.choice(responses)

    # ---------------------------------------------------------------------------------------------------------
    def cubed_intent(self, number):
        return "Inside .cubed_intent()"

    # ---------------------------------------------------------------------------------------------------------
    def no_match_intent(self):
        return "Inside .no_match_intent()"

    # ---------------------------------------------------------------------------------------------------------

# Create an instance of AlienBot below:
my_bot = AlienBot()

my_bot.greet()


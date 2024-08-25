import random
from Tables.connections import connections

class Prompt:
    """
    This is a class that will handle the generation of prompts to send to Gemini.
    The prompts are dependent on player's insanity, the team's current score, and the modifiers table.
    """
    def __init__(self) -> None:
        pass
    
    def create_prompt(self) -> str:
        connections = self._get_connections()
        prompt = f"Make four short surrealist scenes. Make each scene include one of the following phrases: {connections}. \
        Make sure that there is no commonality between all four scenes EXCEPT the one common word that exists in each of the phrases."
        return prompt

    def _get_connections(self):
        connection = connections[random.randint(0, len(connections))]
        print (connection)
        return connection
        
import random
from Amalgamoria.Tables.connections import connections
from Amalgamoria.Tables.modifiers import scene_modifiers

state_team_status_stand_in = 2

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
    
    def _find(self, iterable, condition):
        for i in len(iterable):
            if condition(iterable[i]):
                return (iterable[i], i)
        return None

    def _get_connections(self):
        connection = connections[random.randint(0, len(connections))]
        return connection
    
    def _get_scene_modifiers(self):
        modifier = self._find(scene_modifiers, lambda x: x["weight"] == state_team_status_stand_in)
        print(modifier)
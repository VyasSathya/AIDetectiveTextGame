# character.py

import openai

class Character:
    def __init__(self, data):
        self.name = data['name']
        self.color = data['color']
        self.role = data['role']
        self.personality = data['personality']
        self.background = data['background']
        self.whereabouts = data['whereabouts']
        self.actions = data['actions']
        self.relationships = data['relationships']
        self.motive = data['motive']
        self.alibi = data['alibi']
        self.additional_details = data['additional_details']
        self.is_murderer = data.get('is_murderer', False)
        self.knowledge_base = self.build_knowledge_base()
        self.location = None  # Current location of the character

    def build_knowledge_base(self):
        knowledge = f"""
Name: {self.name}
Role: {self.role}
Personality: {self.personality}
Background: {self.background}
Whereabouts at Time of Crime: {self.whereabouts}
Actions and Habits: {self.actions}
Relationships: {self.relationships}
Motive: {self.motive}
Alibi: {self.alibi}
Additional Details: {self.additional_details}
"""
        return knowledge

    def respond_to_question(self, question, game_state):
        # Build context including knowledge of self and others
        other_characters_info = "\n".join([
            f"{char.name}: {char.personality}, Relationship with me: {self.relationships.get(char.name, 'No significant relationship')}"
            for char in game_state['characters'] if char.name != self.name
        ])

        # Include collected clues
        clues_info = "\n".join([
            f"Clue {idx + 1}: {clue.description}" for idx, clue in enumerate(game_state['clues_collected'])
        ])

        prompt = f"""
You are {self.name}, {self.role} at Summit Technologies.

Your Knowledge:
{self.knowledge_base}

Knowledge about other characters:
{other_characters_info}

Clues collected by the investigator:
{clues_info}

Current Scenario:
{game_state['current_scenario']}

The player asks: "{question}"

Respond in first person, reflecting your character's personality, goals, and the information you have. Be consistent with your alibi, motives, and knowledge of events. If you are the murderer, you may choose to subtly deceive the player. Provide detailed and natural responses.
"""

        # Generate response using OpenAI API
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" or "gpt-4" if available
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7,
            )
            reply = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"Error during API call: {e}")
            reply = "I'm sorry, I can't answer that right now."

        return reply
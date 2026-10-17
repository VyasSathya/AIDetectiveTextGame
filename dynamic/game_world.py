# game_world.py

from character import Character
from location import Location
from clue import Clue

class GameWorld:
    def __init__(self):
        self.characters = []
        self.locations = {}
        self.clues_collected = []
        self.current_scenario = "You are investigating the murder of Jonathan Reed at Summit Lodge."
        self.setup_complete = False

    def setup_characters(self):
        # Load character data dynamically from the story
        character_data_list = self.load_character_data()
        for data in character_data_list:
            character = Character(data)
            self.characters.append(character)
        self.setup_complete = True

    def load_character_data(self):
        # Full character data list from your story
        character_data_list = [
            {
                "name": "Dr. Evelyn Hartman",
                "color": "Blue",
                "role": "Chief Technology Officer (CTO)",
                "personality": "Brilliant, meticulous, reserved",
                "background": (
                    "Holds a Ph.D. in Computer Science with a focus on artificial intelligence. "
                    "Has been with Summit Technologies for over a decade, instrumental in developing their flagship AI products. "
                    "Recently discovered that Jonathan Reed was planning to shift the company’s focus toward more aggressive and less ethical AI applications, which she strongly opposes."
                ),
                "whereabouts": "Claims she was in her room (Guest Room A) working on her laptop, preparing for a presentation.",
                "actions": "Spends most of her time engrossed in research or reading technical journals. Takes solitary walks around the lodge to think through complex problems. Keeps a detailed planner and makes meticulous notes.",
                "relationships": {
                    "Jonathan Reed": "Professional respect but strained relationship due to ethical disagreements.",
                    "Samantha Lee": "Acts as a mentor; sees great potential in her and appreciates her ethical stance.",
                    "Lucas Mitchell": "Professional interactions; occasionally clashes over resource allocations."
                },
                "motive": "Opposes Jonathan’s plan to pivot the company’s direction unethically. Feels that her life’s work is at risk of being compromised or misused.",
                "alibi": "Laptop activity logs show usage during that time, but no one can corroborate her presence.",
                "additional_details": "Wears a simple silver necklace, a gift from her late grandmother. Allergic to almonds, which influences her dietary choices.",
                "is_murderer": False
            },
            {
                "name": "Marcus Turner",
                "color": "Green",
                "role": "Chief Financial Officer (CFO)",
                "personality": "Charismatic, ambitious, sociable",
                "background": (
                    "Joined Summit Technologies five years ago after leaving a rival firm under mysterious circumstances. "
                    "Has been secretly embezzling company funds to cover personal debts accrued from a lavish lifestyle and gambling. "
                    "Jonathan Reed recently discovered financial discrepancies and confronted Marcus privately."
                ),
                "whereabouts": "Claims he was in the lounge with Isabella Rossi until around 8:15 PM. Left the lounge briefly around 8:05 PM, stating he needed to make a phone call.",
                "actions": "Frequently checks his expensive gold watch, a symbol of his status. Spins a ring on his finger when nervous. Enjoys fine wines and is knowledgeable about them. Often steps outside to take 'private' calls.",
                "relationships": {
                    "Jonathan Reed": "Close professional relationship, but recently strained due to the embezzlement discovery.",
                    "Isabella Rossi": "Secret romantic involvement; they have been discreetly seeing each other.",
                    "Lucas Mitchell": "Clashes over budget allocations for projects."
                },
                "motive": "Jonathan’s discovery of his embezzlement threatened to ruin his career and personal life. Stands to lose everything if exposed, providing a strong motive to silence Jonathan.",
                "alibi": "His phone records show no calls made during the time he claims to have been making a call.",
                "additional_details": "His watch was found near the CEO’s office, stopped at 8:12 PM. Has a small scar on his left hand from a past accident.",
                "is_murderer": True
            },
            {
                "name": "Samantha Lee",
                "color": "Red",
                "role": "Lead Software Engineer",
                "personality": "Enthusiastic, idealistic, stubborn",
                "background": (
                    "Joined Summit Technologies straight out of graduate school and quickly rose through the ranks. "
                    "Comes from a modest background and is driven by a desire to make a positive impact. "
                    "Recently had a disagreement with Jonathan over a project involving surveillance technology, which she found ethically questionable."
                ),
                "whereabouts": "Claims she was in the gym from 7:45 PM to 8:30 PM, working out to relieve stress.",
                "actions": "Carries a notebook to jot down ideas and sketches. Fiddles with a small pendant necklace when nervous. Enjoys jogging and practices yoga to maintain balance.",
                "relationships": {
                    "Dr. Evelyn Hartman": "Looks up to her as a mentor; shares similar ethical views.",
                    "Jonathan Reed": "Respected him initially but became disillusioned after ethical disagreements.",
                    "Nina Patel": "Good friends; often confides in her about workplace concerns."
                },
                "motive": "Upset over Jonathan’s approval of unethical projects. Considered going public with information, which could have severe repercussions.",
                "alibi": "Fitness tracker shows activity during that period; no one recalls seeing her there.",
                "additional_details": "Has a pet cat named Luna, which she often mentions affectionately. Prefers herbal teas and avoids caffeine.",
                "is_murderer": False
            },
            {
                "name": "Isabella Rossi",
                "color": "Purple",
                "role": "Director of Marketing",
                "personality": "Elegant, persuasive, strategic",
                "background": (
                    "Originally from Milan, Italy, she moved to the U.S. to advance her career. "
                    "Instrumental in rebranding Summit Technologies, increasing their market share. "
                    "Facing budget cuts imposed by Jonathan, threatening her department’s performance."
                ),
                "whereabouts": "Was with Marcus Turner in the lounge until around 8:15 PM. Then went to the lobby to make phone calls; records confirm calls made starting at 8:20 PM.",
                "actions": "Always impeccably dressed, often in shades of purple. Adjusts her glasses frequently, even when unnecessary. Keeps a detailed diary, written in Italian.",
                "relationships": {
                    "Marcus Turner": "Secret romantic involvement; their relationship is discreet.",
                    "Jonathan Reed": "Professional relationship; disagreed over marketing budget cuts.",
                    "Nina Patel": "Polite but distant; minimal personal interaction."
                },
                "motive": "Budget cuts threatened her department and personal success. Felt underappreciated despite her contributions to the company’s image.",
                "alibi": "Phone records confirm calls from 8:20 PM; confirms Marcus's partial alibi but notes his unexplained absence.",
                "additional_details": "Wears a distinctive amethyst ring. Has a faint accent that becomes more pronounced when stressed.",
                "is_murderer": False
            },
            {
                "name": "Lucas Mitchell",
                "color": "Orange",
                "role": "Head of Product Development",
                "personality": "Innovative, impatient, abrasive",
                "background": (
                    "Responsible for several of the company’s most successful products. "
                    "Frustrated by what he perceives as unnecessary bureaucracy and constraints. "
                    "Had a recent project canceled by Jonathan, leading to a heated argument."
                ),
                "whereabouts": "Claims he was in the lab/workshop testing prototypes during the time of the murder.",
                "actions": "Often sketches designs on any available surface. Scratches his beard when contemplating complex problems. Drinks copious amounts of coffee.",
                "relationships": {
                    "Jonathan Reed": "Respect for his leadership but frustrated by interference in product development.",
                    "Marcus Turner": "Clashes over budget allocations; feels Marcus doesn’t prioritize innovation.",
                    "Samantha Lee": "Recognizes her talent; encourages her to think outside the box."
                },
                "motive": "Angered by the cancellation of his project, which he believed had great potential. Feels his innovations are stifled by corporate politics.",
                "alibi": "Equipment logs confirm usage of lab equipment during that time.",
                "additional_details": "Keeps a prototype gadget with him, tinkering with it constantly. Has a tattoo of a circuit diagram on his forearm.",
                "is_murderer": False
            },
            {
                "name": "Nina Patel",
                "color": "Yellow",
                "role": "Human Resources Manager",
                "personality": "Empathetic, organized, ethical",
                "background": (
                    "Holds a degree in organizational psychology. "
                    "Recently handled a sensitive harassment complaint involving Jonathan Reed. "
                    "Pressured by Jonathan to dismiss the complaint to avoid scandal."
                ),
                "whereabouts": "In her office from 7:50 PM to 8:40 PM preparing employee reports.",
                "actions": "Carries a stress ball, which she squeezes during tense situations. Keeps her office tidy and decorated with motivational quotes.",
                "relationships": {
                    "Jonathan Reed": "Professional relationship strained by ethical conflicts.",
                    "Dr. Evelyn Hartman": "Collaborates on team management and staff well-being."
                },
                "motive": "Disagreed with Jonathan’s handling of the harassment complaint. Felt morally conflicted and under pressure to compromise her principles.",
                "alibi": "Security cameras confirm she was in her office from 7:50 PM to 8:40 PM without leaving.",
                "additional_details": "Wears a bracelet with charms representing important life events. Has a calming presence that puts others at ease.",
                "is_murderer": False
            },
            {
                "name": "Daniel Kim",
                "color": "Teal",
                "role": "Head of Security",
                "personality": "Disciplined, observant, stoic",
                "background": (
                    "Former military officer with experience in intelligence and security operations. "
                    "Joined Summit Technologies four years ago to oversee corporate security. "
                    "Recently discovered potential security breaches linked to internal misconduct."
                ),
                "whereabouts": "Claims he was patrolling the grounds due to the storm and power fluctuations.",
                "actions": "Regularly checks surveillance feeds and patrols the premises. Carries a keychain with numerous keys and security fobs.",
                "relationships": {
                    "Jonathan Reed": "Professional relationship; recently reported concerns about security lapses.",
                    "Marcus Turner": "Suspicious of his activities; has been quietly investigating him.",
                    "Lucas Mitchell": "Collaborates on securing prototypes and sensitive projects."
                },
                "motive": "Discovered that Jonathan may have been involved in or complicit with security breaches. Felt his warnings were ignored, compromising the company’s safety.",
                "alibi": "Patrol logs show rounds conducted, but there is a 15-minute gap between 8:05 PM and 8:20 PM.",
                "additional_details": "Wears a simple wristwatch synchronized to the second. Has a small notebook where he records observations.",
                "is_murderer": False
            }
        ]
        return character_data_list

    def setup_locations(self):
        # Create locations based on the building layout
        rooms = [
            "Lobby", "Dining Hall", "Lounge", "Conference Room", "CEO's Office",
            "Guest Rooms Hallway", "Gym", "Lab/Workshop", "Security Office", "Outdoor Grounds",
            "Guest Room A", "Guest Room B", "Guest Room C", "Guest Room D",
            "Guest Room E", "Guest Room F", "Guest Room G"
        ]
        # Create location instances
        for room in rooms:
            self.locations[room] = Location(room)

        # Connect locations according to the adjacency list
        self.connect_locations()

        # Place characters in their respective rooms
        for character in self.characters:
            room_name = self.get_guest_room_by_character(character.name)
            if room_name:
                if room_name in self.locations:
                    self.locations[room_name].add_character(character)
                else:
                    print(f"Error: Room '{room_name}' does not exist in locations.")
            else:
                # Default to the lobby if no specific room
                self.locations["Lobby"].add_character(character)

    def connect_locations(self):
        # Define the connections based on the adjacency list
        connections = {
            "Lobby": ["Dining Hall", "Lounge", "Conference Room", "Guest Rooms Hallway", "Security Office"],
            "Dining Hall": ["Lobby", "Lounge", "Outdoor Grounds"],
            "Lounge": ["Lobby", "Dining Hall", "Conference Room", "Outdoor Grounds"],
            "Conference Room": ["Lobby", "Lounge", "CEO's Office", "Lab/Workshop"],
            "CEO's Office": ["Conference Room"],
            "Guest Rooms Hallway": ["Lobby", "Gym", "Guest Room A", "Guest Room B", "Guest Room C", "Guest Room D", "Guest Room E", "Guest Room F", "Guest Room G"],
            "Gym": ["Guest Rooms Hallway"],
            "Lab/Workshop": ["Conference Room"],
            "Security Office": ["Lobby"],
            "Outdoor Grounds": ["Dining Hall", "Lounge"]
        }
        for location_name, connected_names in connections.items():
            location = self.locations[location_name]
            for connected_name in connected_names:
                connected_location = self.locations[connected_name]
                location.connect_location(connected_location)

    def get_guest_room_by_character(self, character_name):
        room_assignments = {
            "Dr. Evelyn Hartman": "Guest Room A",
            "Marcus Turner": "Guest Room B",
            "Samantha Lee": "Guest Room C",
            "Isabella Rossi": "Guest Room D",
            "Lucas Mitchell": "Guest Room E",
            "Nina Patel": "Guest Room F",
            "Daniel Kim": "Guest Room G"
        }
        return room_assignments.get(character_name, None)

    def setup_clues(self):
        # Define clues and add them to their respective locations

        # Clue 1: Marcus's Watch
        clue_watch = Clue(
            description="An expensive watch stopped at 8:12 PM, found near the CEO's office.",
            related_to="Marcus Turner",
            evidence="The watch is cracked, suggesting it was dropped or impacted."
        )
        self.locations["Conference Room"].add_clue(clue_watch)

        # Clue 2: Access Logs
        clue_access_logs = Clue(
            description="Access logs show the CEO's office was opened at 8:10 PM using Jonathan Reed's keycard.",
            related_to="Unknown",
            evidence="Jonathan's keycard was found in his office, suggesting someone else used it."
        )
        self.locations["CEO's Office"].add_clue(clue_access_logs)

        # Clue 3: Keycard Duplicator Missing
        clue_keycard_duplicator = Clue(
            description="A keycard duplication device is missing from the Security Office.",
            related_to="Unknown",
            evidence="Daniel Kim reports that the device was locked away and is now missing."
        )
        self.locations["Security Office"].add_clue(clue_keycard_duplicator)

        # Clue 4: Isabella's Statement
        clue_isabella_statement = Clue(
            description="Isabella mentions that Marcus left the lounge around 8:05 PM to make a call.",
            related_to="Marcus Turner",
            evidence="Phone records show Marcus made no calls during that time."
        )
        self.locations["Lounge"].add_clue(clue_isabella_statement)

        # Clue 5: Lucas's Statement
        clue_lucas_statement = Clue(
            description="Lucas reports seeing someone resembling Marcus near the conference room around 8:15 PM.",
            related_to="Marcus Turner",
            evidence="Lucas was working in the lab adjacent to the conference room."
        )
        self.locations["Lab/Workshop"].add_clue(clue_lucas_statement)

        # Clue 6: Security Camera Footage
        clue_security_footage = Clue(
            description="Grainy security footage shows a figure resembling Marcus heading toward the CEO's office.",
            related_to="Marcus Turner",
            evidence="The footage is distorted due to the storm but shows the time as 8:10 PM."
        )
        self.locations["Security Office"].add_clue(clue_security_footage)

        # Clue 7: Financial Documents
        clue_financial_docs = Clue(
            description="Financial documents in Marcus's room suggest attempts to cover up embezzlement.",
            related_to="Marcus Turner",
            evidence="Documents indicate discrepancies and unauthorized transfers."
        )
        self.locations["Guest Room B"].add_clue(clue_financial_docs)

        # Clue 8: Email Draft on CEO's Computer
        clue_email_draft = Clue(
            description="An email draft on Jonathan's computer indicates he was preparing to report financial discrepancies.",
            related_to="Marcus Turner",
            evidence="The email is addressed to the board, mentioning 'serious financial misconduct.'"
        )
        self.locations["CEO's Office"].add_clue(clue_email_draft)

        # Clue 9: Daniel's Patrol Logs
        clue_daniel_logs = Clue(
            description="Daniel has a 15-minute gap in his patrol logs but provides a plausible explanation.",
            related_to="Daniel Kim",
            evidence="Security system logs confirm a minor alert during that time due to the storm."
        )
        self.locations["Security Office"].add_clue(clue_daniel_logs)

        # Clue 10: Samantha's Fitness Tracker
        clue_samantha_tracker = Clue(
            description="Samantha's fitness tracker shows activity consistent with a workout during the time of the murder.",
            related_to="Samantha Lee",
            evidence="No witnesses due to the gym's location and the storm."
        )
        self.locations["Gym"].add_clue(clue_samantha_tracker)

        # Clue 11: Evelyn's Statement
        clue_evelyn_statement = Clue(
            description="Evelyn heard footsteps outside her room at 8:10 PM.",
            related_to="Unknown",
            evidence="Could indicate someone moving toward the CEO's office."
        )
        self.locations["Guest Room A"].add_clue(clue_evelyn_statement)

        # Clue 12: Nina's Alibi
        clue_nina_alibi = Clue(
            description="Security cameras confirm Nina was in her office from 7:50 PM to 8:40 PM without leaving.",
            related_to="Nina Patel",
            evidence="Time-stamped footage shows her working at her desk."
        )
        self.locations["Security Office"].add_clue(clue_nina_alibi)

    def investigate_location(self):
        # Allow the player to choose a location to investigate
        print("\nAvailable locations to investigate:")
        for idx, location_name in enumerate(self.locations.keys()):
            print(f"{idx + 1}. {location_name}")
        choice = input("Enter the number of the location you want to investigate: ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(self.locations):
                location_name = list(self.locations.keys())[choice]
                location = self.locations[location_name]
                self.explore_location(location)
            else:
                print("Invalid choice.")
        else:
            print("Invalid input.")

    def explore_location(self, location):
        print(f"\nInvestigating {location.name}...")
        # Display clues in the location
        if location.clues:
            for clue in location.clues:
                if clue not in self.clues_collected:
                    print(f"\nClue found: {clue.description}")
                    print(f"Evidence: {clue.evidence}")
                    self.clues_collected.append(clue)
                else:
                    print(f"\nAlready found clue: {clue.description}")
        else:
            print("No clues found here.")
        # Display characters present
        if location.characters_present:
            print("\nYou see the following people here:")
            for char in location.characters_present:
                print(f"- {char.name} ({char.role})")
        else:
            print("No one is here.")

    def talk_to_character(self):
        # Allow the player to choose a character to talk to
        print("\nAvailable characters to talk to:")
        for idx, character in enumerate(self.characters):
            print(f"{idx + 1}. {character.name} ({character.color})")
        choice = input("Enter the number of the character you want to talk to: ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(self.characters):
                character = self.characters[choice]
                self.initiate_dialogue(character)
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number corresponding to the character.")

    def initiate_dialogue(self, character):
        print(f"\nYou are now talking to {character.name}.")
        while True:
            question = input("Ask your question (or type 'exit' to stop talking): ")
            if question.lower() == 'exit':
                break
            else:
                response = character.respond_to_question(question, self.get_game_state())
                print(f"\n{character.name}: {response}")

    def get_game_state(self):
        game_state = {
            'characters': self.characters,
            'current_scenario': self.current_scenario,
            'clues_collected': self.clues_collected
        }
        return game_state

    def review_clues(self):
        print("\nClues Collected:")
        if self.clues_collected:
            for idx, clue in enumerate(self.clues_collected):
                print(f"\nClue {idx + 1}:")
                print(clue)
        else:
            print("You have not collected any clues yet.")

    def accuse_suspect(self):
        print("\nWho do you want to accuse?")
        for idx, character in enumerate(self.characters):
            print(f"{idx + 1}. {character.name} ({character.color})")
        choice = input("Enter the number of the character you want to accuse: ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(self.characters):
                character = self.characters[choice]
                self.check_accusation(character)
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number corresponding to the character.")

    def check_accusation(self, character):
        if character.is_murderer:
            print(f"\nYou have accused {character.name}.")
            print("Congratulations! You have solved the mystery!")
            print(f"{character.name} is the murderer.")
            print("Thank you for playing. Goodbye!")
            exit(0)  # Exit the game intentionally after solving the mystery
        else:
            print(f"\nYou have accused {character.name}.")
            print("Unfortunately, this is not the murderer. Keep investigating!")
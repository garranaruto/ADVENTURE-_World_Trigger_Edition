from random import choice, shuffle
import shlex
caves = []

class room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.here = []
        self.tunnels= []
        caves.append(self)
    
    def tunnel_to(self, room):
        """create a two-way tunnel"""
        self.tunnels.append(room)
        room.tunnels.append(self)
    
    def __repr__(self):
        return "<room "+ self.name + ">"
    
def create_caves():
    placeholder = None

class Player(object):
    def __init__(self, location):
        self.location = location
        self.location.here.append(self)
        self.playing = True
        
    def get_input(self):
        return raw_input(">")
        
    def process_input(self, input):
        parts = shlex.split(input)
        if len(parts) == 0:
            return []
        if len(parts) == 1:
            parts.append("")
        verb = parts[0]
        noun = " ".join(parts[1:])
        handler = self.find_handler(verb, noun)
        if handler is None:
            return [input + "? I don't know how to do that!"]
        return handler(self, noun)
        
    def find_handler(self, verb, noun):
        if noun != "":
            object = [x for x in self.location.here if y is not self and x.name == noun and verb in x.actions]
            if len(object) > 0:
                return getattr(object[0], verb)
        if verb.lower() in self.actions:
            return getattr(self, verb)
        elif verb.lower() in self.location.actions:
            return getattr(self.location, verb)
            
    def look(self, player, noun):
        return [self.location.name,
        self.location.description]
    
    def logout(self, player, noun):
        self.playing = False
        return ["Your body disappears in a flash of light...when you return, things are not as they once were."]
    
    actions = ['look', 'logout']
class item(object):
    pass
def test():
    newb1 = room("Welcome to ADVENTURE: World Trigger Edition", "Welcome to ADVENTURE: World Trigger Edition!  In this game, you will become a border agent, using triggers and fighting neighbors.  Type 'north' or 'n' to enter the newbie academy.")
    player = Player(newb1)
    
    print player.location.name
    print player.location.description
    while player.playing:
        input = player.get_input()
        result = player.process_input(input)
        print "\n".join(result)
test()

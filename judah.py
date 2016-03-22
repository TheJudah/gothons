from sys import exit
from random import randint
import time

""" this is my final, based off of Learn Pythyon the Hard Way, and edited to reflect what code I can handle. """

class Scene(object):

    def enter(self):
        print ("This is the beginning of the exercise.")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        ("What's the difference between a child's painting and a painting like a child? Goodbye."),
        ("You are the weakest link. Goodbye."),
        ("You disapoint Tarah. Goodbye."),
        ("You're less useful than a coding monkey. Goodbye")
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)    

class Introduction(Scene):

    def enter(self):
        print " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ "
        print "You are part of an elite team of students-- a member of Team: Blue Cheetahs."
        raw_input("Press Enter to continue...")
        print "\n"
        print "As a group, you travel to the planet Pythonica to learn the ways of the Pythonistas."
        raw_input("Press Enter to continue...")
        print "\n"
        print "In a dramatic twist, you are separated from members of your team."
        raw_input("Press Enter to continue...")
        print "\n"
        print "Confused and alone, radio contact is limited, your battery is low, and time is running out."
        raw_input("Press Enter to continue...")
        print "\n"
        print "To learn Python and survive, you must follow the path of the ancients:"
        time.sleep(3)
        print "Observation, testing, reproduction, reasoning, and logic."
        time.sleep(3)
        print "\n"
        print "If you follow the path, the Pythonistas will reward you with knowledge."
        print "\n"

class Agreement(Scene):
    def enter(self):
        print "Python lessons begining."
        time.sleep(3)
        print "Press Enter to continue" 
        
class BvsS(Scene): 

    def enter(self):

        print "There are thousands of superheros and stories of superheros"
        print "have spawned some pretty dreadful movies."
        print "However, they are still fun."
        print "\n"
        print "In the upcoming movie, Batman vs. Superman, who"
        print "has the superpowers that would prevail in a fight between the two of them?"
        print "\n"
        print "\n"
        print "ACTION:"
        print "Type Superman or Batman.)"

        action = raw_input("> ")

        if action == "Batman":
            print " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ "
            print "You are patently wrong."
            print "While a philosophically engaging argument, the question is moot and"
            print "on its face, a flawed."
            print " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ "
            return 'death'
            
        elif action == "Superman":
            print "Superman always wins. He's such a goodie-two-shoes."
            print "Hot. But boring. Too nice."
            print " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ "
            return 'death'

        elif action == "Wonder Woman":
            print "You surprise me and I look up to you."
            print "Wonder Woman is the superior warrior--"
            print "--while embodying empathy. "
            print "She is fast, fearless, strong and feels deeply for all creatures."
            return 'superhero'

        else:
            print "You should see the movie. Tickets are available at fandango.com."
            return 'lobby'

class CivilWar(Scene):

    def enter(self):
        print "The upcoming movie Captain America: Civil War brings a widely-known"
        print "and widely-enjoyed story arc to the big screen and the reportedly brings"
        print "more than 80 heros to the screen."
        print "\n"
        print "Whose side to you join?"
        print "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ "
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "Wrong! Try again!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            print "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ "
            return 'death'

class JLA(Scene):

    def enter(self):
        print "The movie Batman vs Superman will reportely bring"
        print "all seven members of the Justice League togehter for the first"
        print "time on film."
        print "\n"
        print "We already know that three of the seven members will be in the film--"
        print "Bats, Supers, and WW... but, which do you guess will be another?"
        print "Guess 1 through 5--"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You are delighed that into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won!"

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'

class Map(object):

    scenes = {
        'introduction': Introduction(),
        'agreement': Agreement(),
        'bvss': BvsS(),
        'civilwar': CivilWar(),
        'jla': JLA(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('lobby')
a_game = Engine(a_map)
a_game.play()
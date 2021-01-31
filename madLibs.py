def dayAtTheZoo():
    adjective1 = input("Enter an adjective: ")
    noun2 = input("Enter a noun: ")
    verb3 = input("Enter a verb,past tense: ")
    adverb4 = input("Enter an adverb: ")
    adjective5 = input("Enter an adjective: ")
    noun6 = input("Enter a noun: ")
    noun7 = input("Enter a noun: ")
    adjective8 = input("Enter an adjective: ")
    verb9 = input("Enter a verb: ")
    adverb10 = input("Enter an adverb: ")
    verb11 = input("Enter a verb,past tense: ")
    adjective12 = input("Enter an adjective: ")

    print("Today I went to the zoo. I saw a " + adjective1 + " " + noun2 +
          " jumping up and down in its tree.\nHe " + verb3 + " " + adverb4 +
          " through the large tunnel that led to its "
          + adjective5 + " " + noun6 +
          ". \nI got some peanuts and passed them through the cage to a gigantic gray " + noun7 +
          " towering above my head. \nFeeding that animal made me hungry. I went to get a " + adjective8 +
          " scoop of ice cream. It filled my stomach. \nAfterwards I had to" + verb9 + " " + adverb10 + "to catch our "
          "bus.\n When I got home I " + verb11 + " my mom for a " + adjective12 + " day at the zoo.")


def funPark():
    adjective1 = input("Enter an adjective: ")
    noun2 = input("Enter a plural noun: ")
    noun3 = input("Enter a noun: ")
    adverb4 = input("Enter an adverb: ")
    number5 = input("Enter a number: ")
    verb6 = input("Enter a verb,past tense: ")
    adjective7 = input("Enter -est adjective: ")
    verb8 = input("Enter a verb,past tense: ")
    adverb9 = input("Enter an adverb: ")
    adjective10 = input("Enter an adjective: ")

    print("Today, my fabulous camp group went to a " + adjective1 + " amusement park. "
          "It was a fun park with lots of cool " + noun2 + " and enjoyable play structures. \nWhen we got there, my "
          "kind counselor shouted loudly, \"Everybody off the " + noun3 + ".\" "
          "\nWe all pushed out in a terrible hurry. My counselor handed out yellow tickets, and"
          " we scurried in. I was so excited! \nI couldn't figure out what exciting thing to do first. "
          "\nI saw a scary roller coaster I really liked so, I " + adverb4 +
          " ran over to get in the long line that had about " + number5 + " people in it. \nWhen I finally "
          "got on the roller coaster I was " + verb6 + ". \nIn fact I was so nervous my two knees"
          " were knocking together. \nThis was the " + adjective7 + " ride I had ever been on! In about two "
          "minutes I heard the crank and grinding of the gears. \nThat’s when the ride began! When I got to the bottom,"
          "I was a little " + verb8 + " but I was proud of myself. \nThe rest of the day went "
          + adverb9 + ". It was a " + adjective10 + " day at the fun park. ")


def atTheArcade():
    noun1 = input("Enter a plural noun: ")
    noun2 = input("Enter a plural noun: ")
    verb3 = input("Enter a verb: ")
    noun4 = input("Enter a noun: ")
    verb5 = input("Enter -ing verb: ")
    noun6 = input("Enter a plural noun: ")
    noun7 = input("Enter a  noun: ")
    noun8 = input("Enter a plural noun: ")
    print("When I go to the arcade with my " + noun1 + " there are lots of games to play. I spend "
          "lots of time there with my friends.\nIn the game X-Men you can be different " + noun2 +
          ". The point of the game is to " + verb3 + " every robot. You also need to save people. Then you can "
          "go to the next level. \nIn the game Star Wars you are Luke Skywalker and you try to destroy every "
          + noun4 + ". \nIn a car racing/motorcycle racing game you need to "
          "beat every computerized vehicle that you are "
          + verb5 + " against. There are a whole lot of other cool games. \nWhen you play some games you win "
          + noun6 + " for certain scores. Once you're done you can cash in your tickets to get a big "
          + noun7 + ". \nYou can save your " + noun8 + " for another time. When I went to this arcade I didn't "
          "believe how much fun it would be. "
          "\nSo far I have had a lot of fun every time I've been to this great arcade!")


answer = 'y'
while answer == 'y':
    print("1. A day at the zoo.\n2. The Fun Park.\n3. At the arcade.\n")

    try:
        x = int(input("Choose from the options above: "))
    except:
        x = -1

    if x > 3 or x <= 0:
        print("Only the numbers mentioned above are allowed.")
    if x == 1:
        dayAtTheZoo()
    elif x == 2:
        funPark()
    elif x == 3:
        atTheArcade()

    answer = input("Do you want to play again? \nPress y to continue, and any other key to exit.")

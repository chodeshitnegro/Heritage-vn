#talk space (this will be deleted after we are finished with this part)
#https://www.renpy.org/doc/html/ <=== VERY IMPORTANT
#
#

   #characters
   define n = Character("Pro Tagonist")

   #backgrounds

   image computer = "1_3.jpg"
   image wm = "welcome_message.png"

   label start:

   scene computer
   with Dissolve(3.0)
   n "Oh Yeah! It sure is nice to be on my summer break."
   n "The birds are singing, the grass is green,the sun is shining!"
   n "I have a different feeling about this summer, This one’s gonna be faaaaan-tastic~ there’s all sorts of things to do!"
   jump yeah

   label yeah:
    pause 3.0
    #{Lightning SFX, Background changes, it starts to rain}
    n "I. . . I don't have anything to do!"
    n "I mean, i can always watch Youtube, right? That’ll keep me busy, right!?"
    #{Background change to the MC looking at his PC}
    n "Sooooo, Ex Falchion just uploaded a video, what's this all about"
    #{Muffled Hol Glass Noises}
    n "This looks interesting, the video even has a link to a dedicated server for the game on a popular text and voice communication program. Well, since i got nothing better to do. . ."

    scene wm
    with Dissolve(3.0)

   define pov = Character("[povname]")

   python:
    povname = renpy.input("So stinko whats your name?")
    povname = povname.strip()

    if not povname:
         povname = "Pat Smith"

   pov "god is dissapointed in [povname]!"

   n "Wooow, there's so many channels to choose from! I wonder where can i get the game, maybe people at #General could help me with this! Wait, that would be stupid, i can't just appear out of nowhere and start asking for things! Silly me! I should take a look at some of the other channels before that, or should I?"
   "choice time!"

   menu:

       "Go to #general":
         jump general

       "Visit other channels":
         jump other


   label other:

   menu:

        "hftf general":
         jump hftf

        "guides-and-training":
         jump guide


        "palmodding":
         jump pal

        "emote suggestions":
         jump emote

        "jojo-meme-hell":
         jump memehell

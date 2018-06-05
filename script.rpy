#talk space (this will be deleted after we are finished with this part)
#https://www.renpy.org/doc/html/ <=== VERY IMPORTANT
#are u on drugs or something https://docs.google.com/document/d/1jWP-rRnmaQndJ-cPbdwqCTAaezfcOksFd32lDTRWhVg/view
# wtf did you just do
#gunna test something c
#

   #characters

   define n = Character("[povname]")
   define r = DynamicCharacter("narrator")
   define s = Character("Soui")
   define b = Character("BiLL")
   define a = Character("Aleph Null")
   define tx = Character("Tex Western")
   define rs = Character("Random Stinko")
   define Sp = Character("SploogieMcNoodle")

   #backgrounds

   image computer = "1_3.jpg"
   image wm = "welcome_message.png"
   image wr = "window_rainy.png"
   image sad = "sad.png"

   label start:
    $ narrator = "Pro Tagonist"

   scene computer
   with Dissolve(3.0)
   r "Oh Yeah! It sure is nice to be on my summer break."
   r "The birds are singing, the grass is green,the sun is shining!"
   r "I have a different feeling about this summer, This one’s gonna be faaaaan-tastic~ there’s all sorts of things to do!"
   jump yeah

   label yeah:
    pause 3.0
    scene wr
    with fade
    play sound "lightning-strike.ogg"
    r "I. . . I don't have anything to do!"
    r "I mean, i can always watch Youtube, right? That’ll keep me busy, right!?"
    scene sad
    with Dissolve(1.0)
    r "Sooooo, Ex Falchion just uploaded a video, what's this all about"
    play sound "Hol.ogg" fadeout 1.0
    r "This looks interesting, the video even has a link to a dedicated server for the game on a popular text and voice communication program. Well, since i got nothing better to do. . ."

    scene wm
    with Dissolve(3.0)

   $ narrator = "Narrator"

   define pov = Character("[povname]")

   python:
    povname = renpy.input("So stinko whats your name?")
    povname = povname.strip()

    if not povname:
         povname = "Pro Tagonist"

   r "god is dissapointed in [povname]!"

   n "Wooow, there's so many channels to choose from! I wonder where can i get the game, maybe people at #General could help me with this! Wait, that would be stupid, i can't just appear out of nowhere and start asking for things! Silly me! I should take a look at some of the other channels before that, or should I?"
   "choice time!"

   label choices:

   menu:

       "Go to #general":
         jump general

       "Visit other channels":
         jump other

   label other:

         r "hftf general!"
         r "TBA"

         r "guides and training!"

         r "Tandems? IPS? Loops? Infinites!?What are all those complex words? Is everyone in this channel crazy? Why can't you understand any of this? Shouldn't this be a easy game?"
         r "Right as you were about to give up on any of this, a new message appears, grabbing your attention."
         Sp "Yeah, if you don’t learn the numpad notation system, you’re screwed. It’s not that hard anyways, just check the pins."
         r "Answering a question made by someone else, this woman appears to be very kind and calm, but most importantly, what the hell is a numpad notation? It doesn’t really matter, so you decide to introduce yourself."
         n "Hey! That’s super cool! Could you teach me what those other complex words mean?"
         Sp "Sure, but some other time i gotta bounce to work soon. By the way, I’m SploogieMcNoodle, always here to help if you just ask! See you later alligator!"
         n "Well I should probably check the other channels out."

         r "palmodding?..."

         r "It appears that this channel has a lot of people sharing images of characters from the game with a variety of different colors. You really can't figure out what's it all about, but right as you were about to leave"
         r "you see someone typing."
         a "Haha, holy shit, another anime palmod? Why do I even bother anymore?"
         r "Weird, why is this person so grumpy? Hey! It’s your time to save the day! You can do this, time to cheer this girl up!"
         n "Hey, don’t get discouraged, I’m sure that whatever a palmod is can’t be too bad"
         a "Fuck off please, why do I have to deal with brainlets like you that can’t even read the pins?"
         r "You aren’t sure what a brainlet means or what a pin is, but you keep listening to whatever this girl has to say."
         a "I’m Aleph null, and I run this channel, if you’ve got a problem with that, you can fuck right off."
         r "After Aleph screams at some other people for not creating attractive “palmods”, or whatever they were, you decide to check out some other channels."

         r "emote suggestions!"

         r "Entering this channel, you are greeted with diverse tiny images of dumb faces the characters in the game make. It's not hard to guess that this place is used for suggesting new emotes for"
         r "the server to use. In the middle of thousands of low quality images, it would seem like an old lady is screaming at another user."
         r "Your ears begin to ring as a, well, lets just say “older” woman chews out a user who seems to have violated some sort of rule. As you move in closer, you can see that this woman seems to be in charge of this channel, ruling with an iron fist."
         b "And don’t you ever fucking post that meme here ever again, trash like this belongs into #jojo-meme-hell, you absolute monkey."
         r "She’s clearly in a bad mood, maybe you try to cheer her up, hopefully it will be more successful than the last time."
         n "Hi, I’m Pro Tagonist, are you okay? You seem to be having a rough day, miss."
         b "Do you know what this channel is for? Were you raised by actual monkeys? Choke on glass for me bud."
         r "She proceeds to send a string of multiple potentially racist emoji, namely monkeys."
         b "Whatever, I’m BiLL, and I run this channel. Read the rules if you want to suggest any new emotes."
         n "Thanks ma’am I’ll keep that in-"
         b "Don’t you ma’am me you rascal, I still have my good looks. Run along before I mute you forever kid."
         r "You decide that it may be a good idea to leave."

         r "jojo meme hell!"

         r "Finally! A channel that piques your interest! There are only a few things better than memes in the world, that being JoJo Memes!"
         r "However, you’ve never even heard of Jojo before, so you can't understand any of the jokes there. After looking through a lot of images of a man looking confused at a table, you spot what it seems to be a fight."
         tx "For the last time, you libshits have got to grow a brain and realize that this is not a shitposting server. What’s your fightcade account?"
         #Insert hand crack here
         rs "My fighcade account? Its uhhhhhhh well you see i kinda sorta dont play much of this ga......."
         #show black screen here
         #insert death sounds and what ever music probably hnk music
         #wait for like 4 seconds till player gets to choose again
         r "And so another stinko bites the dust."
         n "Wow, what was brutal, sooo cool!"
         tx "Huh? Oh, I’m sorry you had to see that, these stinkos are seriously getting on my nerves. My name’s Tex, Tex Western, what can I do ya for?"
         n "Oh, nothing, nothing! I was just taking a look at this channel and I swear I wasn’t here to post more dumb images!"
         tx "Good, then get outta here."
         jump general

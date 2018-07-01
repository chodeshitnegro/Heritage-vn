label chapter1:

         scene image "week1"
         with Pause(3.0)

         play sound "alarm_clock.ogg"
         scene image "protagroom"
         with Pause(5.0)         
         stop sound
         r "Upon hearing your alarm go off, you decide to wake up. Like every morning, you hit the bathroom, brush your teeth, eat your breakfast so you can go back to your room and do nothing for the rest of the day."
         r "You've even forgotten what day of the week it is, time doesn't really matter when you are on your break. After you are done with your morning routine, you decide to turn on your computer."
         scene image "twitter"
         with dissolve
         r "Some time passes by while you are checking some social media and it doesn't take long before you find yourself bored. After a few minutes staring into your desktop, you remember about that game you saw a few days ago. That being said, you quickly hop back into Discord."
         scene image "general"
         with dissolve
         r "You enter the game’s server and take a look at some pings you’ve received. Nothing really that important. Right as you were about to enter #General and start typing something, you remember your last time being here, and so, a thought crosses your mind:"
         n "{color=#b13ce5}Wait a second. I’ve already caused enough trouble here, i can’t risk doing something stupid again. Gaah, this sucks! I’ll just read the rules and other stuff, that should get me started on the game.{/color}"
         scene image "fightcade"
         with fade
         r "After some time, you finally got “Fightcade” working and a totally legal copy of the game. Feeling proud of yourself for doing all of this alone, you decide to play a bit offline and do story mode. Since this is your first time, you select a random character."
         scene image "fightcade2.png"
         with Dissolve(5.0)
         n "Well, that was fun! Even though i kept hitting the wrong keys on my keyboard and that i couldn’t win against the first opponent, i still enjoyed the game! I can’t wait to get online and beat everyone that made fun of me! Ha Ha Ha! Let’s see what’s going on at the #General"
         jump week1general

         label week1general:
         scene image "general2"
         with fade
         r "The channel seems to be in conflict over something of questionable and degenerate…"
         p2 "And thats why Futa on Girl is the least possible gay you can have."
         ll "So futa isn't gay but traps are? :pepehands:"
         n "Hey! Remember me, guys? I’m back, and this time stronger than ever! Who wants to fight me?"
         boi "If you want to fight ask that on #hftf-general :monkey:"
         n "Oh."
         play sound "anger.ogg"
         scene image "hftfgeneral"
         with fade
         stop sound
         n "Waaaaaaaaait, should i ping that boring role to ask for games? The matchmaking one? Hmm."
         n " Alright you PEASANTS, who’s ready for a beating? @hftf-matchmaking"
         So "Who the fuck is this kid."
         n "I'm no kid! I'm the greatest player of our generation! Now fight me!"
         So  "Hmph. Fine, get on fightcade, you're dead."
         n "Finally, my first challenge ever! This is my chance to show everyone i'm no stinko!"

         scene image "fightcade"
         with fade

         r " And so, as soon as you log into fightcade, a loud, annoying tune starts to play, catching you off-guard."
         r "It seems like you've received an challenge. Wasting no more time, you click to accept the match."
         play music "Elevator Music.ogg"
         scene image "titecard"
         with Pause(10.0)
         stop music
         scene image "black"
         with fade
         centered "This was a mistake."
         centered "It doesn't take more than a single match to realize you've made a terrible decision on fighting this player."
         centered "It doesn't matter who you pick or what you do"
         centered "You can't even get near this man without getting stuck in a 10 minutes long combo."
         centered "Why? How is this even possible? Why would someone dedicate a majority of their free-time on a silly game?"
         centered "How can you even achieve such skill?"
         r "After a set of 10 matches, you see it on the bottom of your screen"
         #insert png of soui saying gg in fightcade chat here
         r "Those two letters burn deep in your soul and you rethink life."
         n "Damn, i didn't expect to lose so badly. I mean, i'm pretty new to this, but hell, i got perfected 2 times and i don't even know what that means"
         r " As you hop back into Discord, you see another notification pop-up on you screen, how convenient."
         play sound "discordsound.ogg"
         n "Hey, an announcement? Sweet, i wonder what it could be all about."
         scene image "announce"
         with dissolve
         n " A. . . tournament? Huh, I mean, this server was created just for these, so i guess this isn't that special?"
         n "It'll also be streamed? Oh, that's cool, must be a bit scary for the competitors. I'll start this saturday,which is in five days from now"
         n "Man, should i join this? I mean, it could be kinda fun, but it's also highly competitive and i would probably get my ass kicked"
         n "What should I do?"

menu:

       "Join":
         jump join

       "Forget about it":
         jump forget


         label join:
                   n "Eh, why the hell not? There's no way i can win anyways, so i'll just do this for fun. "
                   n "I've got some days to train, but i'm not sure if that's really what i'm going to do."
                   return


         label forget:
                   n "Uh, anyways, this is not for me. If i can't win against a random player, then i can't win a tourney."
                   n "I think i will at least watch a bit of it, maybe i'll learn a thing or two."
                   return

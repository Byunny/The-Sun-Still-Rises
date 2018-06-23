# The script of the game goes in this file.

# Look up REVISION to find revision points.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Backgrounds
image rooftop = "/bg/rooftop.png"     # Chapter One
image street = "/bg/street1.png"      # Chapter Two, Scene 1
image docks = "/bg/docks1.png"        # Chapter Two, Scene 2

# Player Character
define pc = Character("[pcname] [pcsurname]")
$ pcname = "Adas"
$ pcsurname = "Emberforge"

# Daya Elenvir
define d = Character("Daya Elenvir")
image d young neutral = LiveComposite(
    (550,720),
    (0,0), "/daya/young/bodies/body.png",
    (0,0), "d young neutral blink")
image d young neutral blink:
    "/daya/young/faces/neutral.png"
    4
    "/daya/young/faces/neutral_blink.png"
    .15
    repeat
image d young sad = LiveComposite(
    (550,720),
    (0,0), "/daya/young/bodies/body.png",
    (0,0), "d young sad blink")
image d young sad blink:
    "/daya/young/faces/sad.png"
    4
    "/daya/young/faces/sad_blink.png"
    .15
    repeat
image d young happy = LiveComposite(
    (550,720),
    (0,0), "/daya/young/bodies/body.png",
    (0,0), "d young happy blink")
image d young happy blink:
    "/daya/young/faces/happy.png"
    4
    "/daya/young/faces/happy_blink.png"
    .15
    repeat
image d young laugh = LiveComposite(
    (550,720),
    (0,0), "/daya/young/bodies/body.png",
    (0,0), "/daya/young/faces/happy_blink.png")
image d young wink = LiveComposite(
    (550,720),
    (0,0), "/daya/young/bodies/body.png",
    (0,0), "/daya/young/faces/wink.png")
image d young surprised = LiveComposite(
    (550,720),
    (0,0), "/daya/young/bodies/body.png",
    (0,0), "d young surprised blink")
image d young surprised blink:
    "/daya/young/faces/surprised.png"
    4.5
    "/daya/young/faces/surprised_blink.png"
    .15
    repeat

# Mateus Goldenstring
define m = Character("Mateus Goldenstring")
image m young neutral = LiveComposite(
    (550,720),
    (0,0), "/mateus/young/bodies/body.png",
    (0,0), "m young neutral blink")
image m young neutral blink:
    "/mateus/young/faces/neutral.png"
    4.2
    "/mateus/young/faces/neutral_blink.png"
    .15
    repeat
image m young sad = LiveComposite(
    (550,720),
    (0,0), "/mateus/young/bodies/body.png",
    (0,0), "m young sad blink")
image m young sad blink:
    "/mateus/young/faces/sad.png"
    4.2
    "/mateus/young/faces/sad_blink.png"
    .15
    repeat
image m young happy = LiveComposite(
    (550,720),
    (0,0), "/mateus/young/bodies/body.png",
    (0,0), "m young happy blink")
image m young happy blink:
    "/mateus/young/faces/happy.png"
    4.2
    "/mateus/young/faces/happy_blink.png"
    .15
    repeat
image m young laugh = LiveComposite(
    (550,720),
    (0,0), "/mateus/young/bodies/body.png",
    (0,0), "/mateus/young/faces/happy_blink.png")
image m young surprised = LiveComposite(
    (550,720),
    (0,0), "/mateus/young/bodies/body.png",
    (0,0), "m young surprised blink")
image m young surprised blink:
    "/mateus/young/faces/surprised.png"
    4.7
    "/mateus/young/faces/surprised_blink.png"
    .15
    repeat

# Serin Quickstep
define s = Character("Serin Quickstep")
image s young neutral = LiveComposite(
    (550,720),
    (0,0), "/serin/young/bodies/body.png",
    (0,0), "s young neutral blink")
image s young neutral blink:
    "/serin/young/faces/neutral.png"
    3.5
    "/serin/young/faces/neutral_blink.png"
    .15
    repeat
image s young sad = LiveComposite(
    (550,720),
    (0,0), "/serin/young/bodies/body.png",
    (0,0), "s young sad blink")
image s young sad blink:
    "/serin/young/faces/sad.png"
    3.5
    "/serin/young/faces/sad_blink.png"
    .15
    repeat
image s young happy = LiveComposite(
    (550,720),
    (0,0), "/serin/young/bodies/body.png",
    (0,0), "s young happy blink")
image s young happy blink:
    "/serin/young/faces/happy.png"
    3.5
    "/serin/young/faces/happy_blink.png"
    .15
    repeat
image s young laugh = LiveComposite(
    (550,720),
    (0,0), "/serin/young/bodies/body.png",
    (0,0), "/serin/young/faces/happy_blink.png")
image s young surprised = LiveComposite(
    (550,720),
    (0,0), "/serin/young/bodies/body.png",
    (0,0), "s young surprised blink")
image s young surprised blink:
    "/serin/young/faces/surprised.png"
    4
    "/serin/young/faces/surprised_blink.png"
    .15
    repeat

# An'diel Rosesong
define a = Character("An'diel Rosesong")
image a young neutral = LiveComposite(
    (550,720),
    (0,0), "/andiel/young/bodies/body.png",
    (0,0), "a young neutral blink")
image a young neutral blink:
    "/andiel/young/faces/neutral.png"
    3.3
    "/andiel/young/faces/neutral_blink.png"
    .15
    repeat
image a young sad = LiveComposite(
    (550,720),
    (0,0), "/andiel/young/bodies/body.png",
    (0,0), "a young sad blink")
image a young sad blink:
    "/andiel/young/faces/sad.png"
    3.3
    "/andiel/young/faces/sad_blink.png"
    .15
    repeat
image a young happy = LiveComposite(
    (550,720),
    (0,0), "/andiel/young/bodies/body.png",
    (0,0), "a young happy blink")
image a young happy blink:
    "/andiel/young/faces/happy.png"
    3.3
    "/andiel/young/faces/happy_blink.png"
    .15
    repeat
image a young laugh = LiveComposite(
    (550,720),
    (0,0), "/andiel/young/bodies/body.png",
    (0,0), "/andiel/young/faces/happy_blink.png")
image a young surprised = LiveComposite(
    (550,720),
    (0,0), "/andiel/young/bodies/body.png",
    (0,0), "a young surprised blink")
image a young surprised blink:
    "/andiel/young/faces/surprised.png"
    3.8
    "/andiel/young/faces/surprised_blink.png"
    .15
    repeat

# Ioriel Tanith
define i = Character("Ioriel Tanith")
image i young neutral = LiveComposite(
    (550,720),
    (0,0), "/ioriel/young/bodies/body.png",
    (0,0), "i young neutral blink")
image i young neutral blink:
    "/ioriel/young/faces/neutral.png"
    3.7
    "/ioriel/young/faces/neutral_blink.png"
    .15
    repeat
image i young sad = LiveComposite(
    (550,720),
    (0,0), "/ioriel/young/bodies/body.png",
    (0,0), "i young sad blink")
image i young sad blink:
    "/ioriel/young/faces/sad.png"
    3.7
    "/ioriel/young/faces/sad_blink.png"
    .15
    repeat
image i young sigh = LiveComposite(
    (550, 720),
    (0,0), "/ioriel/young/bodies/body.png",
    (0,0), "/ioriel/young/faces/sad_blink.png")
image i young happy = LiveComposite(
    (550,720),
    (0,0), "/ioriel/young/bodies/body.png",
    (0,0), "i young happy blink")
image i young happy blink:
    "/ioriel/young/faces/happy.png"
    3.7
    "/ioriel/young/faces/happy_blink.png"
    .15
    repeat
image i young laugh = LiveComposite(
    (550,720),
    (0,0), "/ioriel/young/bodies/body.png",
    (0,0), "/ioriel/young/faces/happy_blink.png")
image i young surprised = LiveComposite(
    (550,720),
    (0,0), "/ioriel/young/bodies/body.png",
    (0,0), "i young surprised blink")
image i young surprised blink:
    "/ioriel/young/faces/surprised.png"
    4.2
    "/ioriel/young/faces/surprised_blink.png"
    .15
    repeat

# The game starts here.

label start:
    $ a_friend = 0
    $ d_friend = 0
    $ i_friend = 0
    $ m_friend = 0
    $ s_friend = 0
    stop music fadeout 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    show text "This game is created solely for non-commercial purposes. This is a fan work created using characters and assets that are the property of Blizzard Entertainment." at truecenter
    with dissolve
    $renpy.pause(2, hard=True)
    hide text
    with dissolve

    show text "Kestrel Company is a work of fiction. Any resemblance to actual persons, living or dead, or actual events is purely coincidental..." at truecenter
    with dissolve
    $renpy.pause(1.5, hard=True)
    show text "\n\n\n\nThough in the lore of Warcraft, the events depicted actually happened." as text2 at truecenter
    with dissolve
    $renpy.pause(2, hard=True)
    hide text
    with dissolve
    hide text2
    with dissolve

    show text "This is the story of the Sin'dorei." at truecenter
    with dissolve
    $renpy.pause(2, hard=True)
    hide text
    with dissolve

# Define character gender and name.
label gender:
    "What pronouns would you prefer to use?"
    menu:
        "He/Him":
            $ pronoun_nom = "he"
            $ pronoun_obj = "him"
        "She/Her":
            $ pronoun_nom = "she"
            $ pronoun_obj = "her"
        "They/Them":
            $ pronoun_nom = "they"
            $ pronoun_obj = "them"

    "You want to use [pronoun_nom]/[pronoun_obj] as your pronouns?"
    menu:
        "Yes":
            jump name
        "No":
            jump gender

label name:
    python:
        pcname = renpy.input("What is your first name?", default="Adas")
        pcname = pcname.strip()
        if not pcname:
            pcname = "Adas"
        pcsurname = renpy.input("What is your surname?", default="Emberforge")
        pcsurname = pcsurname.strip()
        if not pcsurname:
            pcsurname = "Emberforge"
    "Your name is [pcname] [pcsurname]?"
    menu:
        "Yes":
            "Thanks, [pcname]. Welcome to the World of Warcraft... and may the Light protect you."
            jump prologue
        "No":
            jump name


##########################################
# Prologue: Wine in Silvermoon           #
##########################################

label prologue:
    show text "Chapter One" at truecenter
    $renpy.pause(1, hard=True)

    play music "/music/family.ogg" fadeout 0.5 fadein 0.5

    scene rooftop
    with dissolve

    "The night air is cool and gentle on your skin, a welcome reprieve from the day's hot sun."
    extend " At this hour, high up on the rooftops of Silvermoon, the busy elven city is quiet and peaceful."

    show s young neutral with dissolve
    s "Hiii!"

    "Perhaps you spoke too soon!"
    extend " A figure dives in from above, nimbly rolling on contact with the rooftop and coming to a stop."
    extend " Your friend beams at you and pulls you into a warm hug."

    show s young happy
    s "Hey [pcname], long time no see!"

    menu:
        "It's good to see you!":
            show s young happy
            $ s_friend += 1
            s "It's good to see you too! We've all been so busy, huh?"
            show s young neutral
            s "Mat's around here somewhere too! But, hmm, I think I've lost him."
        "Was that safe?":
            show s young happy
            s "Of course! You're starting to sound like Mat, worrying like that."
            show s young neutral
            s "Speaking of Mat, he was right behind me when I left..."

    "A much less dexterous figure clambers over the side of the building with a grunt. He collapses on the rooftop, exhausted."

    show s young neutral at left with move
    show m young sad at right with hpunch
    with dissolve

    m "Oof!"
    extend " Hey there, [pcname]. Just give me..."
    extend " a moment..."
    extend " to catch my breath."

    "After a few seconds of lying on the ground, Mat eventually gets to his feet and smiles at you."

    show m young neutral
    $ m_friend += 1

    m "It is good to see you! Though I wish we could all get together at ground level sometime. Someone's going to get hurt up here."

    s "If anyone's going to get hurt, it's going to be-"

    show a young neutral with Fade(.25, 0, .75, color="#06e8ff")
    show m young surprised
    show s young surprised

    "Your skin buzzes from the arcane energy still crackling in the air. It feels as if all of your hair is standing on end."

    "When your vision clears, another one of your friends stands on the rooftop, smelling faintly of singed hair and alchemical reagents."

    show m young neutral
    show s young neutral
    show a young happy
    a "I did it! The teleportation spell worked!"

    menu:
        "Good to see you An'diel!":
            a "Oh hey, [pcname]! And Serin and Mat are here too!"
            $ a_friend += 1
            show a young sad
            a "I'm glad I made it to the right place! The spell's a little unstable. I think I might be mispronouncing part of the incantation..."
        "'Worked'?":
            show a young sad
            a "Well, it's a work in progress. I think I might be mispronouncing part of the incantation really; I end up in the sea a lot. Getting brine out of these robes is a pain!"

    show a young neutral
    a "But you know what they say, twenty-seventh time's the charm!"

    m "I hope you're being careful."

    show a young surprised
    a "I'm always careful!"

    "."
    extend "."
    extend "."

    show a young happy
    show m young happy
    show s young happy

    "Everyone bursts out into laughter at once."
    extend " Even An'diel can't keep a straight face, giggling at the thought of himself as a careful person."
    "Finally, Serin manages to stop laughing for long enough to spot two more figures climbing up the side of the wall."

    show s young neutral
    s "Hey!"

    d "PARTY'S COMING IN!" with hpunch

    hide a
    hide m
    hide s
    with dissolve
    show d young happy at left with dissolve
    "Daya leaps up triumphantly, bag heavy with clinking white bottles, each adorned with a crimson ribbon."
    show i young sigh at right with dissolve
    extend " Behind her is Ioriel, looking as exasperated as usual."

    i "Can we not shout? Honestly, you're going to get us in trouble."

    show i young sad

    menu:
        "Glad you could make it!":
            $ i_friend += 1
            show i young happy
            i "It's good to see you, [pcname]. And everyone else too!"
            show i young sad
            i "I'm sorry I couldn't make it last time."
            extend " Magistrix Erona really needed something and I couldn't get away, well I mean I could have but I didn't want to say no and-"
            jump ioriel_prologue_sad
        "Wine?":
            $ d_friend += 1
            d "Oh yes!"
            extend " The finest port wine in Quel'thalas, taken directly from the cellars of the Sunsworn vineyards!"
            jump daya_prologue_wine

label ioriel_prologue_sad:
    menu:
        "It's okay, Ioriel.":
            $ i_friend += 1
            i "-and..."
            show i young surprised
            i "Oh! Really?"

            show i at truecenter with move
            show m young happy at right with dissolve

            m "Definitely. When you're a powerful Magistrix, you'll have us all over, right?"

            show i young happy

            i "Of course! You all have standing invitations to my future mansion. Drop in anytime, you hear?"

            show d young wink
            d "Anytime?"

            show i young sigh
            i "I don't like that look in your eye..."

            hide m
            hide i
            with dissolve
            show d young neutral at truecenter with move

        "You should hang out with us more often.":
            $ i_friend -= 1
            i "Oh."
            extend " Yeah, of course. I'm sorry, everyone, I get carried away with my work sometimes."

            d "No kidding. You've gotta know how to relax too, you know."
            extend " Girl, you run around like the city will fall apart the moment you take a break."

            show i young laugh

            i "You never know, it just might!"

            hide i with dissolve
            show d young happy at truecenter with move
    jump prologue_2

label daya_prologue_wine:
    menu:
        "Did you steal it?":
            show d young surprised
            d "Of course not! I mean, I didn't buy it formally, but I left market price on the shelves."

            show d young neutral
            extend " Dame Sunsworn and I go way back. It's no big deal!"

            show i young neutral
            i "By 'way back', are you talking about how she's been chewing you out since you were a baby?"

            show d young laugh
            d "Pretty much!"

            hide i with dissolve
            show d young happy at center with move

            jump prologue_2
        "Fantastic! Let's have a toast?":
            $ d_friend += 1
            show i young neutral
            show d young happy
            d "You know how to live, [pcname]!"
            show d young neutral
            extend " But we won't need glasses. I brought six whole bottles, see?"

            show d at truecenter with move
            show a young surprised at left with dissolve

            a "You mean..."

            show d young happy
            d "Oh yes. One for each of us!"

            hide a
            hide i
            with dissolve
            show d young happy
            jump prologue_2

label prologue_2:
    d "But enough chitchat! We're all back together again, and that deserves a toast!"

    "Daya sets her bag gingerly on the rooftop, passing out the bottles of port wine."
    extend " An'diel and Serin accept theirs eagerly, while Mat looks rather dubious."

    "At last, Daya raises her own bottle of wine, popping the cork cheerfully."

    show d young happy
    d "Cheers!"
    extend " Here's to us, alright?"

    hide d with dissolve

    "Your friends cheer, six hands and six twinkling white bottles lifted high into the air."
    extend " You bring the bottle to your lips, taking a deep swallow."

    menu:
        "It's delicious!":
            $ wine_good = True
            "It's delicious! Definitely a quality vintage from the Sunsworn vineyards."
            extend " The tawny port is fortified, with a stronger breath of alcohol than regular wine. It tastes faintly of plum dipped in caramel."
            "The wine fills your chest with warmth."
            extend " It tastes like home."
            "But it seems like not everyone's enjoying the drink so much."
        "It's disgusting!":
            $ wine_good = False
            $ a_friend += 1
            "You're not entirely sure what you were expecting. The port wine is much stronger than the wines you've tasted at home."
            extend " You're not entirely sure why adults drink this stuff."
            "But it seems you're not the only one not enjoying the drink."

    show a young surprised at truecenter with dissolve

    "An'diel spits out his mouthful of wine, coughing."

    a "Ack!"
    extend " It's... it's really gross!"

    "Everyone bursts into laughter, to An'diel's chagrin."

    show a young sad

    a "Hey! It's not my fault, I'm just, um..."
    extend " more used to sweet wines, that's all!"

    show d young neutral at right with dissolve

    d "It's alright! I hated wine at first, but part of being in a noble house:"
    extend " they expect you to knock 'em back with a smile by ten!"

    # REVISION: Move Serin to right-side of screen.

    show s young neutral at left with dissolve

    s "I've got a canteen of pomegranate juice if you want instead!"

    show s young happy

    extend " It's Bel's favorite!"

    "Bel, the little emerald serpent coiled in Serin's hair, hisses its approval."
    extend " He seems to be giving An'diel permission to have some juice."

    show a young happy

    a "Yeah, I think I'd prefer that. Thanks, Serin. And Bel too!"

    s "Anytime!"

    hide a with dissolve
    show i young neutral at truecenter with dissolve

    i "So what have you been up to since I saw all of you last?"
    show i young happy
    extend " It's been a while since we've caught up."

    menu:
        "Been practicing my dueling.":
            $ history = "warrior"
            jump prologue_warrior
        "Been studying magic.":
            $ history = "mage"
            jump prologue_mage
        "Been at court with my parents, mostly.":
            $ history = "noble"
            jump prologue_noble

label prologue_warrior:
    $ m_friend += 1
    $ s_friend += 1

    show i young neutral

    s "Ooh, I think I heard about that! You're making a real name for yourself!"

    i "Swordsmanship, huh? Do you think you'll be a Guardian one day?"

    menu:
        "I think so, yes!":
            $ i_friend += 1
            show i young happy
            i "I'll have to work doubly hard to keep up with that kind of enthusiasm!"

            s "Maybe you'll even get to meet the Ranger-General!"

            show d young wink
            d "Now wouldn't you like that, huh Serin?"

            show s young surprised

            s "Eep!"
            extend " I just think Ranger-General Windrunner is really cool!"

            show s young neutral
        "I'd rather be an adventurer, I think!":
            $ d_friend += 1
            show d young happy
            d "Hey, that sounds like a lot of fun!"
            extend " See the world, meet interesting monsters, kill them."
            d "I hope you know, if you go traipsing off on adventures without me, I'm never going to forgive you!"

    hide d with dissolve
    show m young neutral at right with dissolve

    m "My father's been on my case about training. Will you help me out sometime, [pcname]?"

    menu:
        "Of course!":
            $ m_friend += 1
            show m young happy
            m "Thanks!"
            extend " You've always been a great fighter. I'll do my best not to slow you down!"
        "I'm pretty busy...":
            m "No worries! I know you're always working so hard."
            show m young happy
            extend " I'll have to try and follow your example!"
    hide m
    hide i
    hide s
    with dissolve

    jump prologue_friends

label prologue_mage:
    $ i_friend += 1
    $ a_friend += 1

    show i young neutral

    i "Ah, you too? There's so much magic in Silvermoon, we can study in the same field and never cross paths."

    i "I see An'diel more often, though it's usually to make sure he hasn't accidentally blown himself up."

    hide s with dissolve
    show a young happy at left with dissolve

    a "Yep! Ioriel's helped me clean up a lot of messes."
    show a young surprised
    extend " I owe her one! Or, uh, a whole lot of ones!"

    show i young sigh

    i "I just want to make sure you're alright."

    show a young neutral
    show i young neutral

    i "How are your studies going though, [pcname]?"

    menu:
        "Excellent! I'm learning a lot.":
            $ i_friend += 1
            show i young happy
            i "You're such a hard worker. I really admire that!"

            show d young surprised
            d "Ugh, nerd flirting."
            extend " I."
            extend " Am."
            show d young wink
            extend " Disgusted!"

            hide d
            hide i
            hide a
            with dissolve
        "Uh, they're... ok.":
            $ a_friend += 1
            show i young sad
            i "Hmm, that doesn't sound good."

            show a young surprised
            a "That's how I feel!"
            extend " Magic is so cool, but all they want us to do in lessons is repeat stuff!"

            show a young sad

            extend " My marks are awful!"

            show i young sad
            i "Ah... that's not good."

            show i young neutral
            i "Well, perhaps we should study together sometime."
            extend " It's always more productive working with a group!"

            hide i
            hide d
            hide a
            with dissolve

    jump prologue_friends

label prologue_noble:
    $ i_friend += 1
    $ m_friend += 1
    $ d_friend += 1

    show d young sad
    d "Oof, sorry about that."

    menu:
        "Court functions are important.":
            $ i_friend += 1
            show d young surprised
            d "Oh Light, you sound like Ioriel!"
            extend " She's replaced you with a magic clone, hasn't she? Aaaah!"

            show i young laugh
            i "And for your meddling, you'll be next!"

            d "Nooooooo!"

            show s young happy
            show i young neutral

            "Serin laughs brightly, ignoring Ioriel and Daya's familiar banter."

            s "You're always so responsible, [pcname]. I'm sure the Convocation will be able to count on you!"
            show s young neutral
            extend " I don't know much about politics, but I know you'll do a good job."

            hide d
            hide i
            hide s
            with dissolve


        "I know, right?":
            $ d_friend += 1
            $ m_friend += 1

            hide s with dissolve
            show m young neutral at left with dissolve

            m "Court functions can drag on and on, can't they?"
            extend " I brought my little brother to one, and he was squirming in his seat all day!"

            d "They definitely make those seats uncomfortable on purpose."

            show i young surprised

            i "Court is important! With all the important decisions being made, it's vital we make our voices heard."

            show d young neutral

            d "But will they hear our voices clamoring for more comfortable chairs?"

            show i young neutral

            i "Perhaps we can start a petition!"

            hide m
            hide d
            hide i
            with dissolve
    jump prologue_friends

label prologue_friends:
    $ andiel_uncool = False
    $ talked_to_andiel = False
    $ talked_to_daya = False
    $ talked_to_ioriel = False
    $ talked_to_mat = False
    $ talked_to_serin = False
    $ talked_to_someone = False

    "Hours pass in what feels like moments as you and your friends laugh and chatter, catching up after too long spent apart."
    if wine_good == True:
        "You find yourself quickly emptying the bottle of delicious summerwine, and An'diel happily proffers you his."
        "Daya swipes it neatly before you can take it, giving you a mischievous wink before taking a swig."
        extend " She grins, holding it back out to you with a laugh."
    if wine_good == False:
        "You and An'diel pass Serin's canteen of pomegranate juice back and forth, watching bemusedly as Serin and Daya cheerfully toast to having extra wine."
        "Ioriel and Mat hover nervously around them like mother hens, ever the worriers."

    "Eventually, you find yourself a moment to speak with one of your friends alone."

label prologue_talk_menu:
    menu:
        "An'diel" if talked_to_andiel == False:
            $ talked_to_someone = True
            jump prologue_andiel
        "Daya (WIP)" if talked_to_daya == False:
            $ talked_to_someone = True
            jump prologue_daya
        "Ioriel (WIP)" if talked_to_ioriel == False:
            $ talked_to_someone = True
            jump prologue_ioriel
        "Mat (WIP)" if talked_to_mat == False:
            $ talked_to_someone = True
            jump prologue_mat
        "Serin (WIP)" if talked_to_serin == False:
            $ talked_to_someone = True
            jump prologue_serin
        "Done talking" if talked_to_someone == True:
            jump prologue_conclusion

label prologue_andiel:
    show a young neutral with dissolve
    $ talked_to_andiel = True

    if wine_good == False:
        "An'diel grins widely as you take a spot beside him."

        a "Hey, [pcname]!"

        a "You didn't like the wine either, huh?"
        extend " Port wine... it's a lot stronger than I expected. But it's kind of a relief you didn't like it, actually!"
        a "I wouldn't want to be uncool, you know? But you're always so... so self-assured, [pcname]!"

        show a young happy
        "An'diel beams at you, admiration clear on his face."
        extend " No one would ever call you uncool!"

    if wine_good == True:
        "An'diel smiles as you take a spot beside him."

        a "Hey, [pcname]."

        show a young sad
        a "Sorry about earlier. Port wine... it's a lot stronger than I expected."
        extend " I didn't seem super uncool, did I?"

        menu:
            "No, not at all!":
                show a young happy
                a "Oh, phew! That's a relief to hear, [pcname]."
                a "I know I can be kinda... you know, lame sometimes."
                extend " But you're always so self-assured, you know?"

                "An'diel beams at you, admiration clear on his face."
                a "I want to be more like you!"

            "Yeah, you were kind of uncool.":
                $ andiel_uncool = True
                show a young surprised
                a "Oh no, really?"

                show a young sad
                a "I thought so..."
                extend " Sorry, [pcname]. I know I can be kind of a loser sometimes."
                a "I don't get out to parties and things, much."
                extend " Always messing around with magic instead, you know?"

                "An'diel looks hurt, his eyebrows briefly knitting together. The expression quickly fades however, replaced by a smile that seems only slightly forced."

                show a young neutral
                a "But hey, I'm here now! And that's what counts!"

    if history == "mage":
        show a young neutral
        a "Anyway, how's your mentor treating you? It was Magister Sendath teaching you magic, right?"
        show a young surprised
        a "Magistrix Erona keeps us to the grindstone!"
        extend " It's always 'there is much for you to do!' every single day."
        extend " We never get a chance to just... figure things out."

        menu:
            "He keeps us very busy.":
                show a young surprised
                a "Right? It's like they want to take all the fun out of doing magic."
                extend " Magistrix Erona definitely thinks spellcasting should be work!"
                show a young neutral
            "I don't think he's realized he has students yet.":
                show a young surprised
                a "What, really? That's crazy!"
                extend " I can see that though. If I had the resources the Magisters have, I'd probably get caught up in the lab too."
                a "I kinda wish Magistrix Erona would forget about us occasionally, though."
                extend " She definitely thinks spellcasting should be work!"
                show a young neutral

    if history == "warrior":
        show a young neutral
        a "Dueling though, huh?"
        extend " That's pretty cool! I'm no good at swordfighting, but I'd like to see you compete sometime."
        show a young sad
        a "If I ever get a free moment. Magistrix Erona keeps us to the grindstone!"
        extend " It's always 'there is much for you to do!' every single day."
        show a young neutral

    if history == "noble":
        show a young neutral
        a "Out at court, huh?"
        extend " I'm supposed to attend a public debate for class. Maybe I can go when you do?"
        show a young sad
        a "If I ever get a free moment, that is! Magistrix Erona keeps us to the grindstone!"
        extend " It's always 'there is much for you to do!' every single day."

    show a young surprised
    a "Ioriel loves her, though."
    extend " I swear she's secretly a construct... it's like she never gets tired!"
    a "No matter what the Magistrix asks for, she's got it done before sunset."

    show a young neutral
    a "I kind of envy her, you know?"
    extend " She's so... capable. She knows what she wants to do, and she knows how to get there."
    a "She's kind of like you, [pcname]."

    a "..."
    extend " The youngest magistrix in Silvermoon history."
    extend " I think she could definitely do it, too!"
    a "But me, I..."

    show a young sad
    "The boy hesitates, not meeting your eyes."

    a "I don't really know what I'm doing, you know?"
    extend " I'm just messing around with magic and my marks aren't even all that great."

    a "I want to do big, cool things, you know? Magic is so exciting!"
    show a young happy
    extend " Like that teleport, earlier! That was cool. And it didn't come from a book, I figured it out myself!"

    show a young sad
    a "Sorry, [pcname], for getting all serious on you. It just..."
    extend " kinda all slipped out. Must be the starlight."

    menu:
        "I believe in you, An'diel.":
            show a young surprised
            a "Oh!"

            show a young happy
            a "Thanks, [pcname]."
            a "It really means a lot to hear you say that, you know?"

            show a young neutral
            a "I'm going to do something incredible, just you wait."
            extend " I'm going to invent a spell like no one's ever seen! It's going to change the world!"
            show a young happy
            a "And I hope you'll be there when I unveil it!"

        "It's okay, I don't know what I'm doing either.":
            show a young surprised
            a "Really? I never would have expected that from you."
            a "You've got this quiet kind of intensity, you know? Like you're always three steps ahead."

            show a young neutral
            a "I guess if you don't have everything together, I've got some time to keep up, huh?"
            show a young happy
            a "I'm going to invent a spell that's going to change the world, just you wait!"

        "You have to be willing to do whatever it takes.":
            a "Yeah..."
            extend " you're right. I guess I'm not giving it my all right now, huh?"
            a "The rest of you guys are all working really hard."
            extend " I'm going to be right there with you, you hear?"

            show a young happy
            a "I'm going to invent a spell that's going to change the world, just you wait!"
    show a young neutral
    a "Thanks, [pcname]."
    a "Thanks for hearing me out. You're a really good listener, you know?"

    a "Anyway, I'm going to go grab a snack. Catch you in a sec!"

    hide a with dissolve
    "An'diel bounces back to the rest of the group, where - true to his word - someone has produced several pastries."


    "The night sky twinkles overhead. You think there's still time to speak with someone else."

    jump prologue_talk_menu

label prologue_daya:
    show d young happy with dissolve
    $ talked_to_daya = True

    "Daya grins widely as you approach, throwing out her arms with a flourish."

    d "Ah, [pcname]! Welcome to my boudoir."
    extend " Please, make yourself comfortable. Treat yourself to some refreshments."

    menu:
        "It's good to see you too, Daya.":
            show d young wink
            "The girl winks at you, cheer written on her features."
            d "Don't you know it!"
        "Ah, Lady Elenvir! It is an honor!":
            show d young wink
            "The girl snickers, dipping into a cheerful curtsy."
            d "Oh by the Light, I can't keep that up."
        "Are you ever serious?":
            show d young wink
            "The girl winks at you, a smirk tugging at the corners of her mouth."
            d "Oh, you know I try to avoid it."

    if wine_good == True:
        show d young happy
        d "The port's good though, isn't it?"
        extend " Old Lady Sunsworn's strict as an iron cord, but she knows wine."
    if wine_good == False:
        show d young happy
        d "Not a fan of port, though?"
        extend " It's a bit weird, yeah. Bites harder than you'd expect from wine."

    show d young neutral
    "After a while, Daya glances off at the horizon, her lips easing into a gentle grin."
    d "This is good."
    extend " Really, really good. I've missed you guys."
    d "It seems like as we get older, we see one another less and less."
    show d young sad
    d "I don't like that."

    menu:
        "I don't like it either.":
            show d young neutral
            d "Yeah. Growing older shouldn't mean losing touch with friends, yeah?"
        "Just part of growing up.":
            show d young wink
            d "For you, maybe. I think I'll just stay young and beautiful forever, thanks!"
            show d young neutral

    if history == "mage":
        show d young neutral
        "A glimmer of mischief plays across Daya's features."
        d "But anyway, I'm talking to the future Grand Magister, no?"
        extend " Watch yourself, Ioriel will turn you into a sheep for the job!"
        menu:
            "I'm not interested in power.":
                show d young neutral
                "Daya surveys you thoughtfully."
                extend " She smiles, slightly at first, and then warmly."
                d "Yeah, that does sound like you, [pcname]."
                extend " That's really cool. You don't ever let anything get to your head."
                show d young happy
                d "Me, I'd immediately abuse my authority as grand magister to outlaw plaid or something."
                extend " Plaid robes are definitely the most important problem plaguing Silvermoon today."
                d "Think you'd do a good job all the same. People who want to be in charge shouldn't always be."
            "I'm hoping to, yeah.":
                show d young surprised
                d "Whoa, you're really planning to, huh?"
                extend " Better you than me, that's for sure. You're pretty responsible."
                show d young happy
                d "I mean, I'd immediately abuse my authority as grand magister to outlaw plaid or something."
                extend " Plaid robes are definitely the most important problem plaguing Silvermoon today."
                d "Think you'd do a good job. But you will have to compete with Ioriel!"
            "Yes... they shall face my power. Power overwhelming!":
                "Daya breaks into laughter, covering her face to avoid spitting out a mouthful of wine."
                extend " She coughs, grabbing your shoulder as she tries to breathe."
                d "Your delivery! That was fantastic! You're a supervillain in the making, [pcname]."
                show d young neutral
                d "That's right, though. Kick ass and take names! We'll show 'em all, you know?"
                d "We're just kids now, but... world's ours. We'll show the world what we're capable of."
        show d young sad
        "As you speak, the girl hesitates, for a moment uncharacteristically awkward."
        extend " She takes a swig from her drink to fill the silence before meeting your eyes."
        d "Can I tell you something, though?"
        d "I wish I was taking classes with you guys."
        extend " The private tutor's fine, but... I don't know, I'd see you guys more. Get off the estate."

        show d young neutral
        "Daya shakes her head, her normal easy smile returning."
        d "Never mind, forget I said anything."

    if history == "warrior":
        show d young neutral
        ""

label prologue_ioriel:

label prologue_mat:

label prologue_serin:
    "WIP"
    "WIP"
    "WIP"

label prologue_conclusion:
    "WIP"

# This ends the game.

return

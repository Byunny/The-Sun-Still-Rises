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
    $ forgave_ioriel = False

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
            $ forgave_ioriel = True
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

    "Bel, the little emerald serpent coiled in Serin's hair, hisses his approval."
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

    "Serin's eyes twinkle brightly, excitement plain on her face."

    s "Do you think you could fight an orc? I bet you could fight an orc, [pcname]!"

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

    $ mage_difficult = False
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
            $ mage_difficult = True
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
        "Daya" if talked_to_daya == False:
            $ talked_to_someone = True
            jump prologue_daya
        "Ioriel" if talked_to_ioriel == False:
            $ talked_to_someone = True
            jump prologue_ioriel
        "Mat" if talked_to_mat == False:
            $ talked_to_someone = True
            jump prologue_mat
        "Serin" if talked_to_serin == False:
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
        a "Do you ever see Serin around? I know she's "
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

    if talked_to_andiel == False or talked_to_daya == False or talked_to_ioriel == False or talked_to_mat == False or talked_to_serin == False:
        "The night sky twinkles overhead. You think there's still time to speak with someone else."
    else:
        "The sun's almost risen. It's probably time to get going."

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
                d "I think you'd do a good job all the same. People who want to be in charge shouldn't always be."
            "I'm hoping to, yeah.":
                show d young surprised
                d "Whoa, you're really planning to, huh?"
                extend " Better you than me, that's for sure. You're pretty responsible."
                show d young happy
                d "I mean, I'd immediately abuse my authority as grand magister to outlaw plaid or something."
                extend " Plaid robes are definitely the most important problem plaguing Silvermoon today."
                d "Think you'd do a good job. But you'll have to compete with Ioriel!"
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

    if history == "warrior":
        show d young neutral
        d "But anyway, you sure shut up Loranar in the duelist's ring, huh?"
        extend " He sure had a big mouth for someone who dropped his sword the instant you lunged!"
        show d young sad
        d "Sorry I couldn't make it to your match. Dad..."
        extend " doesn't believe swordsmanship is a hobby for a 'lady of good breeding'."
        menu:
            "The real fights are after hours anyway.":
                show d young happy
                d "[pcname]! Are you telling me you're part of an underground fight club?"
                d "Wicked cool. Light, how do I show up to that party? Get me an invite, will you?"
                show d young neutral
                d "You're really living your life, huh? That's really cool, [pcname]."
                extend "I'll be right there behind you, alright? Ten thousand years from now, we'll see who's the bigger badass!"
            "We all have responsibilities.":
                show d young sad
                d "Ugh, you're sounding like Ioriel. Or Mat! Responsibilities this, responsibilities that."
                d "Lugging twelve pounds of lace around some puffed up noble's house isn't responsibility."
                extend "I swear, some nobles think they're actually better than everyone just because their parents had money."
                d "Ioriel's a thousand times the person any of them are. Girl never takes a break, jeez."
                "Daya sighs, brows furrowed in frustration."
                d "Sorry, I've just had my dad on my case lately."
                show d young wink
                d "You watch out though, [pcname]! I've been training, and I'll be seeing you in the ring eventually!"
        show d young sad
        "The girl's grin falters as Daya hesitates, for a moment uncharacteristically awkward."
        extend " She takes a swig from her drink to fill the silence before meeting your eyes."

    d "Can I tell you something, though?"
    d "I feel bad about being unhappy."
    extend " I mean, for real, my family's rich. Dad's influential, or whatever that means."
    extend " We have chefs preparing stuff like... like saffron lobster and caviar at the family dinners I skip."
    d "My life is so... privileged. All I gotta do is look pretty and pretend to care. Easy!"
    extend " Ioriel is working night and day to get what I could just ask dad for!"
    extend " But Light, if I don't hate every second of it. I just want to get out."
    show d young neutral
    d "Sorry, [pcname]. I'm, er, drunk. Don't mind me!"
    menu:
        "You're right, you should be content.":
            show d young sad
            d "I... yeah, you might be right. Lots of people are worse off."
            extend " Forget I said anything, okay? I'll take your advice."
            extend " Thanks, [pcname]."
        "You should do what makes you happy.":
            show d young surprised
            d "I... don't know what that is. You don't think I'm being stupid and whiny?"
            extend " Maybe you're right. I guess no one should feel obligated to be happy."
            extend " Thanks, [pcname]."

    d "You're too easy to talk to, yikes! I bet people just spill their secrets to you."

    d "Anyway, my cup runneth dry. I'll catch you later."

    hide d with dissolve
    "Daya takes off, giving you a cheerful wave."

    if talked_to_andiel == False or talked_to_daya == False or talked_to_ioriel == False or talked_to_mat == False or talked_to_serin == False:
        "The night sky twinkles overhead. You think there's still time to speak with someone else."
    else:
        "The sun's almost risen. It's probably time to get going."

    jump prologue_talk_menu

label prologue_ioriel:
    show i young neutral with dissolve
    $ talked_to_ioriel = True

    "Ioriel looks a little anxious, keeping an eye on everyone as usual, but she smiles warmly as you approach."

    i "Hello [pcname]. Thank you for organizing all of this, by the way!"
    extend " We always mean to meet up, but it doesn't happen as often as we'd like."

    if forgave_ioriel == True:
        show i young happy
        i "Thanks for being understanding, by the way. I really do want to spend time with you guys, but..."
        show i young sigh
        i "There's just always so much to do. It feels like whenever one thing gets done, there's something else I'm behind on."

    else:
        show i young sad
        i "I wanted to apologize about that, by the way. You're my friends, and you're important to me."
        extend " I should make more of an effort to stay in contact with you guys."
        show i young sigh
        i "There's just always so much to do. It feels like whenever one thing gets done, there's something else I'm behind on."

    menu:
        "I'm sorry, Ioriel.":
            show i young neutral
            "Ioriel shakes her head, smiling at you."
            i "Nothing to be sorry about! I don't have to volunteer to take on extra work."
        "You bring it on yourself, you know.":
            show i young neutral
            "Ioriel nods, a serious look in her eye."
            i "I know. I'm the one who chose to take on the extracurricular work."

    show i young sad
    i "But... I do have to. There's only so many spaces in the Magisterium."
    extend " Some of the older Magisters have been in power for over a millennium!"
    i "There are a lot of mages from prestigious bloodlines vying for position."
    extend " If I'm going to apprentice with the Magisterium, I need to stand out. I don't have a name to fall back on..."
    show i young surprised
    i "Oh! I'm wallowing again. I'm sorry, [pcname]! I don't mean to bring down the mood!"

    show i young neutral
    i "You're all working so hard. Serin's practically a shoe-in for the Farstriders, Mat's pretty much already the patriarch of his house..."
    if history == "warrior":
        i "And I have it on good authority that you're one of the most talented warriors to lift a twinblade in centuries, hm?"
    if history == "mage":
        if mage_difficult = True:
            i "And you were being humble, [pcname]. Some of the spells you've designed are incredible, even if it doesn't reflect in marks."
            i "There are more important things than academic grades."
            "Ioriel blinks, covering her mouth with one hand."
            i "Don't tell Daya I said that. She'll never let me forget it!"
        if mage_difficult = False:
            i "And I've heard Magistrix Erona talking about you. You're one of the best students Quel'thalas has to offer."
    if history == "noble":
        i "And I've heard Magistrix Erona talking about you. You've been making quite a stir at court!"

    show i young happy
    i "I've got to keep up with everyone!"

    menu:
        "I think people are trying to keep up with you!":
            show i young surprised
            i "Oh!"
            i "I wouldn't say so. I'm just barely scraping by."
        "We're all doing great.":
            show i young happy
            i "Definitely!"

    show i young neutral
    "Ioriel glances over at your friends, biting her lip as Serin attempts to teach a wobbly Daya how to tumble while Mat frets."

    show i young sigh
    i "I don't... know if it's going to be enough, though."
    extend " I'm so tired all the time, some of my work's been slipping. Magistrix Erona has noticed."
    show i young sad
    i "The others... they think I'm doing so well. The smart girl, always getting top marks. A little insufferable."
    extend " I feel like I'm going to let them down. Some of the other students can already open portals from Silvermoon to Lordaeron!"
    i "If I don't get to apprentice in the Magisterium..."
    extend " mother and father have already put so much into my studies and they really can't afford it."

    show i young sigh
    i "Sorry! Sorry, I'm venting. You should go spend time with the others, I just need a moment to compose myself."

    menu:
        "It's okay to feel unsure.":
            show i young sad
            "Ioriel glances at you, biting her lip."
            i "Is it? I just want to do something worthwhile. There's so much we still need to do to make Silvermoon better. For everyone."
            i "I don't know if I can do it, sometimes."
        "You're going to succeed. I know it.":
            show i young sad
            "Ioriel glances at you, biting her lip."
            i "I hope you're right, [pcname]."
            extend " There's so much that needs to be done to make Silvermoon a better place. For everyone."
            i "I hope I can do it."
        "I'm here for you, Ioriel.":
            show i young surprised
            i "I..."
            "Ioriel turns her head away, rubbing her eyes. She coughs, glancing back at you."
            show i young neutral
            i "Thank you, [pcname]. I think that might have been what I really needed to hear."
            i "I want to make Silvermoon better. I hope... I think I can."

    show i young neutral
    i "Thanks for hearing me out, even though I'm being no fun."
    i "You're a good friend, [pcname]. I hope we get more chances to see each other from now on!"
    i "Now, I should probably go make sure Daya doesn't hurt herself!"

    hide i with dissolve
    "Ioriel gives you a genuine smile before heading back to the group."

    if talked_to_andiel == False or talked_to_daya == False or talked_to_ioriel == False or talked_to_mat == False or talked_to_serin == False:
        "The night sky twinkles overhead. You think there's still time to speak with someone else."
    else:
        "The sun's almost risen. It's probably time to get going."

    jump prologue_talk_menu

label prologue_mat:
    show m young neutral with dissolve
    $ talked_to_mat = True

    "Mat frets over your friends' shenanigans as he often does. The oldest of a half dozen children, he's always the big brother."
    "As you approach, the boy smiles warmly at you."

    m "Oh hey, [pcname]! Good to get a moment to chat."
    show m young happy
    m "It's really nice, getting everyone back together again. It's been too long."
    show m young neutral
    m "But what about you, [pcname]?"

    if history == "warrior":
        extend " I know you're working hard on your swordsmanship, but how has life been otherwise?"
    if history == "mage":
        if mage_difficult = True:
            extend " I know school's been a pain, but how has life been otherwise?"
        if mage_difficult = False:
            extend " I know you've been doing really well in class, but how has life been otherwise?"
    if history == "noble":
        extend " I know you've been busy learning how the kingdom works, but how has life been otherwise?"

    menu:
        "I've been great!":
            show m young happy
            m "I'm glad to hear it! Life's been a little up in the air for a lot of us, so I'm happy you're faring well."
            show m young neutral
            m "You're usually pretty stoic, huh? I admire that. It seems like you've always got your feet under you."
        "It's been rough, sometimes.":
            show m young sad
            m "I'm sorry, [pcname]. I've got your back, okay? Let me know if there's ever anything I can do to help out."
            show m young neutral
            m "We're friends! That means we look out for one another. Don't hesitate to let me know, okay?"
        "I want to hear how you've been!":
            show m young neutral
            m "Oh no, [pcname], you're always taking care of other people. I gotta check in on you, you hear?"
            m "Things have been a little up in the air. Have to keep in mind we've got friends to support us!"
            m "I'm doing well, though. Thanks for asking."

    menu:
        "You worry too much, Mat.":
            m "Haha, sorry about that! I don't mean to pry or anything."
        "Thanks, Mat.":
            show m young happy
            m "Of course!"

    show m young neutral
    m "I just want to make sure my friends are doing okay, you know? I worry about you guys, sometimes."

    menu:
        "About An'diel?":
            show m young sad
            m "Yeah, sometimes. He really works hard, but..."
            extend " he's always comparing himself to Ioriel, and I don't think that's good for him."
            show m young neutral
            m "He's talented and hardworking and creative. He's got a lot to be proud of."
            show m young sad
            m "The Magistrix... all of those Magisters, they seem more inclined to be cruel than supportive."
            extend " There's no way that's the best way to teach!"
        "About Daya?":
            show m young sad
            m "Yeah, sometimes. She's always smiling and making fun, but..."
            extend " her family wears her down. They expect her to be someone she's not."
            m "They've even got her feeling guilty for it! I really hope she'll be okay."
        "About Ioriel?":
            show m young sad
            m "Yeah, sometimes. She seems like the model student, but..."
            extend " she's too hard on herself. Everyone expects her to be perfect, most of all herself."
            m "It's a lot of pressure, I think. That's a lot of stress for anyone, even someone as smart as Ioriel."
        "About Serin?":
            show m young sad
            m "Yeah, sometimes. Serin's brave and skilled, but I wish she'd be a little more careful sometimes."
            extend " I'm worried she's going to get hurt trying to save the world or something."
        "About me?":
            show m young sad
            m "Yeah, sometimes. For what it's worth, everyone looks up to you, you know?"
            extend " People trust you. Our friends trust you. But I don't want you to feel... I don't know, too responsible for everyone?"
            m "That's probably hypocritical to say. But I mean it! Make sure to make time for yourself, ok?"

    show m young surprised
    m "But ah! I'm becoming a gossip. You all already think I'm stodgy, I can't act like this!"

    show m young neutral
    m "But I do think we're all going to be okay in the end."
    show m young happy
    m "I believe in us!"

    show m young neutral
    m "Anyway, those look like mana doughnuts! I haven't had one in ages."
    m "One of my little sisters - Reya, you remember? - wanted to try this new diet plan with someone and it's terrible!"
    show m young surprise
    m "Forgive me, Reya, but I think I'm being led astray!"

    hide m with dissolve
    "Mat gives you a warm hug before heading over to pick up a pastry."

    if talked_to_andiel == False or talked_to_daya == False or talked_to_ioriel == False or talked_to_mat == False or talked_to_serin == False:
        "The night sky twinkles overhead. You think there's still time to speak with someone else."
    else:
        "The sun's almost risen. It's probably time to get going."

    jump prologue_talk_menu

label prologue_serin:
    show s young neutral with dissolve
    $ talked_to_serin = True

    "Serin laughs brightly, nimble on her feet despite the port wine."
    extend " She beams at you as you approach."

    s "Hey hey, [pcname]!"

    if history == "warrior":
        "The girl pulls a baguette from a picnic basket, leveling it at you."
        s "Aha! The mighty Troll King, mightiest of warriors! Lift your weapon and face me!"
    if history == "mage":
        "The girl pulls a baguette from a picnic basket, leveling it at you."
        s "Aha! A sinister necromancer! Muster your sorcery and face me!"
    if history == "noble":
        "The girl pulls a baguette from a picnic basket, leveling it at you."
        s "Aha! The most cunning advisor of Queen Azshara herself! Your silver tongue shall not save you now!"

    menu:
        "You underestimate my power!":
            show s young happy
            "Serin giggles, swapping the blade of bread to her other hand and bopping your shoulder."
            s "But I am not right-handed! Prepare to die!"
        "I surrender!":
            show s young happy
            "Serin giggles, poking you with the baguette."
            s "Very well. I'll let you go this time, villain!"
        "You're being silly, Serin.":
            show s young happy
            "Serin giggles, tossing a grape at you."
            s "You're no fun, [pcname]. C'mon!"

    show s young neutral
    "The ranger-in-training takes a seat, ripping a chunk off of her baguette. She offers you the bread, still smiling."

    s "It's good to be back in Silvermoon. Being out in Eversong is fun, but patrolling so often, I've really missed you guys! And Bel has missed you too."
    "The little snake hisses his assent."

    menu:
        "Doing well with the Farstriders?":
            s "Absolutely! It's tough keeping up sometimes, but they're really cool."
            extend " I want to be like them. Fast, strong, clever... protecting Silvermoon like a real hero, you know?"
            show s young surprised
            s "Also I got to meet the Ranger-General! She's really cool, and so beautiful... and a little bit scary. But she is a legend, after all."
        "Missed you too!":
            s "Aww!"
            extend " Maybe you could come join me? I don't know the other trainees that well, and it would be nice to have a friend along."
            s "We could defend Silvermoon together! [pcname] [pcsurname] and Serin Quickstep, protectors of Quel'thalas!"
        "I did miss Bel a lot.":
            "Serin grins, even as the little serpent bobs his head proudly."
            s "You're the worst, [pcname]. You know the silly little snake has no head for flattery."

    show s young happy
    s "But you've been keeping busy too!"

    if history == "warrior":
        extend " A duelist swifter than Maiev Shadowsong! The hero of the War of the Ancients!"
    if history == "mage":
        extend " A sorcerer as impressive as Dath'remar Sunstrider! Like the first High King of Quel'thalas!"
    if history == "noble":
        extend " An orator more charming and hypnotic than Queen Azshara herself! Ruler of the Highborne!"

    show s young neutral
    s "Or at least, that's what the stories say."
    "Serin looks thoughtful for a moment, gazing up at the stars."

    s "Do you think there will be legends about you someday?"

    menu:
        "Definitely.":
            show s young happy
            s "That's the spirit!"
            show s young neutral
            s "I think you're right, [pcname]. I definitely think you can do something legendary."
            s "I hope I can too!"
        "I hope not.":
            show s young surprised
            s "Wow, really?"
            show s young neutral
            s "Don't be so humble, [pcname]! You could definitely do something legendary."

    s "Seems like a waste if we go our whole lives without doing anything worth telling stories about, right?"
    s "Even if it's only us telling the stories. I'd like to make a mark on the world at least a few times in the next few centuries."

    s "I think we all will, though. You, An'diel, Daya, Mat, Ioriel - especially Ioriel - we're all doing cool things."
    s "Promise you'll do lots of cool things so I can brag about knowing you, ok?"

    "Serin smiles at you before rising to her feet."

    s "Anyway, I did say I was going to teach An'diel how to do a backflip. It's going to be great!"
    s "We've got to hang out more often, alright? Catch you in a sec!"

    "And with that, she's off. Somehow, you get the feeling this backflip thing will go terribly wrong, but..."
    "It'll probably be fine."

    if talked_to_andiel == False or talked_to_daya == False or talked_to_ioriel == False or talked_to_mat == False or talked_to_serin == False:
        "The night sky twinkles overhead. You think there's still time to speak with someone else."
    else:
        "The sun's almost risen. It's probably time to get going."

    jump prologue_talk_menu

label prologue_conclusion:
    "The sun peeks over the horizon, painting Silvermoon crimson and gold. The six of you fall silent, staring off at the sunrise."

    scene black
    with dissolve

    "As the sun rises over that rooftop, surrounded by your closest friends, it really does seem like everything is going to be alright."

    jump chapter_one

# This ends the game.

return

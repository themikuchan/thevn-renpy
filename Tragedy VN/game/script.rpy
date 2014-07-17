init:
    $ d=Character(_("Diana"), color="FFBBDD", what_slow_cps=30)
    $ f=Character(_("Felix"), what_slow_cps=30)
    $ fc=Character(_("Felix's Cellphone"))
    image bg fivestar="Placeholder_resto2.jpg"
    image bg black="#000000"
    
#The game starts here

label start:
    scene bg fivestar
    with dissolve
    play music "07 Etude pour les petites supercordes.mp3"
    
    window show
    
    "I'm a little excited about tonight."
    "I finally gathered up enough courage to ask out Diana, the prettiest girl in my college class, to a dinner date at the L'amour Estragique."
    "Diana's known that I've had a crush on her for a while now, so you can imagine how asking her out was that much harder for me!"
    "She's not here yet, but I had decided to go sit down so that our reservations wouldn't go to waste."
    "Getting reservations here is near impossible, unthinkable even."
    "... For some people."
    "Hehehe... good thing I was able to get some help from Josh."
    "He's always been a good friend."
    "I'm sure he won't go looking for his credit card anytime soon."
    "That aside, I still can't believe that Diana... that Diana said yes. To me!"
    "Tall, slender, fair-skinned Diana, the girl who draws everyone's attention when she enters the room."
    "The girl with a mesmerizing, angelic voice."
    "The girl that people can't help but talk about..."
    "That girl agreed to go on a dinner date with yours truly!"
    "She even looked kind of happy about it."
    "We exchanged phone numbers after I asked her out, and here I am now."
    "This is literally the highest accomplishment I've ever gotten in my entire life."
    pause (1)
    "I should've asked girls out years ago."
    "If everything goes well tonight, I might just finally leave behind my miserable life of singlehood."
    pause (1)
    "Felix, whatever you do, don't mess this up!"
    "This chance may never come again! Ya hear that, brain?"
    "A once-in-a-lifetime opportunity!"
    "Seize it now; strike while the iron's hot!"
    "Make her fall for you! Be confident!"
    
    pause (1.5)
    stop music fadeout 1
    play music "hangouts_incoming_call.ogg"

    fc "*RING* *RING* *RING*"
    f "AAAAAAAAHHHHHHHHH!"
    
    "I almost fall out of my chair in surprise."
    "I fish my phone out of my pocket and check it."
    "..."
    
    "It's Diana calling!"
    "Alright Felix, it's now or never."
    "Show her that you're a man!"
    
    stop music
    play sound "hangouts_message.ogg"
    
    fc "*BEEP*"
    f "Hello?"
    d "Oh, Felix!"
    d "Look, I know this is gonna sound pretty embarrassing, but something just came up and I'm gonna be running just a bit late..."
    f "Wait, what? Are you alright?"
    d "I'm fine, but I don't have much time to talk right now."
    d "I'm really sorry!"
    d "I promise to get there as soon as possible!"
    d "Buuuut... it's gonna take a while."
    d "Maybe about another two hours."
    d "That okay with you?"
    
    "How should I respond?"
    
    menu:
        
        "Tell her you're okay with it.":
            jump route_a
        
        "Get angry at her for being late.":
            jump route_b
            
label route_a:
    "I take a deep breath and let out a sigh."
    "At least she was respectful enough to call in advance and apologize for the delay."
    "I should be happy that she's still thinking of meeting up and having dinner!"
    f "It's alright, really. Don't worry about me."
    f "I can wait for you. Take your time and call me again later if anything else comes up."
    d "Oh my gosh, thank you, thank you, thank you!"
    d "I'm really sorry again about all this!"
    d "I'll make it up to you later, okay?"
    "The way she said that made my heart skip a beat."
    f "I'll be waiting."
    f "And if there's anything else that I can help you with, don't hesitate to ask."
    f "Now go do what you need to do."
    d "Alright, I will."
    d "Thanks so much again, Felix! Bye!"
    fc "*BEEP* *BEEP* *BEEP*"
    play music "07 Etude pour les petites supercordes.mp3"
    "I think that went well."
    "... Two hours, huh?"
    "It's a stretch, but I guess I can wait that long."
    "This is a dinner with Diana, after all."
    "I might never get this chance again."
    "Two hours is a small price to pay for a night with her."
    pause (1)
    "That said, I wonder if it was too much to wear a suit and tie."
    "Hm..."
    "Probably not. Most people dining here are dressed similarly."
    "There's no strict dress code, but it seems like the people who go here choose to dress fancy anyways."
    pause (1)
    "A brief thought of Diana coming to dinner in a ball gown crosses my mind."
    "No, no."
    "Even that would be too formal for a simple dinner."
    "Maybe something a little more casual, like a cocktail dress."
    "Knowing Diana, she could pull it off and still look drop-dead gorgeous."
    "Maybe she's getting ready for tonight and that's why she's going to be late."
    "Hair, dress and makeup, probably?"
    "I check my watch. It's almost six in the evening."
    "Looks like I'm going to be waiting for a while."
    "Does she do this a lot? Do other people know she does this?"
    "Maybe it's just a habit of hers."
    "Or maybe she's forgetful."
    "Either way, I can live with it. It actually makes her a bit more endearing, now that I think about it."
    "Who knew that the elegant Diana had such a side to her?"
    "I wonder how much I've yet to find out..."
    f "Waiter, another glass, please..."
    
    scene bg black
    with dissolve
    
    pause(1)
    
    scene bg fivestar
    with dissolve
    
    "(Two hours later...)"
    "Eight o' clock. It's almost time she showed up."
    "My heart's going crazy."
    "What will she be wearing?"
    "Is she excited?"
    "Is she looking forward to this dinner?"
    "Dang, I just have so many questions..."
    "Just calm down, Felix."
    "You have to play it cool."
    "This is Diana we're talking about here."
    "Don't make a fool out of yourself."
    "It's hard trying to contain myself, though."
    "I can feel my leg bouncing up and down."
    "She's probably going to be here any minute!"
    "Oh man, I really want to see her!"
    "Even if there was a little bump in getting up to this point, I'm still pretty psyched about everything."
    "I wonder how she's doing right now..."
    
    pause (1.5)
    stop music fadeout 1
    play sound "hangouts_incoming_call.ogg"
    
    fc "*RING* *RING*"
    play music "07 Etude pour les petites supercordes.mp3"
    
    f "Huh? A message?"
    f "..."
    f "It's from Diana!"
    play sound "hangouts_message.ogg"
    
    fc "im really sorry felix but i won't be able to make it after all. really sorry. it was really nice of you to plan all this for me but maybe you can plan something else for us some other time okay? super duper sorry again i swear!!"
    f "..."
    
    "... What should I do?"
    menu:
        "Reply.":
            jump route_aa
        
        "Don't reply.":
            jump route_ab
    
label route_b:
    "I feel something inside me snap like a twig."
    "I can't believe she has the {i}nerve{/i} to be so blatantly disrespectful."
    "Before I can stop myself, the words were already coming out of my mouth."
    f "I went through a lot of trouble getting us these reservations, you know."
    f "The least you could do is show up on time."
    f "And if you wondering, no, I am {i}not{/i} okay with waiting for you for another two hours."
    f "It was hard enough putting all this together."
    d "..."
    d "... Felix, I'm so sorry..."
    "I hear sincerity in her voice. And was that a tinge of fear?"
    d "I didn't mean to piss you off... I just thought that..."
    "I roll my eyes. Time to set things straight." #Hell yes, do it FELIX. FOR MEN EVERYWHERE
    f "I'm only waiting for you until the next half hour, you got that?"
    "That gives her a slight pause."
    "While waiting for her to reply, I hear some noises in the background that sound suspiciously like music and sound effects from a video game."
    #Seriously, Diana? What a biiiiiiitch.
    d "..."
    d "... Okay."
    d "... I'll be there in thirty minutes... I promise."
    f "It's six o' clock right now. You can make it up to me when you get here."
    
    fc "*BEEP* *BEEP* *BEEP*"
    
    "Did she think she could get away with that?"
    "I'm not an idiot, Diana. If you're not interested in me, at least tell it to my face."
    "You can at least give me that much, instead of using all these innocent sounding excuses that you think will work on a guy like me."
    "I made plans for us, I asked you out, and you said yes. Changing your mind after all that just isn't fair."
    "You had your chance to reject me, and you didn't."
    "Why chicken out now?"
    "Don't tell me you just {i}like{/i} the idea of being desired?"
    "That you just {i}like{/i} what I'm doing for you because it satisfies your own ego?"
    "Did you even {i}consider{/i} reciprocating my feelings?"
    "And to think I was just praising you a while ago... well guess what, Diana?"
    "I am NOT your plaything."
    "Try playing with my feelings again and I will give up on you, end of story."
    pause (1)
    f "Waiter, another glass, please."
    
    scene bg black
    with dissolve
    
    pause(1)
    
    scene bg fivestar
    with dissolve
    
    "(Thirty minutes later...)"
    "I check my watch. It's half past six."
    "This is it, Diana. The moment of truth."
    "A waitress shuffles past behind me and it takes me a second to notice that she's been leading another lady toward my direction."
    "Waitress" "And this is your seat, Miss Diana. Thank you for choosing to dine at the L'amour Estragique."
    d "Oh... umm, you're welcome. And, uh, thank you too, I guess..."
    "Look who decided to show up after all, in jeans and a t-shirt, no less."
    "Seems like someone was in a hurry to get here."
    "The waitress leaves us and Diana takes a seat across the table."
    d "... Hey."
    "She can't even bear to look me in the eye."
    d "Look, Felix, I'm really sorry about being a jerk a while ago... That was a really bad move on my part."
    d "I didn't realize I was hurting your feelings like that..."
    d "This is the first time anyone has ever asked me out, you see... and..."
    d "I got nervous and felt that I didn't deserve it."
    d "Any of it."
    d "You planned such a big night for us it kinda scared me..."
    d "I was planning to apologize to you tomorrow in class and ask if we could start things over..."
    d "Felix, I'm really sorry about all that..."
    d "I'm here now, so... I hope you can forgive me..."
    f "..."
    "What should I do?"
    return

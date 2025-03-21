define Calem = Character('Calem', color = "#c5fffd", what_prefix='"', what_suffix='"')
define Steven = Character('Steven', color = "#2f39c7", what_prefix='"', what_suffix='"')

# define stats

default stamina_points = 10
default charisma = 0
default sleep = 0
default intelligence = 0
default happiness = 0
default romance = 0

label start:

    scene bg dark room
    with fade

    play sound "audio/sfx/notification.ogg"

    "{i}Ding!{/i}"

    "{i}Assignment Released: Your Test 3 for MATH2401 has been graded! You can access your graded submission through the link below!{/i}"
    
    Steven """
    It can't be that bad, right? I studied... somewhat. I think I did okay."
    
    ...

    Oh.

    I didn't even know the scores {i}went{/i} that low...
    """

    "{i}Student: Steven Vuong\nTotal Points: 7.5/100{/i}"

    play music ["audio/music/relaxing_massage.ogg"] fadein 1.0

    Steven "This sucks."

    "He promptly burrows his head in the mattress."

    Steven "Maybe I'll drop out. Or find a rich man to marry."

    Steven "What am I even paying tuition for at this point?"

    "Steven checks his contacts to find someone to complain about his awful score to."

    "Unfortunately, all three of his contacts haven't responded to the last message he sent them."
    
    Steven "Oh. Right."

    "Defeatedly, he flops back onto his bed and contemplates his life choices."

    Steven "I have four weeks until finals. If I study every day until then, I can probably get out with a… D, maybe?"

    Steven "A D's generous, actually."

    Steven "..."
    
    Steven "Well, that's that. Goodbye, degree. It was nice knowing you."

    "Reluctantly, he closes his eyes, thinking of how he'll break the news to everyone that he's dropping out."

    "..."

    Steven "God. This {i}really{/i} sucks."

    Steven "And I didn't even eat dinner! Maybe that'll fix everything."

    "With a sigh, Steven gets out of bed and heads to the kitchen."

    scene bg dark kitchen
    with fade

    "The electric kettle whirrs quietly."

    Steven "Dear ramen, save me from the horrors of today."

    play sound "audio/sfx/notification.ogg"

    "{i}Ding!{/i}"

    "{i}From Mom: How was your exam score?{/i}"

    Steven "Ah, I forgot..."

    "{i}From Steven: Don't know yet. The scores didn't come out{/i}"

    "{i}From Mom: Ok. let me know when you find out. Love you{/i}"

    Steven "Ugh..."

    Steven "I really need to tell her. Just, not now. Maybe tomorrow."

    "He places his hands on the kitchen counter, and sighs."

    Steven "I hate being an adult."

    stop music

    "Suddenly, the kettle begins to shake."

    Steven "That doesn't sound right."

    "It shakes even more violently, threatening to topple over."

    Steven "Okay, wait, please don't burn the place down..."

    "And then suddenly, it goes quiet."

    Steven "Phew. Maybe I should replace the kettle so-"

    play music ["audio/music/a_chill_fever.ogg"] fadein 1.0

    Calem "Whaaat?! It's so cool! It's all electric, and stuff!"

    Steven "Ah, fuck! Oh my god! Am I dying? Finally!"

    Calem "..."

    Calem "Hey, dude, are you alright?..."

    Steven "Gah!"
    
    Calem "Hi! Really sorry about that - I just got kinda excited by the fact that I see stuff again! I missed this!"

    Steven "Is this a symptom of psychosis?"

    Calem "No, no! I promise, you're not crazy! See, look!"

    "He sticks his hand through Steven's body, and waves at him."

    Steven "Ah! Okay, okay, I get it - Please don't ever do that again. Who {i}are{/i} you?"

    Calem "Sorry! I probably should've started with that - I'm Calem! I, uh..."

    "He pauses for a second."

    Calem "Okay, funny story: I don't really know that much about myself."

    Steven "What?"

    Calem "I mean, all of this stuff is really familiar! I know how it works, it's just - I feel like it's been so long!"

    Calem "Granted, I don't know {i}how{/i} long, but..."

    Calem "It doesn't really matter, anyways! I don't have a story, but you do! What's going on in your life, huh?"

    Steven "Do you {i}really{/i} want to know?"

    Calem "Yeah! So we can get to know each other, build trust, et cetera!"

    Steven "I mean... Okay, well, I'm Steven. Twenty years old, college student, unemployed, all that fun stuff."

    Steven "I'd love to say college is great, but it's pretty terrible."

    Steven "The math, the science, the resume stuff, the {i}networking{/i} - God, I hate networking the most."
    
    Steven "All so I can get a job, right?"

    Steven "But there's no guarantee I'll even get one. Mainly because my GPA is in {i}hell.{/i}"

    Steven "And if you ask me, I really don't care about any of this. I just want a job that'll give me enough money to stop eating ramen every day."

    Calem "Ah."

    Calem "I forgot about that part of life."

    Calem "You, uh... You said your GPA was in hell? I'm sure it isn't {i}that{/i} bad!"

    Steven "How many hands do I have?"

    Calem "Huh?"

    Steven "That's my GPA."

    Calem "..."

    Calem "Yikes!"

    Calem "Okay, okay - Maybe you just need some help! Like, I dunno, a tutor! Doesn't your school have those?"

    Steven "Well, yeah, but I have to pay for one to sit with me for more than 30 minutes."

    Calem "Hmm..."

    "Calem silently thinks to himself."

    Calem "Wait, wait! I got it! You don't need to pay for a tutor!"

    Calem "I'll tutor you for free!"

    Calem "See, it's great because I have no need for money, I don't need to sleep, I don't have a life outside of-"

    Steven "No."

    Steven "Subjecting yourself to hours of torture for {i}nothing{/i}? I wouldn't even let you do that if you were alive."

    Calem "Okay, well, my offer isn't {i}entirely{/i} free. To get my services, I want you..."

    Calem "...to go out with me!"

    Steven "..."

    Calem "Wait, wait! Actually, actually, I meant - Take me with you! When you go outside! Please?!"

    Steven "Oh. Why didn't you say so?"
    
    Steven "Sure, then. I can do that. I mean, it's not as if I go anywhere exciting, but..."

    Calem "Dude, are you serious?! Everything's exciting! Do you just sit in your room all day?"

    Steven "I went out to the grocery store last week to buy laundry detergent. And took out the trash. And walked to the dining hall."

    Calem "Awh, jeez, dude. We really need to work on that."

    Steven "What're your ideas, then?"

    Calem "Okay - New condition for my tutoring! You're required to go off campus at least twice a week!"

    Steven "Terrifying."

    Calem "Ahaha! Well, you gotta do it scared! It'll be fun, I promise!"
    
    Calem "Steven, was it? I hereby declare that I, Calem, will help you live life more than ever before!"

    Steven "Well."

    Steven "{i}At least he sounds happy about it.{/i}"

    "{b}PROLOGUE: END{/b}"

    $ cal += day_inc

    "Today is [cal.day_word], [cal.month] [cal.day]."

    menu day_options:
        "{i}How do you want to spend your day?{/i}"

        "I want to study!":
            "{i}You caught up on your lectures, and did some homework! One step closer to passing your exams!{/i}"
            $ intelligence += 1
            "{i}You gained 1 intelligence point!{/i}"
        
        "I want to go out!":
            "This is a placeholder, but assume you went somewhere cool!"

        "I want to rest!":
            "You flopped into your bed, and took a nap! Begone, sleep debt!"
            $ sleep += 1
            "{i}You restored 10 SP!{/i}"

    label after_menu:
        "You had a pretty fulfilling day! Now, it's bedtime!"
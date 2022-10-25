import random 
when = ["Few Days Ago", "Yesterday","A Month Ago",'An year ago']
where = [" at Eden gardens"," at wankhede stadium"," at Narendra Modi Stadium"," at Oval"]
who = ["Virat Kohli","Rohit sharma","Steve Smith","Kl Rahul","David Warner", "Glenn maxwell","AB Devilliers"]
what = [" scored century in 42 Balls"," scored double century"," scored 265 runs in 318 Balls in Test Match"]
print(random.choice(when),random.choice(who) +  random.choice(what) + random.choice(where))
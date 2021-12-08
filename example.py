questions2 = [
    """"What is the capital of Italy,
Rome, 
Paris, 
Tokyio, 
Madrid""",

    """What is the capital of France, 
Paris, 
Rome, 
Tokyio, 
Madrid""",

    """What is the capital of England
London, 
Paris, 
Tokyio, 
Madrid""",
    ]

questions = []
for line in questions2:
    print(line.split("\n"))
    q, a1, a2, a3, a4 = line.split(",")
    questions.append([q, [a1, a2, a3, a4]])

print(questions)
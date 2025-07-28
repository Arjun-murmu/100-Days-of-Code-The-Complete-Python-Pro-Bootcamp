question_data_first = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament,"
             " you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

question_data_med = [
            {
                "type": "multiple",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "Nvidia&#039;s headquarters are based in which Silicon Valley city?",
                "correct_answer": "Santa Clara",
                "incorrect_answers": [
                    "Palo Alto",
                    "Cupertino",
                    "Mountain View"
                ]
            },
            {
                "type": "multiple",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "What does RAID stand for?",
                "correct_answer": "Redundant Array of Independent Disks",
                "incorrect_answers": [
                    "Rapid Access for Indexed Devices",
                    "Range of Applications with Identical Designs",
                    "Randomized Abstract Identification Description"
                ]
            },
            {
                "type": "multiple",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "Which of these people was NOT a founder of Apple Inc?",
                "correct_answer": "Jonathan Ive",
                "incorrect_answers": [
                    "Steve Jobs",
                    "Ronald Wayne",
                    "Steve Wozniak"
                ]
            },
            {
                "type": "multiple",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "Which of these is the name for the failed key escrow device introduced by the National Security Agency in 1993?",
                "correct_answer": "Clipper Chip",
                "incorrect_answers": [
                    "Enigma Machine",
                    "Skipjack",
                    "Nautilus"
                ]
            },
            {
                "type": "multiple",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "How fast is USB 3.1 Gen 2 theoretically?",
                "correct_answer": "10 Gb/s",
                "incorrect_answers": [
                    "5 Gb/s",
                    "8 Gb/s",
                    "1 Gb/s"
                ]
            },
            {
                "type": "boolean",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "Early RAM was directly seated onto the motherboard and could not be easily removed.",
                "correct_answer": "True",
                "incorrect_answers": [
                    "False"
                ]
            },
            {
                "type": "multiple",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "Which one of these is not an official development name for a Ubuntu release?",
                "correct_answer": "Mystic Mansion",
                "incorrect_answers": [
                    "Trusty Tahr",
                    "Utopic Unicorn",
                    "Wily Werewolf"
                ]
            },
            {
                "type": "boolean",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ",
                "correct_answer": "True",
                "incorrect_answers": [
                    "False"
                ]
            },
            {
                "type": "multiple",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "Which internet company began life as an online bookstore called &#039;Cadabra&#039;?",
                "correct_answer": "Amazon",
                "incorrect_answers": [
                    "eBay",
                    "Overstock",
                    "Shopify"
                ]
            },
            {
                "type": "multiple",
                "difficulty": "medium",
                "category": "Science: Computers",
                "question": "What is the name of the default theme that is installed with Windows XP?",
                "correct_answer": "Luna",
                "incorrect_answers": [
                    "Neptune",
                    "Whistler",
                    "Bliss"
                ]
            }
]

question_data = [
         {"type": "boolean",
          "difficulty": "easy",
          "category": "Science: Computers",
          "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
          "correct_answer": "False",
          "incorrect_answers": ["True"]},
         {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
          "question": "The first IBM PC was released in 1981.", "correct_answer": "True",
          "incorrect_answers": ["False"]},
         {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
          "question": "RAM stands for Random Access Memory.", "correct_answer": "True",
          "incorrect_answers": ["False"]},
         {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
          "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
          "correct_answer": "False", "incorrect_answers": ["True"]},
         {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
          "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
          "correct_answer": "False", "incorrect_answers": ["True"]},
         {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
          "question": "Linux was first created as an alternative to Windows XP.",
          "correct_answer": "False", "incorrect_answers": ["True"]},
         {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
          "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
          "correct_answer": "True", "incorrect_answers": ["False"]},
         {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
          "question": "Time on Computers is measured via the EPOX System.",
          "correct_answer": "False", "incorrect_answers": ["True"]},
         {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
          "question": "Ada Lovelace is often considered the first computer programmer.",
          "correct_answer": "True", "incorrect_answers": ["False"]},
         {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
          "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
          "correct_answer": "True", "incorrect_answers": ["False"]}
]

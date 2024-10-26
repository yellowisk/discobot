from random import choice, randint

def get_response(user_input: str):
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered or 'hi' in lowered:
        return 'Hello! How are you?'
    elif 'how are you' in lowered:
        return 'I\'m doing well, thank you for asking!'
    elif 'good' in lowered or 'great' in lowered:
        return 'That\'s great to hear!'
    elif 'bad' in lowered or 'terrible' in lowered:
        return 'I\'m sorry to hear that. Is there anything I can do to help?'
    elif 'help' in lowered:
        return 'I can help you with a variety of things. What do you need help with?'
    elif 'roll dice' in lowered:
        return 'You rolled a ' + str(randint(1, 6)) + '!'
    elif 'flip coin' in lowered:
        return 'You flipped a ' + choice(['heads', 'tails']) + '!'
    elif 'joke' in lowered:
        return choice([
            'Why did the scarecrow win an award? Because he was outstanding in his field!',
            'Why did the tomato turn red? Because it saw the salad dressing!',
            'What do you call a fake noodle? An impasta!',
            'Why did the coffee file a police report? It got mugged!',
            'What do you call a belt made out of watches? A waist of time!'
        ])
    elif 'math' in lowered:
        return str(randint(1, 100)) + ' + ' + str(randint(1, 100)) + ' = ' + str(randint(2, 200))
    else:
        return choice([
            'I\'m sorry, I didn\'t understand that.',
            'Could you please rephrase that?',
            'I\'m not sure what you mean by that.'
        ])
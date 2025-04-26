# prompts.py

def basic_prompt(user_input):
    return f"Translate this sentence into Shakespearean English: {user_input}"

def few_shot_shakespeare_prompt(user_input):
    return f"Translate this sentence into Shakespearean English using these examples:\n" \
           f"Example 1: 'To be, or not to be, that is the question.'\n" \
           f"Example 2: 'Now is the winter of our discontent.'\n" \
           f"Translate: {user_input}"

def lewis_carrol_prompt(user_input):
    return f"Translate this sentence into a whimsical, nonsensical style like the poem 'Jabberwocky' by Lewis Carroll: {user_input}"

def few_shot_lewis_carrol_prompt(user_input):
    return f"Translate this sentence into a whimsical, nonsensical style like the poem 'Jabberwocky' by Lewis Carroll using these examples:\n" \
           f"Example 1: '’Twas brillig, and the slithy toves did gyre and gimble in the wabe.'\n" \
           f"Example 2: 'All mimsy were the borogoves, and the mome raths outgrabe.'\n" \
           f"Translate: {user_input}"

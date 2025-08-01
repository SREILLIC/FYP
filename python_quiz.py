#get random python test
import random
def random_python_test():
    list_tests = [
        {
        "Q":"What is the correct way to iterate through keys in a dictionary?",
        "Option 1":"for i in dict_example:",
        "Option 2":"for f in len(dict_sample):",
        "Option 3":"for j if dictionary:",
        "Option 4":"if dict for loop:"
        },
        {
        "Q":"When using WSL2 CLI: How many spaces does 'tab' make in nano?",
        "Option 1":"2",
        "Option 2":"This isn't Python!",
        "Option 3":"4",
        "Option 4":"Why do they do this?"
        },
        {
        "Q":"Is Boots the best?",
        "Option 1":"Yes",
        "Option 2":"Who is boots?",
        "Option 3":"Fish are friends, not food",
        "Option 4":"BIOS is better"
        }
    ]

    test = random.choice(list_tests)
    return test
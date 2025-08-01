import random

def get_py_rev():
    list_examples = [
        "a=1","b=2","c=3","d=4","e=5","f=6",
        "g=7","h=8","i=9","j=10","k=11","l=12",
        "m=13","n=14","o=15","p=16","q=17","r=18",
        "s=19","t=20","u=21"
    ]

    list_six = []

    for c in range (0, 6):
        rev = random.choice(list_examples)
        list_six.append(rev)

    return list_six
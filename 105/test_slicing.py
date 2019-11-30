from slicing import text, slice_and_dice, slice_and_dice_2

another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""


def test_slice_and_dice_default_text():
    expected = ['objects', 'y', 'too', ':)', 'bites']
    assert slice_and_dice(text) == expected


def test_slice_and_dice_other_text():
    expected = ['word', 'list', 'list']
    assert slice_and_dice(another_text) == expected

def test_slice_and_dice_2_default_text():
    expected = {'you': 7, 'the': 6, 'is': 4, 'can': 4, 'a': 4, 'as': 4, 
    'and': 4, 'python': 3, 'on': 3, 'this': 3, 'pybites': 3, 'one': 2, 
    'feature': 2, 'of': 2, 'about': 2, 'slicing': 2, 'use': 2, 'well': 2, 
    'list': 2, 'gives': 2, 'so': 2, 'here': 2, 'really': 1, 'nice': 1, 
    'polymorphism': 1, 'using': 1, 'same': 1, 'operation': 1, 'different': 1, 
    'types': 1, 'objects': 1, 'lets': 1, 'talk': 1, 'an': 1, 'elegant': 1, 
    'string': 1, 'for': 1, 'example': 1, 'py': 1, 'first': 1, 'value': 1, 
    'inclusive': 1, 'last': 1, 'exclusive': 1, 'we': 1, 'grab': 1, 
    'indexes': 1, 'letter': 1, 'p': 1, 'y': 1, 'when': 1, 'have': 1, 
    'index': 1, 'leave': 1, 'it': 1, 'out': 1, 'write': 1, 'but': 1, 
    'kicker': 1, 'too': 1, 'teaches': 1, 'would': 1, 'now': 1, 'know': 1, 
    'from': 1, 'end': 1, 'keep': 1, 'enjoying': 1, 'our': 1, 'bites': 1}
    assert slice_and_dice_2(text) == expected
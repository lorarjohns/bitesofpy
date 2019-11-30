from vowels import strip_vowels, text

to_replace = 'aeiou'
replace_with = '*'

def test_strip_vowels_on_zen():
    output, number_replacements = strip_vowels(text, to_replace, replace_with)

    assert number_replacements == 262

    assert 'Th* Z*n *f Pyth*n, by T*m P*t*rs' in output
    assert 'B***t*f*l *s b*tt*r th*n *gly' in output
    assert 'N*m*sp*c*s *r* *n* h*nk*ng gr**t *d**' in output
    assert '*lth**gh pr*ct*c*l*ty b**ts p*r*ty.' in output


def test_strip_vowels_on_other_text():
    to_replace = 'aeiou'
    text = """Hello world!
              We hope that you are learning a lot of Python.
              Have fun with our Bites of Py.
              Keep calm and code in Python!
              Become a PyBites ninja!
              All the way"""

    output, number_replacements = strip_vowels(text, to_replace, replace_with)

    assert number_replacements == 46

    assert 'H*ll* w*rld!' in output
    assert 'H*v* f*n w*th **r B*t*s *f Py' in output
    assert 'B*c*m* * PyB*t*s n*nj*!' in output
    assert '*ll th* w*y' in output

def test_strip_vowels_plus_y():    
    text = """Hello world!
              We hope that you are learning a lot of Python.
              Have fun with our Bites of Py.
              Keep calm and code in Python!
              Become a PyBites ninja!
              All the way"""
    to_replace = 'aeiouy'

    output, number_replacements = strip_vowels(text, to_replace, replace_with)

    assert number_replacements == 52
    assert 'W* h*p* th*t *** *r* l**rn*ng * l*t *f P*th*n.' in output
    assert 'H*v* f*n w*th **r B*t*s *f P*' in output
    assert 'K**p c*lm *nd c*d* *n P*th*n' in output
    assert 'B*c*m* * P*B*t*s n*nj*!' in output
    assert '*ll th* w**' in output

def test_strip_vowels_replace_with_bang():
    text = """The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated."""    

    to_replace = 'aeiou'
    replace_with = '!'

    output, number_replacements = strip_vowels(text, to_replace, replace_with)

    assert number_replacements == 45
    assert 'Th! Z!n !f Pyth!n, by T!m P!t!rs' in output
    assert 'B!!!t!f!l !s b!tt!r th!n !gly' in output
    assert '!xpl!c!t !s b!tt!r th!n !mpl!c!t' in output
    assert 'S!mpl! !s b!tt!r th!n c!mpl!x' in output
    assert 'C!mpl!x !s b!tt!r th!n c!mpl!c!t!d' in output

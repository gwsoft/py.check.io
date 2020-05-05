import Home

def test_popular_words1():
    assert Home.popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }

def test_popular_words2():
    assert Home.popular_words("I will go to the cinema\nNo you will not",
        ["i","will","no"]) == {
        "i":1,"will":2,"no":1
    }

def test_popular_words3():
    assert Home.popular_words("""
And the Raven never flitting still is sitting still is sitting
On the pallid bust of Pallas just above my chamber door\nAnd his
eyes have all the seeming of a demon’s that is dreaming\nAnd the\
lamp-light o’er him streaming throws his shadow on the floor\nAnd
my soul from out that shadow that lies floating on the floor\n
Shall be lifted nevermore""", ["raven","still","is","floor","nevermore"]) == {
    "raven":1,"still":2,"is":3,"floor":2,"nevermore":1}
    

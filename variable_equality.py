print('Hello world!')
def add_one(x):
    return x + 1
x = 1
y = 2
print 'x is equal to y: %s % (x == y)'
z = 1
print 'x is equal to z: %s % (x == z)'
names = ['Donald', 'Jake', 'Phil']
words = ['Random', 'Words', 'Dogs']
if names == words:
    print 'Names list is equal to words'
else:
    print "Names list isn't equal to words"
new_names = ['Donald', 'Jake', 'Phil']
print 'New names list is equal to names: %s % (new_names == names)'

class Talker(object):
    def greet(self, name):
        print 'Hello, %s!' % name
    def farewell(self, name):
        print 'Farewell, %s!' % name

dynamic_languages = ['Python', 'Ruby', 'Groovy']
dynamic_languages.append('Lisp')

numbered_words = dict()
numbered_words[2] = 'world'
numbered_words[1] = 'Hello'
numbered_words[3] = '!'

string = ('This is a single long, long string'
          ' written over many lines for convenience'
          ' using implicit concatenation to join each'
          ' piece into a single string without extra'
          ' newlines (unless you add them yourself).')

for x in xrange(1, 4):
    print ('Hello, new Python user!'
           'This is time number %d') % x


l = [x**2 for x in range(4)]
print(l)
# [0, 1, 4, 9]

squares = {x**2 for x in [0,2,4] if x < 4}
print(squares)
# {0, 4}
x = 1
y = 2
print 'x is equal to y: %s' % (x == y)
z = 1
print 'x is equal to z: %s' % (x == z)
names = ['Donald', 'Jake', 'Phil']
words = ['Random', 'Words', 'Dogs']
if names == words:
    print 'Names list is equal to words'
else:
    print "Names list isn't equal to words"
new_names = ['Donald', 'Jake', 'Phil']
print 'New names list is equal to names: %s' % (new_names == names)
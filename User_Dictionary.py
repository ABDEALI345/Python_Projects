import os
dict = {
    'yoddha' : 'warrior',
    'hawai jahaz' : 'aircraft',
    'bandook' : 'gun',
    'hathyar' : 'weapon',
    'barood' : 'gun powder',
    'dhamaka' : 'explosion'
}
print('choose the word from these whose translation you wanna know ',dict.keys())
a = input('enter the word: ')
print('meaning of your word is: ',dict.get())
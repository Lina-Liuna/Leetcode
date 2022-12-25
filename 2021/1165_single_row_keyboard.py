#There is a special keyboard with all keys in a single row.

#You have given a string keyboard of length 26 indicating the layout of the keyboard(indexed from 0 to 25),
#initialy your finger is at index 0.
#To type a character, you have to move your finger to the index of the desired character.
#The time taken to move your finger from index i to index j is |i - j|
#You want to type a string word.
#Write a program to calculate how much time it takes to type it with one finger.

#Input :- Keyboard = "abcdefghijklmnopqrstuvwxyz", Word = "cba"
#Output :- 4

class SingleRowKeyboard:
    keyboard = ""

    def CalcWordTypeTime(self, keyboard, Word):
        index = 0
        SumTime = 0
        for char in Word:
            CharTypeTime = keyboard.index(char)
            SumTime = SumTime + abs(CharTypeTime - index)
            index = CharTypeTime
        print(SumTime)
        return SumTime


myKeyboard = SingleRowKeyboard()

Keyboard = "abcdefghijklmnopqrstuvwxyz"
Word = "cba"
print(myKeyboard.CalcWordTypeTime(Keyboard, Word))

Keyboard = "pqrstuvwxyzabcdefghijklmno"
Word = "hello"
print(myKeyboard.CalcWordTypeTime(Keyboard, Word))

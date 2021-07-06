#Given a string s, remove the vowels 'a', 'e', 'i', 'o', 'u' from it, and return the new string.
#S consists of lowercase english letters only.

#example:
#input: "today is sunday"
#output: "tdy s sndy"

#input: 'aeiou"
#output: ''

class MyStrClass:
    mystr = ""

    def removeVowels(self, strs):
        self.mystr = strs.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
        print(self.mystr)

stringclass = MyStrClass()
stringclass.removeVowels('today is sunday')
stringclass.removeVowels('aeioud')



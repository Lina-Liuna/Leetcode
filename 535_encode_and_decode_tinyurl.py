#Note: This is a companion problem to the System Design problem: Design TinyURL.

#TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and
# it returns a short URL such as http://tinyurl.com/4e9iAk.
# Design a class to encode a URL and decode a tiny URL.

#There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL
# and the tiny URL can be decoded to the original URL

#1.    what's the traffic volume?(length of the shorteded URL?)

#Let's assume we want to serve more than 1000 billion URLS.
#If we can use 62 characters[A-Z, a-z, 0-9] for the short URLs having lenth n, then
#we can have total 62^n URLs.
#So, we should keep our URLs as short as possible given that it should fulfill the requirement.
#To make things easier,
# we can assume the alias is something like http://tinyurl.com/<alias_hash> and
# alias_hash is a fixed length string.
#Therefore, we can first just store <ID, URL>
#When a user inputs a long URL “http://www.google.com”, the system creates
# a random 7-character string like “abcd123” as ID
# and inserts entry <“abcd123”, “http://www.google.com”> into the database.
#In the run time, when someone visits http://tinyurl.com/abcd123,
# we look up by ID “abcd123” and redirect to the corresponding URL “http://www.google.com”.

#random 7-character string may be cause collision.

#One of the most simple but also effective one, is to have a database table set up this way:

#Table Tiny_Url(
#ID : int PRIMARY_KEY AUTO_INC,
#Original_url : varchar,
#Short_url : varchar
#)


class Solutions:
    ID = 0
    ORiginal_urls = []
    Short_urls = "aaaaaaa"

    def __init__(self):
        self.ID = 0

    def encode(self, longUrl, n):
        idmap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        count = 0
        self.ORiginal_urls = longUrl

        while n >= 1:
            self.Short_urls = self.Short_urls.replace(self.Short_urls[count], idmap[n % 62], 1)
            n = n / 62
            count = count + 1
        self.Short_urls = self.Short_urls[::-1]
        print(self.Short_urls)

mySolutions = Solutions()
mySolutions.encode("http://www.google.com", 5)

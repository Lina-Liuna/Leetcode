# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For instance, if s = 'abcde', then it will be 'bcdea' after one shift.

class rotate_string:
    def sub_string_position(self, s1, s2):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i:] in s2:
                print(s1[i:])
                return i
        return i

    def is_rotate_string(self, s1, s2):
        p = self.sub_string_position(s1, s2)
        if p == len(s1):
            return False
        rss1 = s1[0:p]
        rss2 = s1[p:]
        s3 =rss1[::-1] + rss2[::-1]
        print(s3[::-1], s2)
        if s3[::-1] == s2:
            return True
        return False

s = 'abcde'
goal = 'bcdea'
rs = rotate_string()
print(rs.is_rotate_string(s, goal))
#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = "Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentane"  \
"wnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecrea"  \
"tedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranyn"  \
"artionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefieml" \
"doftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplacef" \
"orthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangand" \
"properthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecr" \
"atewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehave" \
"consecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlen" \
"otlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisfo" \
"rusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofough" \
"therehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegrea" \
"ttdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiont" \
"othatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyr" \
"esolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhav" \
"eanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeoplesh" \
"allnotperishfromtheearth"

# s = "I like racecars that go fast"

def check_n_env(s, position, n=1):
    try:
        return s[position - n] == s[position + n]
    except:
        pass
    return False

def check_r(s, position):
    level = 0
    balanced = True
    while balanced:
        balanced = check_n_env(s, position, n=level)
        level += 1
    return (position, level)

def main(s):
    d = [ check_r(s, i) for i, letter in enumerate(s) ]
    d_sorted = sorted(d, key=lambda item: item[1], reverse=True)    
    position, level = d_sorted[0]
    print "Password level 1:", s[position - level + 2:position + level - 1]
        
if __name__ == '__main__':
    main(s)

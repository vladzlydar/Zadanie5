import regex
import re
testString = "1.2e4*2332+232*(52.2e-5^3.2);12345+(4.2+4.2)+5.2+6.2;(1234+456)+6723;1+(2*4)*6-8^7"


a = regex.search(r'''(?<z>(?<w>(([0-9]+)(\.[0-9]+(e[-]?[0-9])?)?|\((?&w)\))|(([0-9]+)(\.[0-9]+(e[-]?[0-9])?)?|\((?&w)\))[-+/\*\^](?&w));(?&z)?)''',testString)
print("Analyzed string is : "+testString)
if a.span()[1]==len(testString):
    print("Full Match!")
    print("Matched string is : "+str(testString[a.span()[0]:a.span()[1]]))
elif 0< a.span()[1]<len(testString):
    print("Partial Match!")
    print("Matched string is : "+str(testString[a.span()[0]:a.span()[1]]))
else:
    print("Doesn't Match!")



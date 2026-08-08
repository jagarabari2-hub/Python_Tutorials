print()
print("|========================================|"
      "| Regular Expression "
      "||========================================|")
print()
import re
patterns = ['Python', 'data', 'returns', 'portfolio', 'Code', 'Apple']
string = "The financial world is a gold mine when it comes to data-driven insights, and fintech companies are increasingly turning to Python for its capacity to handle complex portfolio optimization tasks. In this blog post, we will explore the essential Python tools and libraries for portfolio optimization, walk through the process of calculating fundamental portfolio metrics such as lognormal returns and Sharpe ratios, and outline how an established optimization strategy mean-variance optimization is applied in practice. Well also show how Python newcomers can use AI Assistant to tackle these tasks and how results can be effectively shared with stakeholders through Datalores reporting features."
for pattern in patterns:
    print('Finding "%s" in "%s" ->' % (pattern, string))
    if re.search(pattern, string):
        print("A match is found!")
    else:
        print("No match!")
print()
print("|========================================|"
      "| Applying methods on match objects "
      "||========================================|")
print()
pattern = 'car'
string = 'Formula F1 is a sports car have a increadible speed'
match = re.search(pattern, string)
s = match.start()
print(s)
e = match.end()
print(e)
sp = match.span()
print(sp)
sp1 = match.span()[0]
print(sp1)
sp2 = match.span()[1]
print('The pattern "%s" is found in "%s" from %d to %d ("%s")' % (match.re.pattern, match.string, s, e, string[s:e]))
print("|========================================|"
      "| The match() Function "
      "||========================================|")
print()
pattern = 'code'
string = 'code Compiled be executed'
print('String :', string)
print('Pattern :', pattern)
match = re.match(pattern, string)
print('If any match found? :', match)
pattern2 = 'AI'
string2 = 'Python Called a glue language'
print("String2 :", string2)
print("Pattern2 :", pattern2)
match2 = re.match(pattern2, string2)
print('If any match found? :', match2)
print("|========================================|"
      "| The findall() function "
      "||========================================|")
print()
pattern = 'fabric'
string = 'The space-time fabric'
for match in re.findall(pattern, string):
    print('Found "%s" in "%s"' % (pattern, string))
if re.search(pattern,  string):
    print('A match is found!')
else:
    print('No match!')
print("|========================================|"
      "| Using the split() function "
      "||========================================|")
print()
lines = ["FName: Jaga, LName: Rabari, Job: Web Developer", "FName: Akshay, LName: Karangiya, Job: Splicer"]
for line in lines:
    print(re.split(",* *\w*: ", line)) 
print("|========================================|"
      "| Using the sub() function "
      "||========================================|")
print()
string = 'My favourite animal is cat. A cat is a very cute animal.'
out = re.sub("cat", "Owl", string)
print(out) 
s=input()
p=print
if s.isnumeric():p("integer")
elif s.count(".")==1 and s.replace(".","").isnumeric():p("float")
else:p("string")

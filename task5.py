escaped = True
if  escaped:
    outcome = "Legend: Everyone knows you escaped."
    good = r"""
              ,
       __-'==
  _--''__---/\_
  7         ,-.';
 (        ,- ",/
 (-,  _--" ,-'
 \  \`; / /,_-
  \\  : \__-=-
   \;-"-.
    | \ 
"""
    print(outcome)
    print(good)

else:
    outcome = "Doom: You are stuck there forever."
    bad = r"""
               __/)
            .-(__(=:
            |    \)
ejm97 (\__  |
     :=)__)-|  __/)
      (/    |-(__(=:
    ______  |  _ \)
   /      \ | / \
        ___\|/___\
       [         ]\
        \       /  \
         \     /
          \___/
"""

    print(outcome)
    print(bad)
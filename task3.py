guard_awake = False
if not guard_awake:
    outcome = "Shadow: You pass the sleeping guard"
    good = r"""
                .==-.                   .-==.
                 \()8`-._  `.   .'  _.-'8()/
                 (88"   ::.  \./  .::   "88)
                  \_.'`-::::.(#).::::-'`._/
                    `._... .q(_)p. ..._.'
                      ""-..-'|=|`-..-""
                      . ""' .'|=|`. `"".
                    ,':8(o)./|=|\.(o)8:`.
                   (O :8 ::/ \_/ \:: 8: O)
                    \O `::/       \::' O/
                     ""--'           `--""   
"""
    print(outcome)
    print(good)

else:
    outcome = "Doom: The guard is walking around."
    bad = r"""
          __  _
       .-.'  `; `-._  __  _
      (_,         .-:'  `; `-._
    ,'o"(        (_,           )
   (__,-'      ,'o"(            )>
      (       (__,-'            )
       `-'._.--._(             )
          |||  |||`-'._.--._.-'
                     |||  |||
"""

    print(outcome)
    print(bad)
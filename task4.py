drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: The bridge starts to raise up."
    good = r"""
 _,-=._                     /|_/|
  `-.}   `=._,.-=-._.,  @ @._,
          `._ _,-.   )      _,.-'
        `    G.m-"^m`m'        
"""
    print(outcome)
    print(good)

else:
    outcome = "Doom: The bridge stays still. "
    bad = r"""
                            _.----.
    .----------------" /  /  \
   (     EVEREADY   | |   |) |
    `----------------._\  \  /
                            "----'
"""

    print(outcome)
    print(bad)
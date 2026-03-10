has_key = True
if has_key:
    outcome = "Click: The key opens the door."
    good = r"""
                                ___,
                    o___.-' /
                    |      _\_
                    |___.-'   `
                    |
                    |
            _   _   j   _   _
           [_]_[_]_[_]_[_]_[_]
           [__j__j__j__j__j__]
             [_j__j__j__j__]
             [__j__j__j__j_]
             [_j__j/V\_j__j]
             [__j_// \\__j_]
             [_j__|   |_j__]
             [__j_|___|__j_]
             [_j__j__j__j__]
             [__j__j__j__j_]
  _   _   _  [_j__j__j__j__]  _   _   _   _
_[_]_[_]_[_]_[__j__j__j__j_]_[_]_[_]_[_]_[_]_
  _j__j__j__j[_j__j__j__j__]j__j__j__j__j_
     j  j  j [  j  j  j  j ] j  j  j  j    hjw

"""
    print(outcome)
    print(good)

else:
    outcome = "Doom: You are stuck here forever."
    bad = r"""
                ,
        .--'|}
       /    /}}
     .=\.--'`\}
    //` '---./`
    ||  /|
     \\| |
   |\_\\/
   \__/\\
        \\
  jgs    \|
    """

    print(outcome)
    print(bad)
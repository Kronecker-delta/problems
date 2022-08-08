def backspaceCompare(s,t):
    s_len , t_len = len(s), len(t)
    spoint, tpoint= s_len-1,t_len-1
    sskip , tskip = 0,0

    while spoint > -1 or tpoint > -1:
        while s[spoint] == "#" or sskip > 0:
            if s[spoint] == "#":
                sskip += 1
            
            elif sskip > 0:
                sskip -= 1
            
            spoint -= 1
        
        while t[tpoint] == "#" or tskip > 0:
            if t[tpoint] == "#":
                tskip += 1
            
            elif tskip > 0:
                tskip -= 1

            tpoint -= 1

        if s[spoint] != t[tpoint]:
            return False

        spoint -= 1
        tpoint -= 1

    return True

print(backspaceCompare("ac#d#","ad#d"))
class computeEv():
    def computeEV (base, iv, ev, level, mod, stats):
        D=(((2*base)+iv+(ev/4)) * ( level/100))
        statMods = stats/mod
        return (((((statMods - D) * 400 )) / level) / 4 ) * 4
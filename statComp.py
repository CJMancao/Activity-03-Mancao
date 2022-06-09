class computeStats ():
    def health (base, ev, level, iv):
        return ((((2*base+iv+(ev/4))*level)/100))+level+10
        
    def otherStat(base, iv, ev, level, nat):
        return ((((((2 * base) + iv + (ev /4) ) * level)) / 100 ) + 5 ) * nat
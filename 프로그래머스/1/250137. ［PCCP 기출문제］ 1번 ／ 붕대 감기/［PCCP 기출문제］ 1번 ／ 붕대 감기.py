def solution(bandage, health, attacks):
    answer = 0
    time = 0
    continuity = 0
    max_health = health
    
    while health > 0 :
        if len(attacks) == 0 :
            return -1 if health < 1 else health
        
        time += 1
        # 공격 시간이 되면 체력 깎고 pass
        if attacks[0][0] == time :
            health -= attacks[0][1]
            continuity = 0
            if len(attacks) > 1 :
                attacks = attacks[1:]
            elif len(attacks) == 1 :
                return -1 if health < 1 else health
            continue
        
        # 공격이 아니라면 회복
        if continuity == bandage[0]-1 :
            health += bandage[1] + bandage[2]
            continuity = 0
        else :
            health += bandage[1]
            continuity += 1
            
        if health > max_health :
            health = max_health
        
    return -1
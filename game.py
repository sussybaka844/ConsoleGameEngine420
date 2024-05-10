from _2D import _2DMap
                
def game():
    CPosition = [1,1]
    
    Map = _2DMap((10,10), '⬜')
    
    print('---- CONTROLS ----')
    print('W\tgo up')
    print('A\tgo left')
    print('S\tgo down')
    print('D\tgo right')
    print('Press enter to start')
    input()
    
    while True:
        kb1 = Map.draw((1,5), (9,1), '🟥')
        
        character = Map.draw(CPosition, (1,1), '⬛')
        
        if Map.check_collisions(CPosition, Object=kb1):
            print('game over')
            return
        
        print('\n'*10+Map.MapStr)
        
        Map.erase(CPosition, (1,1))
        
        Direction = input().upper()
        match Direction:
            case 'W':
                CPosition[1] -= 1
            case 'A':
                CPosition[0] -= 1
            case 'S':
                CPosition[1] += 1
            case 'D':
                CPosition[0] += 1
                
game()
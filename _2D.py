class _2DMap:
    
    def __init__(self, MapSize, DefaultPixel):
        self.MSize = MapSize
        self.MapArray = []
        self.MapStr = ''
        self.DefaultPixel = DefaultPixel
        
        for GenerationPositionY in range(MapSize[1]):
            self.MapArray.append([])
            for GenerationPositionX in range(MapSize[0]):
                self.MapArray[GenerationPositionY].append(DefaultPixel)
                
    def draw_raw(self, Position, Pixel):
        try:
            self.MapArray[Position[1]-1][Position[0]-1] = Pixel
            self.MapStr = ''
            
            for Y in self.MapArray:
                for X in Y:
                    self.MapStr += X
                self.MapStr += '\n'
        except:
            return
        
    def draw(self, Position, Dimensions, Pixel):
        x_start = Position[0]
        y_start = Position[1]
        
        y = y_start
        while y < y_start+Dimensions[1]:
            x = x_start
            while x < x_start+Dimensions[0]:
                self.draw_raw((x, y), Pixel)
                x += 1
            y += 1
            
        return (Position, Dimensions)
        
    def erase_raw(self, Position):
        try:
            self.MapArray[Position[1]-1][Position[0]-1] = self.DefaultPixel
            self.MapStr = ''
            
            for Y in self.MapArray:
                for X in Y:
                    self.MapStr += X
                self.MapStr += '\n'
        except:
            return
        
    def erase(self, Position, Dimensions):
        x_start = Position[0]
        y_start = Position[1]
        
        y = y_start
        while y < y_start+Dimensions[1]:
            x = x_start
            while x < x_start+Dimensions[0]:
                self.draw_raw((x, y), self.DefaultPixel)
                x += 1
            y += 1
            
    def check_collisions(self, CPosition, Position=None, Dimensions=None, Object=None):
        if not Position and not Dimensions:
            Position = Object[0]
            Dimensions = Object[1]
        
        x_start = Position[0]
        y_start = Position[1]
        
        y = y_start
        while y < y_start+Dimensions[1]:
            x = x_start
            while x < x_start+Dimensions[0]:
                if [x,y] == CPosition:
                    return True
                x += 1
            y += 1
        return False
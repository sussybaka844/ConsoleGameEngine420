2d game engine or soemthing idk

_2DMap(MapSize, DefaultPixel)
	creates the map

Map.draw_raw(Position, Pixel)
	draws a single pixel

Map.draw(Position, Dimensions, Pixel)
	draws an object with dimensions

Map.erase_raw(Position)
	erases a single pixel

Map.erase(Position, Dimensions)
	erases an area

Map.check_collisions(CPosition, Position=None, Dimensions=None, Object=None)
	checks collisions between an area and a pixel or an object and a pixel

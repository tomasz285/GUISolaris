import svgwrite
import os
class DrawSVG(object):
   
    def __init__(self, filename, sizex = 250, sizey = 250):
        self.svg_document = svgwrite.Drawing(filename, size = ("%spx" % sizex, "%spx" % sizey))
        
    def drawRect(self,x = 0,y = 0, w = 200, h = 100, colorfill="white" ,colorline="black" ): #r = 255, g = 255, b = 0
        self.svg_document.add(self.svg_document.rect(insert = (x, y),
                                   size = ("%spx" % w, "%spx" % h),
                                   stroke_width = "3",
                                   stroke = colorline,
                                   fill =colorfill   ))   #"rgb(%s,%s,%s)" % (r,g,b)  
    def drawRectrgb(self,  x,y, w, h, rfill, gfill, bfill, rline, gline, bline): 
        self.svg_document.add(self.svg_document.rect(insert = (x, y),
                                   size = ("%spx" % w, "%spx" % h),
                                   stroke_width = "3",
                                   stroke = "rgb(%s,%s,%s)" % (rline, gline, bline),
                                   fill ="rgb(%s,%s,%s)" % (rfill, gfill, bfill)   ))   #"rgb(%s,%s,%s)" % (r,g,b)  
    def drawLine(self, sx, sy , ex , ey, lineColor = "black"):
        self.svg_document.add(self.svg_document.line(start = (sx, sy), 
                                                    end = (ex, ey), 
                                                    stroke_width = "3", 
                                                    stroke = lineColor))
    def drawLinergb(self, sx, sy , ex , ey, rline, gline, bline):
        self.svg_document.add(self.svg_document.line(start = (sx, sy), 
                                                    end = (ex, ey), 
                                                    stroke_width = "3", 
                                                    stroke = "rgb(%s,%s,%s)" % (rline, gline, bline)))
        
    def drawCircle(self, cx, cy, r , colorfill="white", lineColor = "black"):
        self.svg_document.add(self.svg_document.circle(center=(cx, cy), 
                                                       r = r, 
		                                               stroke_width = "3", 
                                                       stroke = lineColor, 
                                                       fill = colorfill))   #"rgb(%s,%s,%s)" % (r,cx,cy)
    def drawCirclergb(self, cx, cy, r , rfill, gfill, bfill, rline, gline, bline):
        self.svg_document.add(self.svg_document.circle(center=(cx, cy), 
                                                       r = r, 
                                                       stroke_width = "3", 
                                                       stroke = "rgb(%s,%s,%s)" % (rline, gline, bline), 
                                                       fill = "rgb(%s,%s,%s)" % (rfill, gfill, bfill)))
              
    def drawEllipse(self, cx, cy , rx, ry , colorfill="white", lineColor = "black"):
        self.svg_document.add(self.svg_document.ellipse(center=(cx, cy), 
                                                        r=(rx, ry), 
                                                        stroke_width = "3", 
                                                        stroke = lineColor,
                                                        fill=colorfill))
        
    def drawEllipsergb(self, cx, cy , rx, ry , rfill, gfill, bfill, rline, gline, bline):
        self.svg_document.add(self.svg_document.ellipse(center=(cx, cy), 
                                                        r=(rx, ry), 
                                                        stroke_width = "3", 
                                                        stroke = "rgb(%s,%s,%s)" % (rline, gline, bline),
                                                        fill="rgb(%s,%s,%s)" % (rfill, gfill, bfill)))
    """    
    def saveDrawing(self):
        self.svg_document.save()
    """    
    def saveDrawing(self):
        if os.path.isfile(self.svg_document.filename):
            self.svg_document.save()
        else:
            self.svg_document.saveas('resources/' + self.svg_document.filename)


    def showDrawing(self):
        print(self.svg_document.tostring())
        

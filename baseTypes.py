import time
from getDrawlib import getDrawlib
drawlib = getDrawlib()

class renObject():
    def __init__(self,renderObj,color=None,palette=drawlib.stdpalette,autoTexture=False,asTexture=True):
        self.pos = (None,None)
        self.renderObj = renderObj
        self.color = {"color":color,"palette":palette}
        self.texture = None
        self.splitPixelGroup = None
        self.asTexture = asTexture
        if autoTexture == True:
            self.texturize()
    def texturize(self):
        if self.asTexture == True:
            try:
                x,y,self.texture = self.renderObj.asTexture()
            except:
                self.texture = self.renderObj.asTexture()
                x = self.renderObj.xPos
                y = self.renderObj.yPos
            self.pos = (x,y)
            if type(self.texture) == list:
                self.texture = drawlib.coreTypes._join_with_delimiter(self.texture,"\n")
        else:
            self.splitPixelGroup = self.renderObj.asSplitPixelGroup()
    def untexturize(self):
        self.texture = None
        self.splitPixelGroup = None
    def _chgPos(self):
        topLeft = drawlib.tools.getTopLeft(self.splitPixelGroup["po"])
        diffs = drawlib.tools.coordinateDifference(self.pos,topLeft)
        self.splitPixelGroup["po"] = drawlib.tools.addDiffToCoords(self.splitPixelGroup["po"],diffs[0],diffs[1])
    def setPos(self,nPos=tuple):
        self.pos = (nPos[0],nPos[1])
        if self.asTexture == False: self._chgPos()
    def addAmnt(self,addX,addY):
        if self.asTexture == True:
            self.pos = (self.pos[0]+addX,self.pos[1]+addY)
        else:
            topLeft = drawlib.tools.getTopLeft(self.splitPixelGroup["po"])
            newPos = (topLeft[0],+addX,topLeft[1]+addY)
            diffs = drawlib.tools.coordinateDifference(newPos,topLeft)
            self.splitPixelGroup["po"] = drawlib.tools.addDiffToCoords(self.splitPixelGroup["po"],diffs[0],diffs[1])
    def stretchShape2X(self,axis="x",lp=True):
        if self.asTexture == True:
            if self.texture == None: self.texturize()
            texture = drawlib.coreTypes._split_with_delimiter(self.texture,"\n")
            texture = drawlib.manip.stretchShape(texture,axis=axis,lp=lp)
            self.texture = drawlib.coreTypes._join_with_delimiter(texture,"\n")
        else:
            if self.splitPixelGroup == None: self.texturize()
            cmpxPixelGroup = drawlib.coreTypes.splitPixelGroup_to_cmpxPixelGroup(self.splitPixelGroup)
            sprite = drawlib.coreTypes.cmpxPixelGroup_to_sprite(cmpxPixelGroup)
            x,y,texture = drawlib.coreTypes.sprite_to_texture(sprite)
            texture = drawlib.coreTypes._split_with_delimiter(texture,"\n")
            texture = drawlib.manip.stretchShape(texture,axis=axis,lp=lp)
            texture = drawlib.coreTypes._join_with_delimiter(texture,"\n")
            sprite2 = drawlib.coreTypes.texture_to_sprite(texture,x,y)
            cmpxPixelGroup2 = drawlib.coreTypes.sprite_to_cmpxPixelGroup(sprite2,exclusionChar=" ")
            self.splitPixelGroup = drawlib.coreTypes.cmpxPixelGroup_to_splitPixelGroup(cmpxPixelGroup2)
    def fillShape(self,fillChar=str):
        if self.asTexture == True:
            if self.texture == None: self.texturize()
            texture = drawlib.coreTypes._split_with_delimiter(self.texture,"\n")
            texture = drawlib.manip.fillShape(texture,fillChar=fillChar)
            self.texture = drawlib.coreTypes._join_with_delimiter(texture,"\n")
        else:
            if self.splitPixelGroup == None: self.texturize()
            cmpxPixelGroup = drawlib.coreTypes.splitPixelGroup_to_cmpxPixelGroup(self.splitPixelGroup)
            sprite = drawlib.coreTypes.cmpxPixelGroup_to_sprite(cmpxPixelGroup)
            x,y,texture = drawlib.coreTypes.sprite_to_texture(sprite)
            texture = drawlib.coreTypes._split_with_delimiter(texture,"\n")
            texture = drawlib.manip.fillShape(texture,fillChar=fillChar)
            texture = drawlib.coreTypes._join_with_delimiter(texture,"\n")
            sprite2 = drawlib.coreTypes.texture_to_sprite(texture,x,y)
            cmpxPixelGroup2 = drawlib.coreTypes.sprite_to_cmpxPixelGroup(sprite2,exclusionChar=" ")
            self.splitPixelGroup = drawlib.coreTypes.cmpxPixelGroup_to_splitPixelGroup(cmpxPixelGroup2)
    def rotateShape(self,degrees,fixTopLeft=False):
        if self.asTexture == True:
            if self.texture == None: self.texturize()
            sprite = drawlib.coreTypes.texture_to_sprite(self.texture)
            cmpxPixelGroup = drawlib.coreTypes.sprite_to_cmpxPixelGroup(sprite," ")
            splitPixelGroup = drawlib.coreTypes.cmpxPixelGroup_to_splitPixelGroup(cmpxPixelGroup)
            splitPixelGroup = drawlib.manip.rotateSplitPixelGroup(splitPixelGroup, degrees, fixTopLeft)
            cmpxPixelGroup = drawlib.coreTypes.splitPixelGroup_to_cmpxPixelGroup(splitPixelGroup)
            sprite = drawlib.coreTypes.cmpxPixelGroup_to_sprite(cmpxPixelGroup)
            x,y,self.texture = drawlib.coreTypes.sprite_to_texture(sprite)
        else:
            if self.splitPixelGroup == None: self.texturize()
            self.splitPixelGroup = drawlib.manip.rotateSplitPixelGroup(self.splitPixelGroup, degrees, fixTopLeft)
    def fillBoundaryGap(self):
        if self.asTexture == True:
            if self.texture == None: self.texturize()
            sprite = drawlib.coreTypes.texture_to_sprite(self.texture)
            cmpxPixelGroup = drawlib.coreTypes.sprite_to_cmpxPixelGroup(sprite," ")
            splitPixelGroup = drawlib.coreTypes.cmpxPixelGroup_to_splitPixelGroup(cmpxPixelGroup)
            splitPixelGroup = drawlib.manip.fillBoundaryGap(splitPixelGroup)
            cmpxPixelGroup = drawlib.coreTypes.splitPixelGroup_to_cmpxPixelGroup(splitPixelGroup)
            sprite = drawlib.coreTypes.cmpxPixelGroup_to_sprite(cmpxPixelGroup)
            x,y,self.texture = drawlib.coreTypes.sprite_to_texture(sprite)
        else:
            if self.splitPixelGroup == None: self.texturize()
            self.splitPixelGroup = drawlib.manip.fillBoundaryGap(self.splitPixelGroup)
    def getTopLeft(self):
        if self.asTexture == True:
            if self.texture == None: self.texturize()
            sprite = drawlib.coreTypes.texture_to_sprite(self.texture,self.pos[0],self.pos[1])
            char,pixels = drawlib.coreTypes.sprite_to_pixelGroup(sprite, char="#", exclusionChar=" ")
            return drawlib.tools.getTopLeft(pixels)
        else:
            if self.splitPixelGroup == None: self.texturize()
            return drawlib.tools.getTopLeft(self.splitPixelGroup["po"])
    def draw(self):
        if self.asTexture == True:
            if self.texture == None: self.texturize()
            _ansi = drawlib.coloring.autoNoneColor(self.color["color"],self.color["palette"])
            drawlib.coreTypes.render_texture(self.pos[0],self.pos[1],self.texture,_ansi)
        else:
            if self.splitPixelGroup == None: self.texturize()
            _ansi = drawlib.coloring.autoNoneColor(self.color["color"],self.color["palette"])
            drawlib.coreTypes.render_splitPixelGroup(self.splitPixelGroup,_ansi)

class window():
    def __init__(self,drawOnUpdate=True,generateOnCreation=False,drawOnCreation=False):
        self.objects = {}
        self.drawlib = drawlib
        self.drawOnUpdate = drawOnUpdate
        self.generateOnCreation = generateOnCreation
        self.drawOnCreation = drawOnCreation
        self.drawnObjects = []
    def resetHead(self,x=0,y=0):
        drawlib.linedraw.reset_write_head(x,y)
    def reset(self,clear=True):
        self.objects = {}
        self.drawnObjects = []
        if clear == True:
            self.clear()
    def _add(self, object=object, id=None) -> str:
        if id == None:
            i = str(len(self.objects.keys()))
            while str(id) in self.objects.keys():
                i += 1
                id = str(i)
            id = str(i)
        else:
            if type(id) != str:
                raise TypeError("Id must be of type string!")
        self.objects[id] = object
        return id
    def _rem(self, id):
        if self.objects.get(id) == None:
            raise Exception(f"Id '{id}' does not exist!")
        else:
            self.objects.pop(id)
    def _get(self,id):
        if self.objects.get(id) == None:
            raise Exception(f"Id '{id}' does not exist!")
        else:
            return self.objects[id]
    def _move(self,id,addX,addY):
        obj = self._get(id)
        obj.addAmnt(addX,addY)
    def _moveto(self,id,nPos=tuple):
        obj = self._get(id)
        obj.setPos(nPos)
    def _draw(self):
        for _,obj in self.objects.items():
            if obj not in self.drawnObjects:
                obj.draw()
                self.drawnObjects.append(obj)
    def _redraw(self):
        for _,obj in self.objects.items():
            if obj not in self.drawnObjects:
                self.drawnObjects.append(obj)
            obj.draw()
    def markDrawn(self,obj):
        if obj not in self.drawnObjects:
            self.drawnObjects.append(obj)
    def unmarkDrawn(self,obj):
        if obj in self.drawnObjects:
            self.drawnObjects.pop(obj)
    def sleep(self,int):
        time.sleep(int)
    def draw(self):
        self._draw()
    def drawC(self):
        self.clear()
        self._draw()
    def redraw(self):
        self._redraw()
    def redrawC(self):
        self.clear()
        self._redraw()
    def clear(self):
        self.drawlib.fill_terminal(" ")
    def fill(self,char=str):
        self.drawlib.fill_terminal(char)

    def moveto(self,id,nPos=tuple):
        self._moveto(id,nPos)
        if self.drawOnUpdate == True:
            self.redraw()
    def move(self,id,addX,addY):
        self._move(id,addX,addY)
        if self.drawOnUpdate == True:
            self.redraw()

    def stretchShape2X(self,id,axis="x",lp=True):
        obj = self._get(id)
        obj.stretchShape2X(axis,lp)

    def fillShape(self,id,fillChar=str):
        obj = self._get(id)
        obj.fillShape(fillChar)

    def rotateShape(self,id,degrees=int,fixTopLeft=False):
        obj = self._get(id)
        obj.rotateShape(degrees,fixTopLeft)

    def fillBoundaryGap(self,id):
        obj = self._get(id)
        obj.fillBoundaryGap()

    def getTopLeft(self,id):
        obj = self._get(id)
        return obj.getTopLeft()

    def create_drawlibObj(self,classObj,color=None,palette=drawlib.stdpalette,asTexture=False,*args,**kwargs):
        addargs = {}
        if self.generateOnCreation == True:
            addargs["autoGenerate"] = True
        if self.drawOnCreation == True:
            addargs["autoDraw"] = True
        kwargs.update(addargs)
        sobj = classObj(*args,**kwargs)
        obj = renObject(sobj,color,palette,asTexture=asTexture)
        return self._add(obj)

    def create_point(self,charset,p1=tuple,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.pointObj
        return self.create_drawlibObj(classObj,color=color,palette=palette,charset=charset,x1=p1[0],y1=p1[1],autoGenerate=autoGenerate)
    
    def create_line(self,charset,p1=tuple,p2=tuple,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.lineObj
        return self.create_drawlibObj(classObj,color=color,palette=palette,charset=charset,x1=p1[0],y1=p1[1],x2=p2[0],y2=p2[1],autoGenerate=autoGenerate)
    
    def create_triangle(self,charset,p1=tuple,p2=tuple,p3=tuple,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.triangleObj
        return self.create_drawlibObj(classObj,color=color,palette=palette,charset=charset,x1=p1[0],y1=p1[1],x2=p2[0],y2=p2[1],x3=p3[0],y3=p3[1],autoGenerate=autoGenerate)
    
    def create_rectangle(self,charset,p1=tuple,p2=tuple,p3=tuple,p4=tuple,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.rectangleObj
        return self.create_drawlibObj(classObj,color=color,palette=palette,charset=charset,x1=p1[0],y1=p1[1],x2=p2[0],y2=p2[1],x3=p3[0],y3=p3[1],x4=p4[0],y4=p4[1],autoGenerate=autoGenerate)

    def create_rectangle2(self,charset,p1=tuple,p2=tuple,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.rectangleObj2
        return self.create_drawlibObj(classObj,color=color,palette=palette,charset=charset,c1=p1,c2=p2,autoGenerate=autoGenerate)

    def create_circle(self,charset,p1=tuple,radius=int,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.circleObj
        return self.create_drawlibObj(classObj,color=color,palette=palette,charset=charset,xM=p1[0],yM=p1[1],r=radius,autoGenerate=autoGenerate)
    
    def create_ellipse(self,charset,p1=tuple,radius1=int,radius2=int,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.ellipseObj
        return self.create_drawlibObj(classObj,color=color,palette=palette,charset=charset,cX=p1[0],cY=p1[1],xRad=radius1,yRad=radius2,autoGenerate=autoGenerate)
    
    def create_quadBezier(self,charset,sp=tuple,cp=tuple,ep=tuple,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.quadBezierObj
        return self.create_drawlibObj(classObj,color=color,palette=palette,charset=charset,sX=sp[0],sY=sp[1],cX=cp[0],cY=cp[1],eX=ep[0],eY=ep[1],autoGenerate=autoGenerate)

    def create_cubicBezier(self,charset,sp=tuple,c1=tuple,c2=tuple,ep=tuple,algorithm="step",modifier=None,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.cubicBezierObj
        return self.create_drawlibObj(classObj,color=color,palette=palette,charset=charset,sX=sp[0],sY=sp[1],c1X=c1[0],c1Y=c1[1],c2X=c2[0],c2Y=c2[1],eX=ep[0],eY=ep[1],algorithm=algorithm,modifier=modifier,autoGenerate=autoGenerate)
    
    def create_assetFile(self,filepath=str,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.assetFileObj
        return self.create_drawlibObj(classObj,color=color,palette=palette,filepath=filepath,autoGenerate=autoGenerate)
    
    def create_assetTexture(self,p1=tuple,filepath=str,color=None,palette=drawlib.stdpalette,autoGenerate=False):
        classObj = self.drawlib.objects.assetTexture
        return self.create_drawlibObj(classObj,color=color,palette=palette,filepath=filepath,posov=p1,autoGenerate=autoGenerate)
    
    def create_boxImage(self, p1=tuple,imagePath=str,charset=None, mode="foreground",monochrome=False,width=None,height=None,resampling="lanczos",method=None,strTxtMethod=False, color=None,palette=drawlib.stdpalette,exNonTexture=False):
        classObj = self.drawlib.imaging.boxImage
        if exNonTexture == True: asT = False
        else: asT = True
        return self.create_drawlibObj(classObj,color=color,palette=palette,asTexture=asT, imagePath=imagePath,mode=mode,char=charset,monochrome=monochrome,width=width,height=height,resampling=resampling,method=method,strTxtMethod=strTxtMethod,xPos=p1[0],yPos=p1[1])

    def create_asciiImage(self, p1=tuple,imagePath=str,charset=None, mode="standard",pc=False,method="lum",invert=False,monochrome=False,width=None,height=None,resampling="lanczos",strTxtMethod=False, color=None,palette=drawlib.stdpalette,exNonTexture=False):
        classObj = self.drawlib.imaging.asciiImage
        if exNonTexture == True: asT = False
        else: asT = Tru
        return self.create_drawlibObj(classObj,color=color,palette=palette,asTexture=asT, imagePath=imagePath,mode=mode,pc=pc,method=method,invert=invert,monochrome=monochrome,width=width,height=height,resampling=resampling,strTxtMethod=strTxtMethod,char=charset,xPos=p1[0],yPos=p1[1])
        
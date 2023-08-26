from getDrawlib import getDrawlib
drawlib = getDrawlib()

class renObject():
    def __init__(self,renderObj,sPos=tuple,color=None,palette=drawlib.stdpalette,autoTexture=True):
        self.pos = (None,None)
        if sPos != None: self.pos = (sPos[0],sPos[1])
        self.renderObj = renderObj
        self.color = {"color":color,"palette":palette}
        self.texture = None
        if autoTexture == True:
            self.texturize()
    def texturize(self):
        self.texture = self.renderObj.asTexture()
    def untexturize(self):
        self.texture = None
    def setPos(self,nPos=tuple):
        self.pos = (nPos[0],nPos[1])
    def draw(self):
        if self.texture == None: self.texturize()
        _ansi = drawlib.coloring.autoNoneColor(self.color["color"],self.color["palette"])
        drawlib.coreTypes.render_texture(self.pos[0],self.pos[1],self.texture,_ansi)

class window():
    def __init__(self,drawOnUpdate=True,generateOnCreation=False,drawOnCreation=False):
        self.objects = {}
        self.drawlib = drawlib
        self.drawOnUpdate = drawOnUpdate
        self.generateOnCreation = generateOnCreation
        self.drawOnCreation = drawOnCreation
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
    def _move(self,id,nPos=tuple):
        obj = self._get(id)
        obj.setPos(nPos)
    def _draw(self):
        for _,obj in self.objects.items():
            obj.draw()
    def draw(self):
        self.clear()
        self._draw()
    def drawNC(self):
        self._draw()
    def clear(self):
        self.drawlib.fill_terminal(" ")
    def fill(self,char=str):
        self.drawlib.fill_terminal(char)
    def redraw(self):
        self.clear()
        self.draw()

    def move(self,id,nPos=tuple):
        self._move(id,nPos)
        if self.drawOnUpdate == True:
            self.redraw()

    def create_drawlibObj(self,classObj,sPos=tuple,color=None,palette=drawlib.stdpalette,*args,**kwargs):
        addargs = {}
        if self.generateOnCreation == True:
            addargs["autoGenerate"] = True
        if self.drawOnCreation == True:
            addargs["autoDraw"] = True
        kwargs.update(addargs)
        sobj = classObj(*args,**kwargs)
        obj = renObject(sobj,sPos,color,palette)
        return self._add(obj)

    def create_point(self,char,sPos=tuple,color=None,palette=drawlib.stdpalette):
        classObj = self.drawlib.objects.pointObj
        return self.create_drawlibObj(classObj,sPos=sPos,color=color,palette=palette,char=char,x1=0,y1=0)
    #def create_line(self,char,sPos=tuple,point2=tuple,color=None,palette=drawlib.stdpalette):
    #    classObj = self.drawlib.objects.lineObj
    #    return self.create_drawlibObj(classObj,sPos=sPos,color=color,palette=palette,char=char,x1=0,y1=0)
    def create_circle(self,char,sPos=tuple,radius=int,color=None,palette=drawlib.stdpalette):
        classObj = self.drawlib.objects.circleObj
        return self.create_drawlibObj(classObj,sPos=sPos,color=color,palette=palette,char=char,xM=0,yM=0,r=radius)
    
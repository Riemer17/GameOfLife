class GOL:
    def __init__(self):
        self.nrows = width/10
        self.ncols = height/10
        self.w = width/self.ncols
    def makeboard(self):
        grid = []
        for i in range(self.nrows):
            grid.append([])
            for j in range(self.ncols):
                grid[i].append(0)
        return grid
    def color_cell(self,mousex,mousey,board):
        try:
            board[mousey/10][mousex/10] = 1
        except:
            pass
        return board
    def creategen0(self,board):
        for i in range(self.nrows):
            for j in range(self.ncols):
                board[i][j] = int(random(0,2))
        return board
    def display(self,grid):
        for x in range(self.ncols):
            for y in range(self.nrows):
                if grid[y][x] == 0:
                    fill(255)
                else:
                    fill(0)
                rect(x*self.w,y*self.w,self.w,self.w)
    def newstate(self,neighbors,state):
    
        if neighbors <2 and state == 1:
            return 0
        elif neighbors >3 and state == 1:
            return 0
        elif neighbors == 3 and state == 0:
            return 1
        else:
            return state
    def newgen(self,prevgen):
        nextgen = self.makeboard()
        for i in range(self.ncols):
            for j in range(self.nrows):
                neighbors = 0
                try:
                    for x in range(i-1,i+2):
                        for y in range(j-1,j+2):
                            neighbors += prevgen[y][x]
                    neighbors-= prevgen[j][i]
                    nextgen[j][i] = self.newstate(neighbors, prevgen[j][i])
                except:
                    nextgen[j][i] = 0
        return nextgen 
                
                    
def setup():
    stroke(150)
    size(800,800)
    gol = GOL()
    frameRate(10)
    grid = gol.makeboard()
    gol.display(grid)
    run = False
    global gol,grid,run

def draw():
    global grid,run
    if run == True:
    
        gol.display(grid)
        grid = gol.newgen(grid)
        if keyPressed:
            if key == 'r':
                grid = gol.makeboard()
                gol.display(grid)
                run = False
            elif key == 'a':
                run = False
    else:
        
        if mousePressed and mouseButton == LEFT:
            try:
                grid[mouseY/10][mouseX/10] = 1
            except:
                pass
            fill(0)
            rect(mouseX/10*gol.w,mouseY/10*gol.w,gol.w,gol.w)   
        elif mousePressed and mouseButton == RIGHT:
            try:
                grid[mouseY/10][mouseX/10] = 0
            except:
                pass
            fill(255)
            rect(mouseX/10*gol.w,mouseY/10*gol.w,gol.w,gol.w) 
        if keyPressed:
            if key == 's':
                run = True
            elif key == 'p':
                board = gol.makeboard()
                grid = gol.creategen0(board)
                run = True
            elif key == 'n':
                grid = gol.newgen(grid)
                gol.display(grid)
        
                
        
        

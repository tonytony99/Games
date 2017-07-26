import pygame, time, math, random, sys
from pygame.locals import *
pygame.init()


class box:
    def __init__(self,x):
        self.gap_height=random.randint(80,200)
        self.width=20
        self.xpos=x

    def draw_box(self,screen,white):
        pygame.draw.rect(screen,white,((self.xpos,0),(self.width,self.gap_height)))
        pygame.draw.rect(screen,white,((self.xpos,self.gap_height+120),(self.width,400)))
            

class bird:
    def __init__(self):
        self.height=200
        self.alive=False
        self.direction=0
        self.y_vel=0

    def draw_bird(self,screen,white,black,direction):
        pygame.draw.circle(screen,white,(100,self.height),20)
        pygame.draw.circle(screen,black,(int(110-direction/2),self.height-6-int(direction)),4)
        
        

class player:
    
    
    def main(dimensions):
        def close():
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                    
        def gravity(y_vel):
            if y_vel>-1:
                return y_vel-0.3
            else:
                return y_vel-0.15
        
        

        def jump(mouse_ready,y_vel):
            mouse=pygame.mouse.get_pressed()
            if mouse[0]==1 and mouse_ready:
                mouse_ready=False
                return 6
                
            if mouse[0]==0:
                mouse_ready=True
                return y_vel
            else:
                return y_vel

        def new_highscore(highscore):
            return fonti.render("Hi : "+str(highscore),1,white)
            
        mouse_ready=False
        y_vel=0
        white=[255,255,255]
        black=[0,0,0]
        screen=pygame.display.set_mode(dimensions)

        birdie=bird()
        score=0
        highscore=0
        game_on=False
        pre_game=True
        game_off=False
        
        try:
            font=pygame.font.SysFont('Impact', 30)
            fonti=pygame.font.SysFont('Impact', 20)
        except:
            font=pygame.font.SysFont('Courier', 30)
            fonti=pygame.font.SysFont('Courier', 20)
        begin_msg=font.render("Burd Game!",1,white)

      
                    
        highscore_msg=new_highscore(0)
        
        
        while 1:
            mainLoopStartTime = time.time()
            mainLoopEndTime = mainLoopStartTime+0.015
            close()
            screen.fill(black)

            screen.blit(highscore_msg,(10,10))

            if pre_game:
                score=0                
                birdie.height=200
                birdie.direction=0
                birdie.draw_bird(screen,white,black,birdie.direction)
                screen.blit(begin_msg,(300,185))
                mouse=pygame.mouse.get_pressed()
                
                
                if mouse[0]==1:
                    game_on=True
                    pre_game=False
                    birdie.y_vel=6
                    a=box(600)
                    b=box(1100)

            if game_off:
                while birdie.height<380:
                    screen.fill(black)
                    screen.blit(highscore_msg,(10,10))
                    if birdie.direction>-14:
                        birdie.direction-=0.3
                    birdie.y_vel=gravity(birdie.y_vel)
                    birdie.height-=int(birdie.y_vel)
                    birdie.draw_bird(screen,white,black,birdie.direction)
                    a.draw_box(screen,white)                
                    b.draw_box(screen,white)
                    time.sleep(0.012)
                    pygame.display.update()
                for i in range(100):
                    time.sleep(0.01)
                    close()
                pre_game=True
                game_off=False
                    
                    
                    
            
            if game_on:
                mouse=pygame.mouse.get_pressed()
                if mouse[0]==0:
                    mouse_ready=True            
                birdie.y_vel=gravity(birdie.y_vel)
                birdie.y_vel=jump(mouse_ready,birdie.y_vel)
                birdie.height-=int(birdie.y_vel)
                if 96<a.xpos<124:
                    if not(a.gap_height+20<birdie.height<a.gap_height+100):
                        game_on=False
                        game_off=True
                    if a.xpos==100:
                        b=box(600)
                        score+=1

                        if score>highscore:
                            highscore=score; highscore_msg=new_highscore(highscore)
                        
                if 96<b.xpos<124:
                    if not(b.gap_height+20<birdie.height<b.gap_height+100):
                        game_on=False
                        game_off=True
                    if b.xpos==100:
                        a=box(600)
                        score+=1

                        if score>highscore:
                            highscore=score; highscore_msg=new_highscore(highscore)

                

                
                birdie.direction=int(birdie.y_vel)
                score_msg=font.render(str(score),1,white)
                
                a.xpos-=4
                b.xpos-=4
                
                
                a.draw_box(screen,white)
                b.draw_box(screen,white)                                    

                screen.blit(score_msg,(60,birdie.height-40))
                birdie.draw_bird(screen,white,black,birdie.direction)
                if birdie.height>380:
                    game_on=False
                    game_off=True
                    
            while(time.time() < mainLoopEndTime):
                time.sleep(0.00001)
            pygame.display.update()
        



    dimensions=(600,400)
    main(dimensions)


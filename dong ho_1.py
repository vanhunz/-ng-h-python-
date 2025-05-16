import pygame
import time
import math
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('dong ho dem nguoc')
GREY=(150,150,150)
BLACK=(0,0,0)
WHITE=(255, 255, 255)
RED=(255,0,0)
fontchu=pygame.font.SysFont('sans', 35)
plus=fontchu.render('+', True, BLACK) #font cho dau + 
minus=fontchu.render('-', True, BLACK) #font cho dau -
start_text=fontchu.render('START', True, BLACK) #font START
reset_text=fontchu.render('RESET', True, BLACK) #font RESET
running=True
sogiay=0
start=False
nhac=pygame.mixer.Sound('HUAN.mp3')
sogiayconlai=0
while running:
    
    screen.fill(GREY)
    pygame.draw.rect(screen, WHITE, (100,50,50,50)) #nut cong phut
    pygame.draw.rect(screen, WHITE, (200,50,50,50)) #nut  cong giay
    pygame.draw.rect(screen, WHITE, (300,50,100,50)) # nut START

    pygame.draw.rect(screen, WHITE, (100,200,50,50)) #nut tru phut
    pygame.draw.rect(screen, WHITE, (200,200,50,50)) #nut tru giay
    pygame.draw.rect(screen, WHITE, (300,200,100,50)) #nut RESET

    pygame.draw.circle(screen, BLACK, (300,400),100) #mat dong ho
    pygame.draw.circle(screen, WHITE, (300,400),95)
    pygame.draw.circle(screen, BLACK, (300,400),5) 
    #pygame.draw.line(screen, BLACK, (300,400),(300, 320)) #kim dong ho

    pygame.draw.rect(screen, BLACK, (100,530,400,50)) # thanh lui
    pygame.draw.rect(screen, WHITE, (105,535,390,40)) 

    screen.blit(plus, (105, 52)) # ghi dấu +
    screen.blit(plus, (205, 52))
    
    screen.blit(minus, (105,200 )) # ghi dau -
    screen.blit(minus, (205, 200))
    
    screen.blit(start_text, (305,50 )) # ghi chu START
    screen.blit(reset_text, (305, 200))# ghi chu RESET

    x,y=pygame.mouse.get_pos()
       
    for sukien in pygame.event.get():
        if sukien.type==pygame.QUIT:
            running=False
        if sukien.type==pygame.MOUSEBUTTONDOWN:
            if sukien.button==1: #neu an chuot trai
                if 100<=x<=150 and 50<=y<=100: #phạm vi của nut + phut
                    print(' cong 1 phut')
                    sogiay+=60
                    sogiayconlai=sogiay
                if 200<=x<=250 and 50<=y<=100:
                    print(' cong 1 giay')
                    sogiay+=1
                    sogiayconlai=sogiay
                if 100<=x<=150 and 200<=y<=250:
                    print(' tru 1 phut')
                    sogiay-=60
                    sogiayconlai=sogiay
                if 200<=x<=250 and 200<=y<=250:
                    print(' tru 1 giay')
                    sogiay-=1
                    sogiayconlai=sogiay
                if 300<=x<=400 and 50<=y<=100:
                    start=True
                    
                    print(' nut START')
                if 300<=x<=400 and 200<=y<=250:
                    sogiay=0
                    print(' nut RESET')
    #print(sogiay)
    sophut=sogiay//60  #chia lấy phần nguyên
    sogiayle=sogiay%60 #chia 60 lấy phần dư
    time1=str(sophut) +':' + str(sogiayle)
    time_text=fontchu.render(time1, True, BLACK)
    screen.blit(time_text, (120,120))
    
    if start==True:
        sogiay-=1
        if sogiay==0:
            start=False
            pygame.mixer.Sound.play(nhac)
            
        time.sleep(0.05)
        #sogiayconlai=sogiay
    if sogiay<=0:
        
        start=False
   
    x_giay=300+ 90*math.sin(6*sogiayle*math.pi/180)
    y_giay=400- 90*math.cos(6*sogiayle*math.pi/180)
    pygame.draw.line(screen, BLACK,(300, 400), (int(x_giay), int(y_giay)))

    x_phut=300+ 40*math.sin(6*sophut*math.pi/180)
    y_phut=400- 40*math.cos(6*sophut*math.pi/180)
    pygame.draw.line(screen, RED,(300, 400), (int(x_phut), int(y_phut)))

    if sogiayconlai!=0:
        pygame.draw.rect(screen, RED, (100,535, int(400*(sogiay/sogiayconlai)),40))
    pygame.display.flip()
pygame.quit()

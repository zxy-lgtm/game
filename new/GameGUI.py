from GameSystem import GameSystem
import pygame

class GameGUI():

    def __init__(self):
        pygame.init()
        self.gameSystem = GameSystem()
        self.screen = pygame.display.set_mode((600, 800), 0, 32)
        self.score = 0 # score to trigger the events
        self.clocks = []

        self.COUNT = pygame.USEREVENT + 1 # main timer used to update the frame
        self.doubleClickEvent = pygame.USEREVENT+2
        self.umbrellaEvent = pygame.USEREVENT+3
        self.waterEvent = pygame.USEREVENT+4
        self.glassesEvent = pygame.USEREVENT+5
        self.bagEvent = pygame.USEREVENT+6
        self.phoneEvent = pygame.USEREVENT+7

        self.doubleClickEventCount = 0
        self.umbrellaEventCount = 0
        self.waterEventCount = 0
        self.glassesEvent = 0
        self.bagEvent = 0
        self.phoneEvent = 0

        self.eventCount = 0
        self.timeCount = 1000
        self.callerNames = []

    def umbrella_event(self):
        if self.umbrellaEventCount == 0:
            pygame.time.set_timer(self.umbrellaEvent, 300)
            self.umbrellaEventCount = 11
            pass
            # start this event
            # print the clock
        else:
            self.umbrellaEventCount -= 1

            pass
            # update the clock
            # if over add fail

        pass

    def click_in_umbrella(self,x,y):
        if x==0 and y==0 and self.umbrellaEventCount != 0:
            pygame.time.set_timer(self.umbrellaEvent,15000)
            self.umbrellaEventCount = 0

        # stop the clock
        # redraw the screen

        pass

    def water_event(self):
        pass

    def glasses_event(self):
        pass

    def bag_event(self):
        pass

    def phone_event(self):
        pass

    def game_start(self):
        # start the game
        self.main_loop()

    def game_end(self):
        # stop the game, restart, show the score
        pass

    def update_frame(self):
        self.score += 1
        # start events
        # update the frame

    def main_loop(self):
        pygame.time.set_timer(self.COUNT, self.timeCount)
        while True:
            if self.gameSystem.check_fail():
                self.game_end()
            for event in pygame.event.get():
                if event.type == self.umbrellaEvent:
                    self.umbrella_event()

                if event.type == self.waterEvent:
                    self.water_event()

                if event.type == self.glassesEvent:
                    self.glasses_event()

                if event.type == self.bagEvent:
                    self.bag_event()

                if event.type == self.phoneEvent:
                    self.phone_event()

                if event.type == self.COUNT:
                    self.update_frame()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.doubleClickEventCount == 0:
                        self.doubleClickEventCount = 1
                        pygame.time.set_timer(self.doubleClickEvent,500)
                        # check one click event
                        if self.click_in_umbrella(event.pos[0],event.pos[1]):
                            pass

                    elif self.doubleClickEventCount == 1:
                        self.doubleClickEventCount = 0
                        pygame.time.set_timer(self.doubleClickEvent,0)
                        # check the one click event and double click event
                        pass

                if event.type == self.doubleClickEvent:
                    self.doubleClickEventCount = 0
                    pygame.time.set_timer(self.doubleClickEvent, 0)

                if event.type == pygame.QUIT:
                    exit()

    def reset_timer(self,num):
        pygame.time.set_timer(self.COUNT,num)






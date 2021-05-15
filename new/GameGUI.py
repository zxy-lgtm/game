from GameSystem import GameSystem
import pygame

def is_rect(pos,rect):
    x,y =pos
    rx,ry,rw,rh = rect
    if (rx <= x <=rx+rw)and(ry <= y <= ry +rh):
        return True
    return False

class GameGUI():

    def __init__(self):
        pygame.init()
        self.gameSystem = GameSystem()
        self.screen = pygame.display.set_mode((1280, 720), 0, 32)
        self.score = 0 # score to trigger the events
        self.start_parts = {
            "background":ScreenObject("C:\\Users\\91609\\Pictures\\_DSC7985.jpg",1,2),
            "button":ScreenObject("C:\\Users\\91609\\Pictures\\_DSC7985.jpg")
        }
        self.screenParts = {"background":ScreenObject("C:\\Users\\91609\\Pictures\\_DSC7985.jpg",0,0),
                            "roads":None,
                            "legs":None,
                            "character":None,
                            "umbrella":ScreenObject("C:\\Users\\91609\\Pictures\\Camera Roll\\1.png",50,50),
                            "bag":None,
                            "glasses":None,
                            "phone":None,
                            "clock_umbrella":None,
                            "clock_water":None,
                            "clock_glasses":None,
                            "clock_bag":None,
                            "clock_phone":None,
                            }

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
            self.umbrellaEventCount = 10
            self.screenParts["umbrella"] = ScreenObject("C:\\Users\\91609\\Pictures\\Camera Roll\\2.png",50,50)
            self.update_frame()
            # start this event
            # print the clock
        else:
            self.umbrellaEventCount -= 1

            if self.umbrellaEventCount == 0:
                self.screenParts["umbrella"] = ScreenObject("C:\\Users\\91609\\Pictures\\Camera Roll\\1.png", 50, 50)
                self.update_frame()
                pygame.time.set_timer(self.umbrellaEvent, 8000)
                self.gameSystem.add_failure()

            pass
            # update the clock
            # if fail add fail

        pass

    def click_in_umbrella(self,x,y):
        print(x,y)
        rec = self.screenParts["umbrella"].object.get_rect()
        if is_rect((x,y),rec) and self.umbrellaEventCount != 0:
            print("clicked")
            pygame.time.set_timer(self.umbrellaEvent,8000)
            self.umbrellaEventCount = 0
            self.screenParts["umbrella"] = ScreenObject("C:\\Users\\91609\\Pictures\\Camera Roll\\1.png", 50, 50)
            self.update_frame()

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
        print("game over")
        pass

    def game_time(self):
        print(self.score)
        self.score+=1
        if self.score == 5:
            pygame.time.set_timer(self.umbrellaEvent,8000)
        pass

    def update_frame(self):
        if self.screenParts["background"] != None:
            self.screen.blit(self.screenParts["background"].object,self.screenParts["background"].position)

        if self.screenParts["roads"] != None:
            self.screen.blit(self.screenParts["roads"].object, self.screenParts["roads"].position)

        if self.screenParts["legs"] != None:
            self.screen.blit(self.screenParts["legs"].object, self.screenParts["legs"].position)

        if self.screenParts["character"] != None:
            self.screen.blit(self.screenParts["character"].object, self.screenParts["character"].position)

        if self.screenParts["umbrella"] != None:
            self.screen.blit(self.screenParts["umbrella"].object, self.screenParts["umbrella"].position)

        if self.screenParts["bag"] != None:
            self.screen.blit(self.screenParts["bag"].object, self.screenParts["bag"].position)

        if self.screenParts["glasses"] != None:
            self.screen.blit(self.screenParts["glasses"].object, self.screenParts["glasses"].position)

        if self.screenParts["phone"] != None:
            self.screen.blit(self.screenParts["phone"].object, self.screenParts["phone"].position)

        if self.screenParts["clock_umbrella"] != None:
            self.screen.blit(self.screenParts["clock_umbrella"].object, self.screenParts["clock_umbrella"].position)

        if self.screenParts["clock_water"] != None:
            self.screen.blit(self.screenParts["clock_water"].object, self.screenParts["clock_water"].position)

        if self.screenParts["clock_glasses"] != None:
            self.screen.blit(self.screenParts["clock_glasses"].object, self.screenParts["clock_glasses"].position)

        if self.screenParts["clock_bag"] != None:
            self.screen.blit(self.screenParts["clock_bag"].object, self.screenParts["clock_bag"].position)

        if self.screenParts["clock_phone"] != None:
            self.screen.blit(self.screenParts["clock_phone"].object, self.screenParts["clock_phone"].position)

        pygame.display.update()
        # start events
        # update the frame

    def main_loop(self):
        pygame.time.set_timer(self.COUNT, self.timeCount)
        while True:
            if self.gameSystem.check_fail():
                break

            self.update_frame()
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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.doubleClickEventCount == 0:
                        self.doubleClickEventCount = 1
                        pygame.time.set_timer(self.doubleClickEvent,500)
                        # check one click event
                        self.click_in_umbrella(event.pos[0],event.pos[1])

                    elif self.doubleClickEventCount == 1:
                        self.doubleClickEventCount = 0
                        pygame.time.set_timer(self.doubleClickEvent,0)
                        # check the one click event and double click event
                        pass

                if event.type == self.doubleClickEvent:
                    self.doubleClickEventCount = 0
                    pygame.time.set_timer(self.doubleClickEvent, 0)

                if event.type == self.COUNT:
                    self.game_time()

                if event.type == pygame.QUIT:
                    exit()
        self.game_end()

    def reset_timer(self,num):
        pygame.time.set_timer(self.COUNT,num)

class ScreenObject():

    def __init__(self,path,x=0,y=0):
        self.object = pygame.image.load(path).convert_alpha()
        self.position = (x,y)

if __name__ == "__main__":
    game = GameGUI()
    game.game_start()



from GameSystem import GameSystem
import pygame

def is_rect(pos,obj):
    rect = obj.object.get_rect()
    x,y =pos
    x -= obj.position[0]
    y -= obj.position[1]
    rx,ry,rw,rh = rect
    if (rx <= x <=rx+rw)and(ry <= y <= ry +rh):
        return True
    return False

class GameGUI():

    def __init__(self):
        pygame.init()
        self.gameSystem = GameSystem()
        self.screen = pygame.display.set_mode((1920, 1080), 0, 32)
        self.score = 0 # score to trigger the events
        self.start_parts = {
            "background":ScreenObject("C:\\Users\\91609\\Pictures\\_DSC7985.jpg",1,2),
            "button":ScreenObject("C:\\Users\\91609\\Pictures\\_DSC7985.jpg")
        }
        self.parsNames = ["background",
                            "water",
                            "legs",
                            "character",
                            "umbrella",
                            "bag",
                            "glasses",
                            "phone",
                            "clock_umbrella",
                            "clock_water",
                            "clock_glasses",
                            "clock_bag",
                            "clock_phone",]
        self.screenParts = {"background":ScreenObject("./../pics/background.png",0,0),
                            "water":ScreenObject("./../pics/water.png",600,600),
                            "legs":None,
                            "character":None,
                            "umbrella":ScreenObject("./../pics/umbrella1.png",500,500),
                            "bag":None,
                            "glasses":ScreenObject("./../pics/glasses.png",700,700),
                            "phone":None,
                            "clock_umbrella":None,
                            "clock_water":None,
                            "clock_glasses":None,
                            "clock_bag":None,
                            "clock_phone":None,
                            }
        self.pointers = {
            "clock_umbrella": None,
            "clock_water": None,
            "clock_glasses": None,
            "clock_bag": None,
            "clock_phone": None,
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
        self.glassesEventCount = 0
        self.bagEventCount = 0
        self.phoneEventCount = 0
        self.counts = {
            "umbrella":0,
            "glasses":0,
            "bag":0,
            "water":0,
            "phone":0,
        }

        self.eventCount = 0
        self.timeCount = 1000
        self.callerNames = []

    def draw_clock(self,clockName,position,num):
        self.screenParts[clockName] = ScreenObject("./../pics/clock.png",position[0],position[1])
        print("drawing")
        pointer = ScreenObject("./../pics/pointer.png",position[0],position[1]).object
        pointer = pygame.transform.rotate(pointer,num*90)
        self.pointers[clockName] = ScreenObject("",position[0],position[1],pointer)
        self.update_frame()


    def umbrella_event(self):
        path0 = "./../pics/umbrella1.png"
        path1 = "./../pics/umbrella2.png"
        path2 = "./../pics/umbrella3.png"
        path3 = "./../pics/umbrella4.png"
        pathOrigin = "./../pics/umbrella1.png"
        partName = "umbrella"
        clockName = "clock_umbrella"

        position1 = (500,500)
        position2 = (500,500)
        position3 = (500,500)
        position4 = (500,500)
        positionOrigin = (500,500)
        clockPosition = (500,500)

        if self.counts[partName]== 0:
            pygame.time.set_timer(self.umbrellaEvent, 300)
            self.counts[partName] = 10
            self.screenParts[partName] = ScreenObject(path0,position1[0],position1[1])
            self.draw_clock(clockName,clockPosition,0)
            self.update_frame()
        else:
            self.counts[partName] -= 1
            if self.counts[partName] == 7:
                self.screenParts[partName] = ScreenObject(path1, position2[0],position2[1])
                self.draw_clock(clockName, clockPosition, 1)
                self.update_frame()
            elif self.counts[partName] == 5:
                self.screenParts[partName] = ScreenObject(path2, position3[0],position3[1])
                self.draw_clock(clockName, clockPosition, 2)
                self.update_frame()
            elif self.counts[partName] == 3:
                self.screenParts[partName] = ScreenObject(path3, position4[0],position4[1])
                self.draw_clock(clockName, clockPosition, 3)
                self.update_frame()
            elif self.counts[partName] == 0:
                self.screenParts[partName] = ScreenObject(pathOrigin, positionOrigin[0],positionOrigin[1])
                self.draw_clock(clockName, clockPosition, 4)
                self.update_frame()
                self.screenParts[clockName] = ScreenObject("./../pics/empty_clock.png")
                self.pointers[clockName]= ScreenObject("./../pics/empty_clock.png")
                pygame.time.set_timer(self.umbrellaEvent, 8000)
                self.gameSystem.add_failure()
            # update the clock
            # if fail add fail


    def click_in_umbrella(self,x,y):
        print(x,y)
        partName = "umbrella"
        clockName = "clock_umbrella"
        pathOrigin = "./../pics/umbrella1.png"
        positionOrigin = (500,500)

        print(is_rect((x,y),self.screenParts[partName]))
        print(self.counts[partName])
        if is_rect((x,y),self.screenParts[partName]) and self.counts[partName] != 0:
            print("clicked")
            pygame.time.set_timer(self.umbrellaEvent,8000)
            self.counts[partName] = 0
            self.screenParts[partName] = ScreenObject(pathOrigin, positionOrigin[0],positionOrigin[1])
            self.screenParts[clockName] = ScreenObject("./../pics/empty_clock.png")
            self.pointers[clockName] = ScreenObject("./../pics/empty_clock.png")
            self.update_frame()
            print("updated")
            print(self.screenParts)




    def water_event(self):
        path0 = "./../pics/water.png"
        path1 = "./../pics/water.png"
        path2 = "./../pics/water.png"
        path3 = "./../pics/water.png"
        pathOrigin = "./../pics/water.png"
        partName = "water"
        clockName = "water"

        position1 = (600, 600)
        position2 = (600, 620)
        position3 = (600, 640)
        position4 = (600, 660)
        positionOrigin = (600, 680)
        clockPosition = (650, 650)

        if self.counts[partName]== 0:
            pygame.time.set_timer(self.waterEvent, 300)
            self.counts[partName] = 10
            self.screenParts[partName] = ScreenObject(path0,position1[0],position1[1])
            self.draw_clock(clockName,clockPosition,0)
            self.update_frame()
        else:
            self.counts[partName] -= 1
            if self.counts[partName] == 7:
                self.screenParts[partName] = ScreenObject(path1, position2[0],position2[1])
                self.draw_clock(clockName, clockPosition, 1)
                self.update_frame()
            elif self.counts[partName] == 5:
                self.screenParts[partName] = ScreenObject(path2, position3[0],position3[1])
                self.draw_clock(clockName, clockPosition, 2)
                self.update_frame()
            elif self.counts[partName] == 3:
                self.screenParts[partName] = ScreenObject(path3, position4[0],position4[1])
                self.draw_clock(clockName, clockPosition, 3)
                self.update_frame()
            elif self.counts[partName] == 0:
                self.screenParts[partName] = ScreenObject(pathOrigin, positionOrigin[0],positionOrigin[1])
                self.draw_clock(clockName, clockPosition, 4)
                self.update_frame()
                self.screenParts[clockName] = ScreenObject("./../pics/empty_clock.png")
                self.pointers[clockName]= ScreenObject("./../pics/empty_clock.png")
                pygame.time.set_timer(self.waterEvent, 8000)
                self.gameSystem.add_failure()


    def click_in_water(self,x,y):
        print(x,y)
        partName = "water"
        pathOrigin = "./../pics/water.png"
        positionOrigin = (500,500)
        clockName = "clock_water"

        print(is_rect((x,y),self.screenParts[partName]))
        print(self.counts[partName])
        if is_rect((x,y),self.screenParts[partName]) and self.counts[partName] != 0:
            print("clicked_water")
            pygame.time.set_timer(self.waterEvent,8000)
            self.counts[partName] = 0
            self.screenParts[partName] = ScreenObject(pathOrigin, positionOrigin[0],positionOrigin[1])
            self.screenParts[clockName] = ScreenObject("./../pics/empty_clock.png")
            self.pointers[clockName] = ScreenObject("./../pics/empty_clock.png")
            self.update_frame()
            print("updated")
            print(self.screenParts)



    def glasses_event(self):
        path0 = "./../pics/glasses.png"
        path1 = "./../pics/glasses.png"
        path2 = "./../pics/glasses.png"
        path3 = "./../pics/glasses.png"
        pathOrigin = "./../pics/glasses.png"
        partName = "glasses"
        clockName = "clock_glasses"

        position1 = (600, 600)
        position2 = (600, 620)
        position3 = (600, 640)
        position4 = (600, 660)
        positionOrigin = (600, 680)
        clockPosition = (650, 650)

        if self.counts[partName]== 0:
            pygame.time.set_timer(self.glassesEvent, 300)
            self.counts[partName] = 10
            self.screenParts[partName] = ScreenObject(path0,position1[0],position1[1])
            self.draw_clock(clockName,clockPosition,0)
            self.update_frame()
        else:
            self.counts[partName] -= 1
            if self.counts[partName] == 7:
                self.screenParts[partName] = ScreenObject(path1, position2[0],position2[1])
                self.draw_clock(clockName, clockPosition, 1)
                self.update_frame()
            elif self.counts[partName] == 5:
                self.screenParts[partName] = ScreenObject(path2, position3[0],position3[1])
                self.draw_clock(clockName, clockPosition, 2)
                self.update_frame()
            elif self.counts[partName] == 3:
                self.screenParts[partName] = ScreenObject(path3, position4[0],position4[1])
                self.draw_clock(clockName, clockPosition, 3)
                self.update_frame()
            elif self.counts[partName] == 0:
                self.screenParts[partName] = ScreenObject(pathOrigin, positionOrigin[0],positionOrigin[1])
                self.draw_clock(clockName, clockPosition, 4)
                self.update_frame()
                self.screenParts[clockName] = ScreenObject("./../pics/empty_clock.png")
                self.pointers[clockName]= ScreenObject("./../pics/empty_clock.png")
                pygame.time.set_timer(self.glassesEvent, 8000)
                self.gameSystem.add_failure()

    def click_in_glasses(self,x,y):
        print(x,y)
        partName = "glasses"
        pathOrigin = "./../pics/glasses.png"
        positionOrigin = (500,500)
        clockName = "clock_glasses"

        print(is_rect((x,y),self.screenParts[partName]))
        print(self.counts[partName])
        if is_rect((x,y),self.screenParts[partName]) and self.counts[partName] != 0:
            print("clicked_glasses")
            pygame.time.set_timer(self.glassesEvent,8000)
            self.counts[partName] = 0
            self.screenParts[partName] = ScreenObject(pathOrigin, positionOrigin[0],positionOrigin[1])
            self.screenParts[clockName] = ScreenObject("./../pics/empty_clock.png")
            self.pointers[clockName] = ScreenObject("./../pics/empty_clock.png")
            self.update_frame()
            print("updated")
            print(self.screenParts)


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
            pygame.time.set_timer(self.waterEvent,8000)
            pygame.time.set_timer(self.glassesEvent, 8000)
        pass

    def update_frame(self):
        for name in self.parsNames:
            if self.screenParts[name] != None:
                self.screen.blit(self.screenParts[name].object,self.screenParts[name].position)

        for _,v in self.pointers.items():
            if v != None:
                self.screen.blit(v.object,v.position)
        pygame.display.flip()
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
                        self.click_in_water(event.pos[0],event.pos[1])
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

    def __init__(self,path,x=0,y=0,screen = None):
        if screen == None:
            self.object = pygame.image.load(path).convert_alpha()
            self.position = (x,y)
        else:
            self.object = screen.convert_alpha()
            self.position = (x,y)

if __name__ == "__main__":
    game = GameGUI()
    game.game_start()



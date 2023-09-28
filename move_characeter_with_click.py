from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global hand_point
    global click
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            hand_point.append([event.x, TUK_HEIGHT - 1 -event.y])
            click = True
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def move_boy(boy, hands):
    pass


running = True
boy_point = [TUK_WIDTH // 2, TUK_HEIGHT // 2]
frame = 0
hand_point = []
click = False
while running:
    if click:
        hand.draw(hand_point[0][0], hand_point[0][0],100,100)
        update_canvas()
        pass
    handle_events()
close_canvas()





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
            hand_point.append([event.x, TUK_HEIGHT - 1 - event.y])
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def move_boy(boy, hands):
    global frame
    global boy_left
    x1, y1 = boy[0], boy[1]
    x2, y2 = hands[0][0], hands[0][1]
    if (boy[0] > hands[0][0]):
        boy_left = True
    else: 
        boy_left = False
    for i in range(0, 100 + 1, 5):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        if (boy_left):
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', boy_point[0], boy_point[1], 100, 100)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, boy_point[0], boy_point[1])
        t = i / 100
        boy_point[0] = (1 - t) * x1 + t * x2
        boy_point[1] = (1 - t) * y1 + t * y2
        for i in range (len(hand_point)):
            hand.draw(hand_point[i][0], hand_point[i][1])
            update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        handle_events()

    hands.remove(hands[0])

running = True
boy_point = [TUK_WIDTH // 2, TUK_HEIGHT // 2]
frame = 0
hand_point = []
click = False
boy_left =False

while running:
    if len(hand_point):
        move_boy(boy_point, hand_point)
    else:
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        if (boy_left):
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', boy_point[0], boy_point[1], 100, 100)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, boy_point[0], boy_point[1])
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    handle_events()
close_canvas()





# 월드 0번에는 background 객체를 / 월드 1번에는 foreground 객체를 저장함
world = [[], []]

def add_object(o, depth = 0):
    world[depth].append(o)


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    print(f'존재하지 않은 {o}를 지우려고 합니다.\n')
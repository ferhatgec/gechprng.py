import gechprng


def get_seed():
    from time import time

    return int(round(time() * 1000))


init = gechprng.gechprng()
init.feed(get_seed())

print(f'Your lucky number {init.generate() % 42}')

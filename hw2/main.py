from random import random, randint

from fabrics import GemGenerator, GoldGenerator, SilverGenerator, BronzeGenerator, IronGenerator

rewards = [GemGenerator(), GoldGenerator(), SilverGenerator(),
           BronzeGenerator(), IronGenerator()]
# если подгонять под задачу, то есть такое решение управляемой случайности
for i in range(100):
    rnd = random()
    if rnd < 0.018:
        rewards[0].create_item().open()
    elif rnd < 0.055:
        rewards[1].create_item().open()
    else:
        rewards[randint(2, len(rewards)-1)].create_item().open()

# если же говорить о том как бы я это делал с заделом на будущее,
# то я бы делал в самих классах параметр, который бы показывал
# вероятность непосредственно, а после уже сравнивал бы этот показатель с тем что выпадет

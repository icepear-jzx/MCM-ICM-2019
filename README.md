# Cellular-Automata-Evacuation-Model

> A modified cellular automata model for 2019 Mathematical Contest in Modeling Problem D.
Our team was designated as Meritorious Winner!

## Usage

You can get more detailed information in our [paper](Escape-to-Victory-from-the-Louvre.pdf).

You need to install pygame.

```shell
$ pip3 install pygame --user
```

At first, we assume that people are uniformly distributed in the room.
You can see the simulation of an evacuation without any guidance.

```shell
$ python3 room-default.py
```

You can see the simulation of an evacuation with a bar separating people to two groups.

```shell
$ python3 room-default-bar.py
```

Then we consider a more complicated situation with unevenly distributed people and we change the location of one door to make the two doors closer.
You can see the simulation by running this:

```shell
$ python3 room-imbalance.py
```

We use a more complicated strategy to guide and separate people.

```shell
$ python3 room-imbalance-bar.py
```

We move further forward to consider disabled or old people who move slowly, foreigners and people who are in the same tourist group.

```shell
$ python3 room-disable-foreign-group.py
```

We also consider a situation where a fireman tries to get to the fire. We can compare the time that the fireman takes to get to the fire between setting a channel specially for the fireman and not setting that.

```shell
$ python3 room-fireman-channel.py
```

Expand a single room to the whole layer:

```shell
$ python3 layer-default.py
```

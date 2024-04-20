import random
import time


def process_steps(x, steps):
    for step in steps:
        x = step(x)
    return x


def many_to_many(xs, f):
    ys = []
    for x in xs:
        y = f(x)
        ys.append(y)
    return ys


def many_to_wone(xs, f):
    from functools import reduce

    y = reduce(f, xs)
    return y


def wone_to_many(x, f):
    xs = f(x)
    return xs


def producer_consumer(xs, process):

    import goless

    ## Define Channels
    ##
    done = goless.chan()
    inputs = goless.chan()
    outputs = goless.chan()

    #      +--+--+
    #      |  P  |
    #      +--+--+
    #         | INS
    #    +----+----+--- ... ---+
    #    |         |           |
    # +--+--+   +--+--+     +--+--+
    # | C 1 |   | C 2 | ... | C n |
    # +--+--+   +--+--+     +--+--+
    #    |         |
    #    +----+----+
    #         | OUTS
    #      +--+--+
    #      |  L  |
    #      +--+--+
    #         |
    #        DONE

    #
    # PRODUCER (P)
    #

    def produce():
        # Produce inputs
        #
        # xs = dir.list_dir("./input")
        print("_ _ " * 10 + "Feed inputs channel by producer")
        for x in xs:
            inputs.send(x)

        # All inputs send -> close channel
        #
        print("_ _ " * 10 + "Close inputs channel by producer")
        inputs.close()

    ##
    ## CONSUMER (C n)
    ##

    def consume(name):
        for input in inputs:  # Drain all inputs (ins)
            output = process(input)
            c = random.randrange(100000, 1000000)
            print(c)
            for i in range(0, c):
                i * i
            print(f"Consume {input} by {name}")
            outputs.send(output)
        print("_ _ " * 10 + f"Close channel by {name}")
        outputs.close()

    #
    # Logger (L)
    #
    def logger():
        for output in outputs:  # Drain all outputs (outs)
            print(f"Logger {output}")
        #
        # If channel is empty -> send done
        #
        print("_ _ " * 10 + f"Logger send done!")
        done.send()

    # --------------------------------------------------------------------------
    # GO
    # --------------------------------------------------------------------------

    # 1 Produce stuff
    goless.go(produce)

    # 2 Start N Consumers
    for i in range(0, 3):
        goless.go(consume, "consumer_" + str(i))

    # 3 Logger and Finisher
    goless.go(logger)

    # 4 Wait until done
    #
    done.recv()

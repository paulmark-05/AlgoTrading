def crossover(current_a, previous_a,
              current_b, previous_b):

    return (
        previous_a <= previous_b
        and
        current_a > current_b
    )


def crossunder(current_a, previous_a,
               current_b, previous_b):

    return (
        previous_a >= previous_b
        and
        current_a < current_b
    )
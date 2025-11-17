def split_at_first_digit(formula):
    digit_location = 1
    for i in formula[1:]:
      if i.isdigit():
        break

      else:
        digit_location += 1

    prefix = formula[:digit_location]
    num_pos = formula[digit_location:]

    if digit_location == len(formula):
        return (formula, 1)

    return (prefix, int(num_pos))


def split_at_first_digit(formula):
    pass # Replace the `pass` with your code

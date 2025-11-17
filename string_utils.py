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


def split_before_each_uppercases(formula):
    start = 0
    end = 1
    split_formula = []
    for i in formula[1:]:
      if i.isupper():
          split_formula.append(formula[start:end])
          start = end
          end = start + 1

      else: 
        end += 1
    split_formula.append(formula[start:end])
    return (split_formula)

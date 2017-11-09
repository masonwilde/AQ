def combine_complex(complex1, complex2):
    new_complex = []
    for selector1 in complex1:
        new_complex.append(selector1)
    for selector2 in complex2:
        if selector2 not in new_complex:
            new_complex.append(selector2)
    return new_complex

def disjunction(star1, star2, maxstar):
    new_star = []
    for complex1 in star1:
        for complex2 in star2:
            new_star.append(combine_complex(complex1, complex2))
            if len(new_star) >= maxstar:
                return new_star
    return new_star

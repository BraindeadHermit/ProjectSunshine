from nlp.pos_tag import generate_tag


def is_singular(term):
    tag = generate_tag(term)
    if tag == 'NN' or tag == 'NNP':
        return True
    else:
        return False


def is_plural(term):
    tag = generate_tag(term)
    if tag == 'NNS' or tag == 'NNPS':
        return True
    else:
        return False
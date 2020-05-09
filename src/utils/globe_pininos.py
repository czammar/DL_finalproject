
## mkdir glove6B
## cd glove6B
## wget http://nlp.stanford.edu/data/glove.6B.zip # cerca de 800 MB
## ls -lha # glove.6B.50d.txt, glove.6B.100d.txt, glove.6B.200d.txt, glove.6B.300d.txt


def load_glove(path_to_glove='glove.6B.50d.txt'):
    '''
    Obtenemos la representacion de la coleccion glove.GB.XXd.txt especificada
    '''

    # Lectura del archivo donde se tiene la representacion de glove
    file = open(path_to_glove, mode='rt', encoding='utf8')

    # Obtenemos un array con la representacion numerica de las palabras
    word2em = {}
    for line in file:
        words = line.strip().split()
        word = words[0]
        embeds = np.array(words[1:], dtype=np.float32)
        word2em[word] = embeds

    file.close()

    return word2em

word2em = load_glove('glove.6B.50d.txt') # Con glove.6B.50d.txt esta en el directorio
embedding_dim=50

def encode_doc(doc, embedding_dim=50, max_allowed_doc_length=None):
    '''
    Representacion de una oracion en la coleccion glove.GB.XXd.txt antes cargada
    Nota: se fija un parametro de longitud maxima
    '''

    words = [w.lower() for w in doc.split(' ')]
    max_len = len(words)
    if max_allowed_doc_length is not None:
        max_len = min(len(words), max_allowed_doc_length)
        E = np.zeros(shape=(embedding_dim, max_len))
        X = np.zeros(shape=(embedding_dim, ))
        for j in range(max_len):
            word = words[j]
            try:
                E[:, j] = _word2em[word]
            except KeyError:
                pass
        X[:] = np.sum(E, axis=1)
    return X


# Ejemplos

doc='the shadow of your smile'
encode_doc(doc,50)
encode_doc('happy',50)
encode_doc('flower',10)
encode_doc('sunflower',10)
encode_doc('watermelon',10)

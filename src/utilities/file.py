def read_file(filename):
    # return (line for line in map(str.strip, open(filename)))
    return (line for line in open(filename))

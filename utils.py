def format_num(d):
    if d//10 == 0:
        return "0{}".format(d)
    else:
        return str(d)


def Lines_in_sutra(volume):
    """ volume: number (1~80)"""
    assert volume in [i for i in range(1,81)]
    readdata = ""
    with open('T0279/T0279_0{}.txt'.format(format_num(volume))) as f:
        readdata = f.readlines()
    return readdata

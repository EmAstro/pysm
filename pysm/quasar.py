import numpy as np
from pysm import utils as smutils


def M1450_to_M912(M1450):
    """Converts absolute magnitude M1450 to
    absolute magnitude M912 of a quasar assuming
    the relation in Lusso et al. (2015).

    Parameters
    ----------
    M1450 : np.array floats
        absolute magnitude at 1450Ang.

    Returns
    -------
    M912 : np.array floats
        absolute magnitude at 912Ang.
    """

    return np.array(M1450+0.33, dtype=np.float_)

def M912_to_1450(M912):
    """Converts absolute magnitude M912 to
    absolute magnitude M1450 of a quasar assuming
    the relation in Lusso et al. (2015).

    Parameters
    ----------
    M912 : np.array floats
        absolute magnitude at 912Ang.

    Returns
    -------
    M1450 : np.array floats
        absolute magnitude at 1450Ang.
    """

    return np.array(M912-0.33, dtype=np.float_)

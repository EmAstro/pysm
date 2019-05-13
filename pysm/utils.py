import numpy as np

doc = ""

doc += "    AB Magnitude zero point"
MABZP = np.float(-2.5*np.log10(3631.e-23))

doc += "    speed of light in km/s"
c_kms = 299792.458 # km/s


def listmacro():
    """ List macros in pysm.utils
    - MAB_to_LumNu
    """

def MAB_to_LumNu(MAB):
    """ Converts absolute magnitude in AB to
    luminosity in erg/s/Hz.

    Parameters
    ----------
    MAB : np.array floats
        absolute magnitude in AB


    Returns
    -------
    LumNu : np.array floats
        Luminosity in erg/s/Hz
    """

    Lum_nu = np.array(4.*.np.pi*10.**(-0.4*(MAB+MABZP)), dtype=np.float_)

    return Lum_nu

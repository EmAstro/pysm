import numpy as np


# Define some useful constants

doc = ""

doc += "MAB_ZP: AB Magnitude zero point"
MAB_ZP = np.float(-2.5*np.log10(3631.e-23))

doc += "c_kms: speed of light in km/s"
c_kms = np.float(299792.458) # km/s

doc += "c_kms: speed of light in km/s"
c_cms = np.float(2.99792458e10) # km/s

doc += "kpc_in_cm: conversion from kiloparsecs to cm"
kpc_in_cm = np.float(3.086e21)

doc += "kpc_in_cm: conversion from parsec to cm"
pc_in_cm = np.float(3.086e18)


# sterting the modulus

def listmacro():
    """ List macros in pysm.utils
    - MAB_to_LumNu
    """

    print(" ")
    print("Macros in pysm.utils")
    print("    - MAB_to_LumNu(MAB): M_AB to L in erg/s/Hz")
    print(" ")


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

    print("MAB_to_LumNu: return luminosity in erg/s/Hz")

    area = 4.*np.pi*np.power(10.*pc_in_cm,2.)
    Lum_nu = np.array(area*10.**(-0.4*(MAB+MABZP)), dtype=np.float_)

    del area

    return Lum_nu

def LumNu_to_MAB(LumNu):
    """ Converts luminosity in erg/s/Hz to
    absolute magnitude in AB.

    Parameters
    ----------
    LumNu : np.array floats
        Luminosity in erg/s/Hz

    Returns
    -------
    MAB : np.array floats
        absolute magnitude in AB
    """

    area = 4.*np.pi*np.power(10.*pc_in_cm,2.)

    MAB = np.array(-2.5 * np.log10(LumNu/area) - MABZP)

    del area

    return MAB

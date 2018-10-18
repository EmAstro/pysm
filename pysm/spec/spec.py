import numpy as np

from matplotlib import pyplot as plt

def PlotSpec(wavelength,
             flux,
             sigma=None,
             wave_min=None,
             wave_max=None,
             norm_flux=0.,
             save_name=None,
             spec_color='black'):
    """ Plot a spectrum given wavelength and flux.

    Parameters:
    ----------
    SpecObj : a Spectral Object
    
    Return:
    -------
    """
    _wavelength = np.copy(wavelength)/10**norm_flux
    _flux       = np.copy(flux)
    if sigma is not None:
        _sigma = np.copy(sigma)/10**norm_flux
    plt.figure()
    if sigma is not None:
        plt.plot(_wavelength,_sigma)
    plt.plot(_wavelength,_flux)
    plt.xlabel(r'Wavelength [\AA]')
    plt.ylabel(r'Flux $\times$10$^-{}$ [erg/s/cm$^2$/\AA]'.format(norm_flux))
    plt.show()



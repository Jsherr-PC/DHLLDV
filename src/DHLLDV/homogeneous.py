'''
homogeneous.py - calculations of newtonian (fluid), homogeneous and pseudo-homogeneous flow.

Created on Oct 7, 2014

@author: RCRamsdell
'''

from math import log, exp

from .DHLLDV_constants import gravity, musf, particle_ratio

Acv = 3.0   # coefficient homogeneous regime, see note after Eqn 8.7-8
kvK = 0.4   # von Karman constant

def pipe_reynolds_number(vls, Dp, nu):
    """
    Return the reynolds number for the given velocity, fluid & pipe
    vls: velocity in m/sec
    Dp: pipe diameter in m
    nu: fluid kinematic viscosity in m2/sec
    """
    return vls*Dp/nu    # Eqn 8.7-2 / 3.2-1


def swamee_jain_ff(Re, Dp, epsilon):
    """
    Return the friction factor using the Swaamee-Jain equation.
    Re: Reynolds number
    Dp: Pipe diameter in m
    epsilon: pipe absolute roughness in m
    """
    if Re <= 2320:
        #laminar flow
        return 64. / Re
    c1 = epsilon / (3.7 * Dp)
    c2 = 5.75 / Re**0.9
    bottom = log(c1 + c2)**2
    return 1.325 / bottom  # Eqn 8.2-7 / 8.7-3


def fluid_pressure_loss(vls, Dp, epsilon, nu, rhol):
    """
    Return the pressure loss (delta p in kPa) per m of pipe
    vls: line speed in m/sec
    Dp: Pipe diameter in m
    epsilon: pipe absolute roughness in m
    nu: fluid kinematic viscosity in m2/sec
    rhol: fluid density in ton/m3
    """
    Re = pipe_reynolds_number(vls, Dp, nu)
    lmbda = swamee_jain_ff(Re, Dp, epsilon)
    return lmbda*rhol*vls**2/(2*Dp) # Eqn 8.2-5
    

def fluid_head_loss(vls, Dp, epsilon, nu, rhol=1.0):
    """
    Return the head loss (il in m.l.c) per m of pipe
    vls: line speed in m/sec
    Dp: Pipe diameter in m
    epsilon: pipe absolute roughness in m
    nu: fluid kinematic viscosity in m2/sec
    rhol: fluid density in ton/m3, included for compatibility
    """
    Re = pipe_reynolds_number(vls, Dp, nu)
    lmbda = swamee_jain_ff(Re, Dp, epsilon)
    return lmbda*vls**2/(2*gravity*Dp) # Eqn 8.2-6 / 8.7-5


def apparent_density(rhol, rhos, Cvs, X):
    """
    Return the apparent density of the fluid given the fraction of fines
    rhol: fluid density in ton/m3
    rhos: particle density in ton/m3
    Cvs - spatial (insitu) volume concentration of solids
    X is the fraction of fines
    """
    Rsd = (rhos - rhol)/rhol     # Eqn 8.2-1
    return rhol + rhol*Rsd*X*Cvs/(1-Cvs+Cvs*X) # Eqn 8.3-1


def apparent_viscosity(nu, rhol, rhos, Cvs, X):
    """
    Return the apparent viscosity (nu-l,h) of a pseudo-homogeneous slurry, using the 
    Thomas (1965) approach.
    nu: fluid kinematic viscosity in m2/sec
    rhol: fluid density in ton/m3
    rhos: particle density in ton/m3
    Cvs - spatial (insitu) volume concentration of solids
    X is the fraction of fines
    """
    Rsd = (rhos - rhol)/rhol     # Eqn 8.2-1
    top = nu * (1 + 2.5*X*Cvs + 10.05*(X*Cvs)**2 + 0.00273*exp(16.6*X*Cvs))
    bottom = 1+Rsd*X*Cvs
    return   top/bottom # Eqn 8.3-2 modified to take nu directly


def apparent_concentration(Cvs, X):
    """
    Return the apparent concentration of solids in a pseudo-homogeneous fluid
    Cvs - spatial (insitu) volume concentration of solids
    X is the fraction of fines
    """
    return (1 - X) * Cvs # Eqn 8.3-3


def limiting_particle(Dp, nu, rhol, rhos, Stk = 0.03):
    """
    Return the limiting particle diameter for the particles influencing the
    viscosity
    Dp: Pipe diameter in m
    nu: fluid kinematic viscosity in m2/sec
    rhol: fluid density in ton/m3
    rhos: particle density in ton/m3
    Stk is the stokes number, here using 0.03 as a first approximation
    """
    top = Stk * 9 * rhol * nu * Dp
    bottom = rhos * 7.5 * Dp**0.4
    return (top/bottom)**0.5 # Eqn 8.15-2


def Erhg(vls, Dp, d, epsilon, nu, rhol, rhos, Cvs, use_sf = True):
    """Return the Erhg value for homogeneous flow.
    Use the Talmon (2013) correction for slurry density.
    vls: line speed in m/sec
    Dp: Pipe diameter in m
    d: Particle diameter in m
    epsilon: pipe absolute roughness in m
    nu: fluid kinematic viscosity in m2/sec
    rhol: fluid density in ton/m3
    rhos: particle density in ton/m3
    Cvs - spatial (insitu) volume concentration of solids
    use_sf: Whether to apply the sliding flow correction
    """
    Re = pipe_reynolds_number(vls, Dp, nu)
    lambda1 = swamee_jain_ff(Re, Dp, epsilon)
    Rsd = (rhos - rhol)/rhol     # Eqn 8.2-1
    rhom = rhol+Cvs*(rhos-rhol)
    deltav_to_d = min((11.6*nu)/((lambda1/8)**0.5*vls*d), 1)    # Eqn 8.7-7
    
    sb = ((Acv/kvK)*log(rhom/rhol)*(lambda1/8)**0.5+1)**2
    top = 1+Rsd*Cvs - sb
    bottom = Rsd*Cvs*sb
    il = fluid_head_loss(vls, Dp, epsilon, nu, rhol)
    f = d/(particle_ratio * Dp)  # Eqn 8.8-4 in 2nd ed B, overridden in 3rd edition
    if not use_sf or f<1:
        return il*(1-(1-top/bottom)*(1-deltav_to_d))            # Eqn 8.7-8
    else:
        #Sliding flow per equation 8.8-5 in 2nd ed B, overridden in 3rd edition
        return (il*(1-(1-top/bottom)*(1-deltav_to_d)) + (f-1)*musf)/f


def homogeneous_pressure_loss(vls, Dp, d, epsilon, nu, rhol, rhos, Cvs):
    """
    Return the pressure loss (delta_pm in kPa per m) for (pseudo) homogeneous flow incorporating viscosity correction.
    vls: line speed in m/sec
    Dp: Pipe diameter in m
    epsilon: pipe absolute roughness in m
    nu: fluid kinematic viscosity in m2/sec
    rhol: fluid density in ton/m3
    Cvs - spatial (insitu) volume concentration of solids
    """
    return homogeneous_head_loss(vls, Dp, d, epsilon, nu, rhol, rhos, Cvs)*gravity*rhol


def homogeneous_head_loss(vls, Dp, d, epsilon, nu, rhol, rhos, Cvs):
    """
    Return the head loss (m.l.c per m) for (pseudo) homogeneous flow incorporating viscosity correction.
    vls: line speed in m/sec
    Dp: Pipe diameter in m
    epsilon: pipe absolute roughness in m
    nu: fluid kinematic viscosity in m2/sec
    rhol: fluid density in ton/m3
    Cvs - spatial (insitu) volume concentration of solids
    """
    il = fluid_head_loss(vls, Dp, epsilon, nu, rhol)
    Rsd = (rhos - rhol)/rhol     # Eqn 8.2-1
    return Erhg(vls, Dp, d, epsilon, nu, rhol, rhos, Cvs)*Rsd*Cvs + il
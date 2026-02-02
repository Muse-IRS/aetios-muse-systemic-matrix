# ==================================================
# SSF — Phase Causale Φ
# ==================================================

import math

class PhaseCore:
    """
    Noyau de phase causale avec inertie IRS.
    """

    def __init__(self, alpha: float = 0.12, omega: float = 1.0):
        self.alpha = alpha
        self.omega = omega
        self.phi = 0.0
        self.phi_c = 0.0

    def step(self, dphi: float) -> float:
        self.phi += dphi
        self.phi_c = self.alpha * self.phi + (1.0 - self.alpha) * self.phi_c
        return self.phi_c

    def invariant_L(self) -> float:
        return (self.phi_c * math.pi) / self.omega

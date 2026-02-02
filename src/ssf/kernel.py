# ==================================================
# SSF — Kernel principal
# ==================================================

from .phase import PhaseCore
from .gate import SSFGate

class SSFKernel:
    """
    Kernel SSF minimal : Phase + Gate.
    """

    def __init__(self, alpha=0.12, epsilon=0.06):
        self.phase = PhaseCore(alpha=alpha)
        self.gate = SSFGate(epsilon=epsilon)

    def step(self, dphi: float, dt: float = 1.0) -> dict:
        phi_c = self.phase.step(dphi)
        status = self.gate.step(phi_c, dt)
        L = self.phase.invariant_L()

        return {
            "status": status,
            "phi_c": round(phi_c, 6),
            "L": round(L, 6),
            "t_dec": round(self.gate.t_dec, 3),
        }

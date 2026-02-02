# ==================================================
# SSF — Silence-First Framework
# Module : gate
# ==================================================

class SSFGate:
    """
    Gate causal SSF.
    Autorise ou inhibe l'exécution selon la divergence de phase.
    """

    def __init__(self, epsilon: float = 0.06):
        self.epsilon = epsilon
        self.last_phi_c = None
        self.t_dec = 0.0

    def step(self, phi_c: float, dt: float = 1.0) -> str:
        if self.last_phi_c is None:
            self.last_phi_c = phi_c
            return "SILENCE"

        div = abs(phi_c - self.last_phi_c)
        self.last_phi_c = phi_c

        if div > self.epsilon:
            self.t_dec += dt
            return "ACTIVE"

        return "SILENCE"

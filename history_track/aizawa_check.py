"""Check the equations in a social-media post: the Aizawa attractor (a real chaotic system), with the post's constants.
Integrates it, draws it, and measures how torus-like it is. History and art track; not physics evidence."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a, b, c, d, e, f = 0.95, 0.7, 0.6, 3.5, 0.25, 0.1        # as shown in the post


def rhs(t, s):
    x, y, z = s
    return [(z - b) * x - d * y,
            d * x + (z - b) * y,
            c + a * z - z ** 3 / 3 - (x * x + y * y) * (1 + e * z) + f * z * x ** 3]


sol = solve_ivp(rhs, (0, 600), [0.1, 0, 0], t_eval=np.linspace(100, 600, 120000), rtol=1e-9, atol=1e-11)
x, y, z = sol.y
r = np.hypot(x, y)
# Two nearby starts: chaos means they separate exponentially (rough largest Lyapunov exponent)
s2 = solve_ivp(rhs, (0, 600), [0.1 + 1e-9, 0, 0], t_eval=sol.t, rtol=1e-9, atol=1e-11).y
sep = np.linalg.norm(sol.y - s2, axis=0)
grow = (sep > 1e-12) & (sep < 1e-2)
lyap = np.polyfit(sol.t[grow], np.log(sep[grow]), 1)[0] if grow.sum() > 50 else float("nan")
print(f"radius r=sqrt(x^2+y^2): min {r.min():.3f}, median {np.median(r):.3f}, max {r.max():.3f}")
print(f"z range {z.min():.3f} .. {z.max():.3f}")
print(f"fraction of time with r > 0.3 (a hole down the middle, like a torus): {np.mean(r > 0.3):.3f}")
print(f"rough largest Lyapunov exponent: {lyap:.3f} (positive = chaotic)")

fig = plt.figure(figsize=(12, 5.5))
ax = fig.add_subplot(121, projection="3d")
ax.plot(x, y, z, lw=0.15, color="#4c72b0")
ax.set_title("Aizawa attractor (post's constants)")
ax.axis("off")
ax2 = fig.add_subplot(122)
ax2.plot(x, y, ",", alpha=0.3, color="#4c72b0")
ax2.set_aspect("equal"); ax2.set_title("Seen from above: the empty centre is the torus hole")
fig.suptitle("Real mathematics: a chaotic flow that winds around a torus-like shape. It says nothing about Earth or gravity.")
fig.tight_layout()
fig.savefig("aizawa_check.png", dpi=130)

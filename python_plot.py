import matplotlib.pyplot as plt


def vector_initialization(size):
    vector_list = [0.0] * size
    return vector_list


def main():
    times = 7000

    # Compartments
    S = vector_initialization(times)
    E = vector_initialization(times)
    I = vector_initialization(times)
    R = vector_initialization(times)
    V = vector_initialization(times)
    Q = vector_initialization(times)

    # Rates
    alpha_i = 1/14   # Recovery rate for infectious
    alpha_q = 1/14   # Recovery rate for quarantined
    beta_s = 1/2     # Disease transmission rate for susceptible
    beta_v = 1/4     # Disease transmission rate for vaccinated
    rho = 1/14       # Isolation / Quarantine rate
    sigma_e = 1/5    # Exposed to Infected Rate
    sigma_q = 1/365  # Immunity loss rate
    tau = 1/3        # Vaccination rate
    mu = 1/29200     # Natural death rate

    # Initialization
    S[0] = 0.999
    I[0] = 0.001
    t = 0
    dt = 1

    # Loop
    while t < times - dt:
        S[t+dt] = S[t] + (- beta_s * S[t] * I[t] - tau * S[t] + sigma_q * Q[t] - mu * S[t])
        E[t+dt] = E[t] + (beta_s * S[t] * I[t] + beta_v * V[t] * I[t] - sigma_e * E[t] - mu * E[t])
        I[t+dt] = I[t] + (sigma_e * E[t] - alpha_i * I[t] - rho * I[t] - mu * I[t])
        R[t+dt] = R[t] + (alpha_i * I[t] + alpha_q * Q[t] - mu * R[t])
        V[t+dt] = V[t] + (tau * S[t] - beta_v * V[t] * I[t] - mu * V[t])
        Q[t+dt] = Q[t] + (- sigma_q * Q[t] + rho * I[t] - alpha_q * Q[t] - mu * Q[t])

        t += dt

    # Graph plot
    t = list(range(0, times))
    plt.plot(t, S, label='Susceptible')
    plt.plot(t, E, label='Exposed')
    plt.plot(t, I, label='Infectious')
    plt.plot(t, R, label='Recovered')
    plt.plot(t, V, label='Vaccinated')
    plt.plot(t, Q, label='Quarantined')

    # Plot labels and legends
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.xlim(0, 100)
    plt.ylim(0, 1.1)
    plt.legend()

    # Plot show
    plt.show()


if __name__ == '__main__':
    main()

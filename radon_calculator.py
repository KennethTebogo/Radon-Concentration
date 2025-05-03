import math

def calculate_cf(I, F):
    """Calculate calibration factor Cf based on initial and final voltage."""
    V_sum = I + F
    Cf = 0.0459 + (1.5519e-5) * V_sum
    return Cf

def calculate_crn(I, F, T, BG=32):
    """Calculate radon concentration CRn in Bq/m^3."""
    V = I - F
    Cf = calculate_cf(I, F)
    CRn = V / (Cf * T) - BG
    return CRn, V, Cf

def calculate_errors(I, F, CRn):
    """Estimate total uncertainty in percentage."""
    # E1: System component error
    E1 = 5.0
    
    # E2: Error in voltage readings
    delta_V = math.sqrt(1**2 + 1**2)  # 1V uncertainty for I and F
    V = I - F
    E2 = (delta_V / V) * 100

    # E3: Background error
    BG_error = 6  # Bq/m³
    E3 = (BG_error / CRn) * 100 if CRn != 0 else 0

    # Total error
    E_total = math.sqrt(E1**2 + E2**2 + E3**2)
    return E1, E2, E3, E_total

# Example data
I = 708  # Initial voltage (V)
F = 640  # Final voltage (V)
T = 7    # Exposure time in days

# Compute radon concentration
CRn, V, Cf = calculate_crn(I, F, T)
E1, E2, E3, E_total = calculate_errors(I, F, CRn)

# Display results
print("Initial Voltage (V):", I)
print("Final Voltage (V):", F)
print("Exposure Time (days):", T)
print("Voltage Drop (V):", V)
print("Calibration Factor (Cf):", round(Cf, 5))
print("Radon Concentration (Bq/m³):", round(CRn, 2))
print("\n--- Error Estimates ---")
print(f"System Component Error (E1): {E1:.2f}%")
print(f"Voltage Reading Error (E2): {E2:.2f}%")
print(f"Gamma Background Error (E3): {E3:.2f}%")
print(f"Total Estimated Error: {E_total:.2f}%")


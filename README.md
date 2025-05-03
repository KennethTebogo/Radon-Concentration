
# 🧪 Radon Concentration Calculator (E-PERM Method)

This Python script calculates radon concentration in indoor air using E-PERM electret ion chambers. It also provides a detailed uncertainty analysis, accounting for system errors, voltage reading errors, and background radiation.

## 📈 Features

- Computes radon concentration (in Bq/m³) based on:
  - Initial and final electret voltages
  - Exposure time
  - Calibration factor
  - Background gamma radiation
- Calculates error contributions:
  - System error (E₁)
  - Voltage reading error (E₂)
  - Background correction error (E₃)
  - Total combined uncertainty
- Fully documented and easy to modify

## 🧮 Formula Used

**Radon concentration (CRn):**
```
CRn = (I - F) / (Cf × T) - BG
```
Where:
- `I` = Initial voltage (V)
- `F` = Final voltage (V)
- `T` = Time in days
- `Cf` = Calibration factor, computed as `Cf = 0.0459 + 1.5519 × 10⁻⁵ × (I + F)`
- `BG` = Background gamma radiation (default 32 Bq/m³)

## ❗ Error Estimation

Total uncertainty is calculated from:

- **E₁:** System error = 5%
- **E₂:** Error in voltage readings (±1 V for both I and F)
- **E₃:** Background gamma correction uncertainty (default ±6 Bq/m³)

Combined using:
```
E_total = √(E1² + E2² + E3²)
```

## 🛠️ Usage

### Requirements

- Python 3.x

### Run the script

```bash
python radon_calculator.py
```

You can modify the example values in the script:

```python
I = 708  # Initial voltage in volts
F = 640  # Final voltage in volts
T = 7    # Exposure time in days
```

## 📜 Example Output

```
Initial Voltage (V): 708
Final Voltage (V): 640
Exposure Time (days): 7
Voltage Drop (V): 68
Calibration Factor (Cf): 0.05678
Radon Concentration (Bq/m³): 70.65

--- Error Estimates ---
System Component Error (E1): 5.00%
Voltage Reading Error (E2): 2.06%
Gamma Background Error (E3): 8.49%
Total Estimated Error: 9.98%
```

## 📁 Project Structure

```
├── radon_calculator.py     # Main Python script
├── README.md               # Project documentation
```

## 🔍 References

- **E-PERM® Electret Ion Chamber Technology**, Rad Elec Inc.
- Background gamma radiation values based on regional studies (default: 32 Bq/m³)
- Calibration curve derived from empirical constants

## 📃 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

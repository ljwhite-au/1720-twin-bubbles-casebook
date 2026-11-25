#!/usr/bin/env python3
"""
The 1720 Twin Bubbles (Part II — London): South Sea Surplus-Stock Arbitrage,
Green Book Option Payoffs, £11M Loan Collateral Breach & 33-Estate Clawback Audit.
MIT License | Open Forensic Accounting Lab
"""
import os
import pandas as pd

def resolve_csv_path(filename: str) -> str:
    for p in [os.path.join("data", filename), filename, os.path.join("..", "data", filename)]:
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"Could not locate {filename}")

def run_london_audit():
    df_l = pd.read_csv(resolve_csv_path("south_sea_1720_timeline_prices.csv"))
    df_e = pd.read_csv(resolve_csv_path("south_sea_33_director_estates_1721.csv"))

    print("=== PART II (LONDON, 1711-1723): SOUTH SEA BUBBLE FORENSIC AUDIT ===")
    stat_cap = 90 * 14
    issued = 350
    surplus = stat_cap - issued
    print(f"Short-Annuity (£90 p.a.) Statutory Cap (14 yrs): £{stat_cap:,.2f} | Issued: £{issued:,.2f} | Surplus Stock: £{surplus:,.2f} ({surplus/issued:.2f}x)")
    print(f"  Surplus Market Value @ 375%: £{surplus*3.75:,.2f} gross (Net less £217.50 cash: £{surplus*3.75-217.50:,.2f}) | @ 890%: £{surplus*8.90:,.2f}")

    subs = [(2250000, 3.0, 3.0), (1500000, 4.0, 4.0), (5000000, 10.0, 4.0), (1250000, 10.0, 4.0)]
    init_ob = sum(n * p for n, p, _ in subs)
    adj_ob = sum(n * a for n, _, a in subs)
    relief = adj_ob - init_ob
    print(f"Four Money Subs (£10M nom.): Initial £{init_ob:,.2f} -> Post-20 Sept £{adj_ob:,.2f} (Relief: £{relief:,.2f}, {relief/init_ob*100:.2f}%)")

    pool_a = 574500.0
    print(f"Green Book Pool A (£{pool_a:,.0f} @ 135%): Payoff @ £375 = £{pool_a*(375-135)/100:,.2f} | @ £890 = £{pool_a*(890-135)/100:,.2f} | @ £1,050 = £{pool_a*(1050-135)/100:,.2f}")

    loans = 11000000.0
    pledged_nom = (loans / 500.0) * 100.0
    print("\n--- £11,000,000 Stock & Receipt Loan Collateral Breach Test ---")
    for dt, spot in [("1720-06-25", 1050), ("1720-08-22", 820), ("1720-09-15", 520), ("1720-09-20", 410), ("1720-10-14", 170)]:
        collat = pledged_nom * (spot / 100.0)
        ltv = loans / collat * 100.0
        diff = collat - loans
        status = "COVERED" if diff >= 0 else "COLLATERAL BREACH"
        print(f"  {dt} @ £{spot:4d}: Collateral £{collat:11,.0f} | LTV {ltv:6.2f}% | Cushion/(Deficit) £{diff:+11,.0f} | {status}")

    gross = df_e["sworn_estate_gbp"].sum()
    allow = df_e["allowance_gbp"].sum()
    net = df_e["net_confiscated_gbp"].sum()
    blunt_adj = gross - 9000.50
    print("\n--- 1721 Statutory Director & Officer Clawbacks (7 Geo. I c. 28) ---")
    print(f"33 Estates (Noorthouck): Gross £{gross:,.2f} | Allowances £{allow:,.2f} | Net Confiscated £{net:,.2f} ({net/gross*100:.2f}%)")
    print(f"Blunt-Adjusted Gross (Surman -£9,000.50): £{blunt_adj:,.2f} vs 1911 Britannica £2,014,123.00 (Diff: £{blunt_adj-2014123:,.2f})")

if __name__ == "__main__":
    run_london_audit()

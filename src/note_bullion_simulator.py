#!/usr/bin/env python3
"""
The 1720 Twin Bubbles (Part I — Paris): Banque Royale Monetary Overhang,
9,000-Livre Equity Peg Stress Test & 1721 Commission du Visa Simulator.
MIT License | Open Forensic Accounting Lab
"""
import os
import pandas as pd

def resolve_csv_path(filename: str) -> str:
    for p in [os.path.join("data", filename), filename, os.path.join("..", "data", filename)]:
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"Could not locate {filename}")

def run_paris_audit():
    df = pd.read_csv(resolve_csv_path("banque_royale_issuance_1716_1720.csv"))
    tranches = df[df["phase"].isin(["Occident", "Filles", "Petites-Filles", "Soumissions", "Final Creation"])]
    total_shares = int(tranches["share_tranche_count"].sum())
    total_par = total_shares * 500
    gross_raised = float(tranches["tranche_gross_capital_livres"].sum())
    share_premium = gross_raised - total_par
    peak_cap_600k = 600000 * 20000
    hurdle_5pct = peak_cap_600k * 0.05
    coin_stock = 1300000000.0
    gross_notes = 2696400000.0
    retired_notes = 707327460.0
    net_notes = gross_notes - retired_notes

    print("=== PART I (PARIS, 1716-1721): JOHN LAW'S SYSTEME FORENSIC AUDIT ===")
    print(f"Total Compagnie des Indes Shares:  {total_shares:>14,} shares (600k core + 24k Oct 4)")
    print(f"Total Par Capital (@ 500L):        {total_par:>14,.0f} livres")
    print(f"Gross Share Capital Raised:        {gross_raised:>14,.0f} livres ({share_premium/gross_raised*100:.2f}% premium)")
    print(f"Dec 1719 Peak Mkt Cap (600k core): {peak_cap_600k:>14,.0f} livres (1.00% cash dividend yield)")
    print(f"5% Market Yield Revenue Hurdle:    {hurdle_5pct:>14,.0f} livres/yr ({hurdle_5pct/coin_stock*100:.2f}% of France coin stock)")
    print(f"Gross Banque Royale Notes (May 3): {gross_notes:>14,.0f} livres ({gross_notes/coin_stock:.2f}x coin stock; {coin_stock/gross_notes*100:.2f}% cover)")
    print(f"Net Unretired Notes:               {net_notes:>14,.0f} livres ({net_notes/coin_stock:.2f}x coin stock)")
    print("\n--- 5 March 1720 9,000-Livre Equity Put Window Stress Test ---")
    for pct in [0.10, 0.25, 0.50, 0.75, 1.00]:
        sh = total_shares * pct
        req_notes = sh * 9000
        mult = req_notes / coin_stock
        status = "BREACH (>1x COIN)" if mult > 1.0 else "BELOW 1x COIN"
        print(f"  {pct*100:5.0f}% Put ({sh:9,.0f} sh): {req_notes:15,.0f} L | {mult:4.2f}x coin stock | {status}")
    print("\n--- 1721 Commission du Visa Sensitivity (48M L/yr Interest Ceiling vs 2,222,597,491 L Claims) ---")
    gross_claims = 2222597491.0
    for r in [0.03, 0.035, 0.04]:
        surv = 48000000.0 / r
        haircut = gross_claims - surv
        print(f"  Rate {r*100:4.1f}% -> Surviving Principal: {surv:15,.0f} L | Haircut: {haircut:14,.0f} L ({haircut/gross_claims*100:.2f}%)")

if __name__ == "__main__":
    run_paris_audit()

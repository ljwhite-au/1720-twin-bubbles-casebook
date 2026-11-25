# The 1720 Twin Bubbles: John Law's *Système* & The South Sea Bubble

**Open Forensic Accounting & Monetary Stress Lab** | *Paris (1716–1721) & London (1711–1723)*

A complete, free, open-access dual-theatre forensic accounting reconstruction of the concurrent 1720 sovereign debt-for-equity bubbles in Paris (*Banque Royale* / *Compagnie des Indes*) and London (*South Sea Company* / *Sword Blade Bank*), built strictly from pre-1923 public-domain primary sources.

## What This Casebook Shows (Key Findings)

This comparative forensic lab demonstrates how two concurrent 1720 sovereign debt-for-equity bubbles built on the same post-war debt-swap blueprint broke through **opposite sides of the balance sheet**:

1. **Paris — Monetary-Equity Fusion & The Unfunded 9,000-*Livre* Put Trap:** After creating **624,000 *Compagnie des Indes* shares** (raising **1,689.5M *livres***, 81.53% as share premium) and peaking at **20,000 *livres*** in December 1719 (**1.00%** cash dividend yield; a 5% market return required **600M *livres*/year** — **46.15%** of France's entire **1.3B *livre*** coin stock), John Law merged the *Banque Royale* with the Company (22 Feb 1720) and pegged shares at **9,000 *livres*** payable in banknotes (5 Mar 1720). That turned equity selling directly into fiat printing: gross notes hit **2,696.4M *livres*** (**2.07x** national coin), while a 100% share put carried a **5,616M *livre*** ceiling (**4.32x** coin). Eyewitness lawyer **Edmond Barbier** recorded how the 21 May 50% devaluation decree shattered confidence and how Bank Treasurer Bourgeois refused commissioners Fagon and Trudaine a physical count of the gold bags in July 1720.
2. **London — Surplus-Stock Arbitrage, Circular Vendor Lending & Insider Call Options:** Because the Bank of England stayed independent, South Sea directors outbid it (**£7,567,500** vs. **£5,547,600**, +36.41%) and engineered equity demand through three internal mechanisms: (a) **2.60x Surplus Stock arbitrage** on Short Annuities (£1,260 statutory authorization vs. £350 issued per £90 p.a. annuity); (b) **£75.25M** in leveraged Money Subscriptions (slashed by **-£37.50M** on 20 Sept 1720) paired with **£11,000,000** in circular loans against Company shares and receipts that breached collateral below **£500/share** (reaching **-£7.26M** deficit / **294.12% LTV** at £170 on 14 Oct); and (c) **£574,500** in Cashier Robert Knight's secret "Green Book" zero-cash political call options (**£5.26M** peak spread at £1,050) alongside **£936,000** in Pool B allocations.
3. **Opposite Post-Crash Legal Workouts:** France ran an administrative sovereign-creditor haircut—the 1721 *Commission du Visa* audited **511,009 claims** totaling **2,222,597,491 *livres*** down to a **48M *livres*/year** state interest cap (**28.0%–46.0%** implied macro haircut at 3%–4% capitalization rates). Great Britain upheld executed debt contracts (**259–117** Commons vote) and instead stripped the personal estates of 33 directors and officers under *7 Geo. I c. 28*—recovering **£1,668,523.88** (**82.47%**) out of **£2,023,123.88** gross inventories, with statutory allowances matching *1911 Britannica*'s **£354,600.00** to the exact penny and isolating Robert Surman's **-£9,000.50** print transposition between Blunt (1722) and Noorthouck (1773).


---

## Repository Structure

```text
1720-twin-bubbles/
├── README.md                                  # Overview, Key Findings, setup & legal notices
├── LICENSE-PROSE.txt                          # CC BY-NC-SA 4.0 (narrative, PDF, SVGs & workbooks)
├── LICENSE-CODE.txt                           # MIT License (Python scripts, CSVs & notebook code)
├── .gitignore                                 # Excludes OS and Python/Excel cache files
├── casebook.md                                # Complete 6-section forensic monograph & 6 lab exercises
├── 1720_Twin_Bubbles_Casebook.pdf             # Standalone formatted PDF reading & seminar edition
├── instructor_debrief.md                      # 100-point grading rubric, pitfalls & 120-min seminar plan
├── 1720_Twin_Bubbles_Lab.ipynb                # Interactive Jupyter notebook (Paris + London labs)
├── data/
│   ├── banque_royale_issuance_1716_1720.csv   # 17 verified Paris chronological records (1716–1721)
│   ├── south_sea_1720_timeline_prices.csv     # 16 verified London chronological records (1711–1723)
│   ├── south_sea_33_director_estates_1721.csv # Complete 33-estate statutory clawback ledger (7 Geo. I c. 28)
│   └── sources_index.md                       # Pre-1923 bibliography & transparent [PENDING ARCHIVE] log
├── src/
│   ├── note_bullion_simulator.py              # Part I Paris dilution, 9,000L peg & Visa sensitivity script
│   └── surplus_stock_audit.py                 # Part II London surplus stock, Green Book & 33-estate script
├── assets/
│   ├── mississippi_credit_loop.svg            # Vector schematic: Paris debt swap -> 9,000L peg -> Visa
│   ├── south_sea_credit_loop.svg              # Vector schematic: London surplus stock -> Green Book -> Clawbacks
│   ├── chart_1_paris_dilution_and_peg.png     # 300-DPI Paris monetary overhang & 9,000L put drain
│   ├── chart_2_paris_visa_sensitivity.png     # 300-DPI 1721 Visa sensitivity & provenance desk audit
│   ├── chart_3_london_subs_and_green_book.png # 300-DPI Money Sub -£37.5M relief & Green Book payoffs
│   └── chart_4_london_loan_and_clawbacks.png  # 300-DPI £11M loan breach & top 10 director estates
└── workbook/
    ├── 1720_twin_bubbles_challenge.xlsx       # 8-tab blank-input learner challenge workbook
    └── 1720_twin_bubbles_solution_key.xlsx    # Worked 8-tab live-formula solution workbook (367 formulas, 4 charts)
```

---

## Quick Start (Verify Locally, in Excel/Sheets, or in Jupyter)

1. **Run both automated MIT-licensed forensic audit scripts:**
   ```bash
   python3 src/note_bullion_simulator.py
   python3 src/surplus_stock_audit.py
   ```
2. **Explore in Jupyter:** Open `1720_Twin_Bubbles_Lab.ipynb` to inspect all three CSVs and reproduce the Paris and London audit checks.
3. **Work through or inspect the 8-tab Excel workbooks:**
   * Open `workbook/1720_twin_bubbles_challenge.xlsx` to complete the amber-shaded input cells across Labs 1–6 (Tabs 0–6).
   * Open `workbook/1720_twin_bubbles_solution_key.xlsx` in Excel, LibreOffice Calc, or Google Sheets to inspect all 367 live formulas, cross-sheet links, and 4 embedded charts.

---

## Licensing & Australian Legal Notices

### 1. Dual Open License
* **Prose, PDF, Diagrams & Workbook Layouts (`LICENSE-PROSE.txt`):** Licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**. Free to read, share, teach from, and adapt non-commercially with attribution; third-party resale is prohibited.
* **Code & Structured CSV Data (`LICENSE-CODE.txt`):** Licensed under the **MIT License**. Free to use, modify, and integrate `src/*.py`, `data/*.csv`, and the Python code cells in `1720_Twin_Bubbles_Lab.ipynb`.

### 2. Educational Purpose & Non-Advice Disclaimer
This casebook, its spreadsheets, and its Python scripts are **historical forensic accounting exercises prepared solely for educational, training, and academic research purposes**. Nothing in this repository constitutes legal, audit, tax, or financial advice.

### 3. Australian Consumer Law Qualification
To the maximum extent permitted by law (including Schedule 2 of the *Competition and Consumer Act 2010* (Cth) — the **Australian Consumer Law**), these materials are provided on an educational reference basis without warranty as to completeness for any specific purpose. Nothing in these notices excludes, restricts, or modifies any right or remedy conferred by the Australian Consumer Law that cannot lawfully be excluded.

### 4. Archival Transparency & Historical Clearance
* **Primary-Source Discipline:** Every figure is transcribed from pre-1923 public-domain decrees, UK statutes, parliamentary proceedings, contemporary eyewitness journals (Edmond Barbier, 1720), and treatises (Steuart 1767, Smith 1776, Noorthouck 1773, Wood 1824, Francis 1847, Moran 1863, Sumner 1896, Conant 1915, *1911 Britannica*). Unretrieved sub-lines or OCR uncertainties are explicitly flagged `[PENDING ARCHIVE]`, `[VERIFY OCR DIGIT]`, or `[VARIANCE FLAG]`.
* **Public-Domain & Defamation Clearance:** All primary records sit in the public domain, and all named historical figures died in the eighteenth century (clearing defamation risk under s 10 of Victoria's *Defamation Act 2005* and uniform Australian defamation legislation).

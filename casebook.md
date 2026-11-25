# The 1720 Twin Bubbles: John Law's *Système* & The South Sea Bubble

**Open Forensic Accounting & Monetary Stress Lab** | *Paris (1716–1721) & London (1711–1723)*
**Dual License:** Narrative prose, PDF, SVGs & workbook layouts under **CC BY-NC-SA 4.0**; Python audit scripts, CSV datasets & notebook code under **MIT License**.

## What This Casebook Shows (Key Findings)

This comparative forensic lab demonstrates how two concurrent 1720 sovereign debt-for-equity bubbles built on the same post-war debt-swap blueprint broke through **opposite sides of the balance sheet**:

1. **Paris — Monetary-Equity Fusion & The Unfunded 9,000-*Livre* Put Trap:** After creating **624,000 *Compagnie des Indes* shares** (raising **1,689.5M *livres***, 81.53% as share premium) and peaking at **20,000 *livres*** in December 1719 (**1.00%** cash dividend yield; a 5% market return required **600M *livres*/year** — **46.15%** of France's entire **1.3B *livre*** coin stock), John Law merged the *Banque Royale* with the Company (22 Feb 1720) and pegged shares at **9,000 *livres*** payable in banknotes (5 Mar 1720). That turned equity selling directly into fiat printing: gross notes hit **2,696.4M *livres*** (**2.07x** national coin), while a 100% share put carried a **5,616M *livre*** ceiling (**4.32x** coin). Eyewitness lawyer **Edmond Barbier** recorded how the 21 May 50% devaluation decree shattered confidence and how Bank Treasurer Bourgeois refused commissioners Fagon and Trudaine a physical count of the gold bags in July 1720.
2. **London — Surplus-Stock Arbitrage, Circular Vendor Lending & Insider Call Options:** Because the Bank of England stayed independent, South Sea directors outbid it (**£7,567,500** vs. **£5,547,600**, +36.41%) and engineered equity demand through three internal mechanisms: (a) **2.60x Surplus Stock arbitrage** on Short Annuities (£1,260 statutory authorization vs. £350 issued per £90 p.a. annuity); (b) **£75.25M** in leveraged Money Subscriptions (slashed by **-£37.50M** on 20 Sept 1720) paired with **£11,000,000** in circular loans against Company shares and receipts that breached collateral below **£500/share** (reaching **-£7.26M** deficit / **294.12% LTV** at £170 on 14 Oct); and (c) **£574,500** in Cashier Robert Knight's secret "Green Book" zero-cash political call options (**£5.26M** peak spread at £1,050) alongside **£936,000** in Pool B allocations.
3. **Opposite Post-Crash Legal Workouts:** France ran an administrative sovereign-creditor haircut—the 1721 *Commission du Visa* audited **511,009 claims** totaling **2,222,597,491 *livres*** down to a **48M *livres*/year** state interest cap (**28.0%–46.0%** implied macro haircut at 3%–4% capitalization rates). Great Britain upheld executed debt contracts (**259–117** Commons vote) and instead stripped the personal estates of 33 directors and officers under *7 Geo. I c. 28*—recovering **£1,668,523.88** (**82.47%**) out of **£2,023,123.88** gross inventories, with statutory allowances matching *1911 Britannica*'s **£354,600.00** to the exact penny and isolating Robert Surman's **-£9,000.50** print transposition between Blunt (1722) and Noorthouck (1773).


---

## Section 1. Prologue — The Post-War Sovereign Debt Engine
When the War of the Spanish Succession ended in 1713–1714, both France (~1.5B–1.6B *livres* in legacy Crown debts) and Great Britain (~£30.98M in redeemable debts and 96-/99-year irredeemable annuities) sought to refinance expensive war obligations without formal default. Both capitals deployed the same **sovereign debt-for-equity swap**, exchanging depressed or illiquid government obligations for chartered monopoly shares—yet broke through opposite mechanisms: **monetary-equity fusion** in Paris versus **corporate credit loops and insider call options** in London.

### Unified Anglo-French Forensic Glossary
* ***Livres tournois* / *Actions*:** French unit of account / corporate equity shares (*mères*, *filles*, *petites-filles*, *soumissions*).
* ***Billets d'État* vs. *Billets de banque*:** Discounted war-debt notes swapped into shares vs. *Banque Royale* paper currency notes.
* ***Arrêts* & *Commission du Visa*:** Royal Council financial decrees & the January 1721 state audit tribunal (511,009 filings).
* ***Surplus Stock* (*6 Geo. I c. 4*):** Authorized share capital retained by the South Sea Company whenever rising stock prices reduced shares needed to retire fixed par debt.
* ***Green Ledger* ("Taken-in" Stock):** Secret book recording £574,500 in fictitious stock allocations with blank/coded buyer names and zero cash paid in.
* ***Scire Facias* (*6 Geo. I c. 18*):** Judicial writ challenging corporate charter misuse; August 1720 writs against rival bubbles triggered cross-margin liquidation across Exchange Alley.

---

## Section 2. Part I (Paris, 1716–1719) — Sovereign Swaps & Capital Dilution (Lab 1)
**Workbook Tab:** `1_Paris_Debt_Swap_T_Accounts` | **Data:** `data/banque_royale_issuance_1716_1720.csv`

John Law chartered ***Banque Générale*** on **2 May 1716** (6,000,000 *livres* capital: 25% specie, 75% *billets d'État*; fixed-weight coin convertibility) and ***Compagnie d'Occident*** in **August 1717** (200,000 *mères* @ 500 *livres* = 100M *livres*; 3% Crown annuity = 3M/yr; `[VARIANCE FLAG]` on 25% coin/75% *billets* vs. 100% *billets*). On **4 December 1718**, the Regency nationalized *Banque Générale* into ***Banque Royale***, stripping away private specie discipline.

Between June and October 1719, the renamed ***Compagnie des Indes*** absorbed the Royal Mint (50M *livres*) and tax farms (*Fermes générales*), assumed **1.5B *livres*** of Crown debt at 3% (rising to 1.6B by Feb 1720), and issued **624,000 total shares**: 200,000 *mères* (500L), 50,000 *filles* (550L), 50,000 *petites-filles* (1,000L), 300,000 *soumissions* (5,000L, 10% down), and 24,000 final shares on 4 Oct 1719 (500L)—raising **1,689,500,000 *livres*** (**312M** par + **1,377.5M** share premium, 81.53%). At the **December 1719** peak of **20,000 *livres*/share** (**12.0B *livres*** core market cap on 600k shares), the promised 40% par dividend (200L/sh) delivered just a **1.00%** cash yield; a 5% market return required **600,000,000 *livres*/year**—**46.15%** of France's entire **1.3B *livre*** coin stock (Crown 3% interest of 45M/yr covered only **7.50%**).

**Graded Exercise 1 (15 Points):** Complete `1_Paris_Debt_Swap_T_Accounts` (`F6:H10`, `C11`, `E11:H11`, `C15:C23`, `F27:F29`).

---

## Section 3. Part I (Paris, 1720–1721) — The 9,000-*Livre* Peg, Eyewitness Collapse & 1721 *Visa* (Labs 2–3)
**Workbook Tabs:** `2_Paris_Note_Issuance_Peg` & `3_Paris_1721_Visa_Haircuts` | **Script:** `src/note_bullion_simulator.py`

On **22 February 1720**, *Banque Royale* merged with *Compagnie des Indes*. On **5 March 1720**, the Regency pegged shares at **9,000 *livres*** freely convertible into banknotes. Gross notes reached **2,696,400,000 *livres*** by 3 May 1720 (**2.07x** France's 1.3B coin stock; **48.21%** theoretical cover; **1,989.1M *livres*** net of 707.3M retired), while a 100% share put carried a **5,616,000,000 *livre*** ceiling (**4.32x** coin stock).

> **Eyewitness Audit Note — Edmond-Jean-François Barbier's *Journal* (Paris, May–October 1720):** Contemporary Paris lawyer Edmond Barbier recorded the collapse on the ground: after the **21 May 1720** *arrêt* cut notes and shares by 50% (revoked **27 May** under Parlementary pressure), shares crashed to **4,000 *livres***, crowds were suffocated outside the Bank waiting for 100-*livre* payouts, and in **July 1720** when Council commissioners **Fagon** and **Trudaine** inspected the Bank vaults and demanded to count the stacked gold bags on a table, Treasurer **Bourgeois** refused—telling them *"il falloit avoir de la foi"* ("one must have faith")—leading to both inspectors' dismissal. By **12 October 1720**, after the 10 October demonetization decree, a 100-*livre* banknote traded for just **19 *livres*** in coin.

In **January 1721**, the Pâris brothers' ***Commission du Visa*** audited **511,009 declarations** totaling **2,222,597,491 *livres*** (average **4,349.43 *livres*/claim**) and capped post-*Visa* Crown interest at **48,000,000 *livres*/year** (Moran 1863)—implying surviving principal of **1.60B L** (28.01% haircut) at 3.0%, **1.37B L** (38.30%) at 3.5%, or **1.20B L** (46.01%) at 4.0% (Wood 1824's surviving-principal OCR string `1,676,5015831` remains tagged `[VERIFY OCR DIGIT]`).

**Graded Exercises 2 & 3 (30 Points):** Complete `2_Paris_Note_Issuance_Peg` (`D6:F9`, `C10:F12`, `C14`, `C18:G22`, `C27:C31`) and `3_Paris_1721_Visa_Haircuts` (`B8`, `C14:E16`, `C20:C23`, `F20:G23`), then verify against `python3 src/note_bullion_simulator.py`.

---

## Section 4. Part II (London, 1711–1720) — Surplus Stock & Money Subscriptions (Lab 4)
**Workbook Tab:** `4_London_Surplus_Stock` | **Data:** `data/south_sea_1720_timeline_prices.csv`

Chartered in **September 1711** (*9 Anne c. 21*; ~£9.18M war debt @ 6%), the South Sea Company won the **April 1720** *South Sea Act* (*6 Geo. I c. 4*; ~£30.98M target debt pool) by bidding **£7,567,500** against the Bank of England's **£5,547,600** (+£2,019,900 / +36.41%). Because Parliament authorized new stock based on **par debt converted** rather than shares issued, inflating the conversion price generated massive **Surplus Stock**: on **19 May 1720** (@ 375%), each **£90 p.a. Short Annuity** authorized **£1,260** par stock (14 years' purchase) but paid the annuitant only **£350** stock + **£217 10s.** cash/bonds, leaving **£910.00 Surplus Stock (2.60x)** worth **£3,412.50** gross (**£3,195.00** net) at 375% and **£8,099.00** at £890.

Between April and August 1720, directors launched **Four Money Subscriptions** totaling **£10,000,000 nominal** (**£75,250,000** initial gross commitments: £6.75M @ 300%, £6.00M @ 400%, £50.00M @ 1,000% on 10% down, and £12.50M @ 1,000% on 20% down). On **20 September 1720**, with spot down to **£410**, the General Court slashed the 3rd and 4th Subscriptions from 1,000% to 400%—wiping **-£37,500,000 (-49.83%)** off investor obligations.

**Graded Exercise 4 (15 Points):** Complete `4_London_Surplus_Stock` (`D7`, `E10`, `G10`, `D14:G18`, `B21:B25`, `C33:D33`, `F29:H34`).

---

## Section 5. Part II (London, 1720–1723) — Green Ledger Bribes, £11M Loans & 33-Estate Clawbacks (Labs 5–6)
**Workbook Tabs:** `5_London_Green_Ledger_Credit` & `6_London_Director_Clawbacks` | **Script:** `src/surplus_stock_audit.py`

To secure parliamentary passage, Cashier **Robert Knight** recorded **£574,500** in fictitious pre-Act "taken-in" stock (**Pool A**: £170,000 itemized across Sunderland, Sword Blade Company, Craggs, Duchess of Kendal, Countess of Platen & nieces, and Charles Stanhope; £404,500 `[PENDING ARCHIVE]`) operating as zero-cash call options worth **£5,256,675** at the £1,050 peak, plus **£936,000** in **Pool B** allocations (Craggs Sr. £659k, Sunderland £160k, Aislabie £70k, Stanhope £47k) and Sir George Caswall's £250,000 Sword Blade refund.

Simultaneously, the Company lent **£11,000,000** against its own stock and receipts (at a benchmark £500/share advance = £2.2M nominal pledged). After the **June 1720 Bubble Act** (*6 Geo. I c. 18*) and **August *scire facias* writs** triggered cross-margin liquidations, spot plunged below £500—breaching collateral at **£410** (20 Sept: **-£1.98M** deficit, **121.95% LTV**) and **£170** (14 Oct: **-£7.26M** deficit, **294.12% LTV**, 66.00% impairment).

After Knight fled to Brabant (23 Jan 1721), Parliament voted **259–117** to uphold executed debt contracts, restructured capital into 4% annuities (*9 Geo. I c. 6*, 1723), and enacted the ***South Sea Sufferers Act* (*7 Geo. I c. 28*, 1721)** confiscating **£1,668,523.88 (82.47%)** across **33 director and officer estates** (**£2,023,123.88** gross Noorthouck/Francis inventories less **£354,600.00** exact parliamentary allowances—reconciling to *1911 Britannica*'s £2,014,123 gross via Robert Surman's **-£9,000.50** Blunt 1722 print transposition).

**Graded Exercises 5 & 6 (30 Points):** Complete `5_London_Green_Ledger_Credit` (`D6:G13`, `B14:F15`, `B23`, `E29:H36`) and `6_London_Director_Clawbacks` (`F6:G38`, `D39:G39`, `D44:G46`), then verify against `python3 src/surplus_stock_audit.py`.

---

## Section 6. Cross-Channel Synthesis & Modern Audit Crosswalk
See Tab `7_Twin_Bubbles_Crosswalk` for the full structural matrix comparing Paris vs. London and mapping all five 1720 red flags to modern **IAS 32**, **IFRS 2**, **IAS 24**, **ISA / ASA 240**, **Basel III LCR**, and **IFRS 9 ECL** controls.

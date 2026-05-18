# Global Electricity Mix Dashboard

*This dashboard is in progress. It runs locally. Live hosting and screenshot are pending. See Next Steps for planned additions.*

## Project Overview

The global energy transition is widely covered in the news, often focusing on renewable growth and progress. This dashboard examines what the data actually shows about that progress — where it is real and significant, where it is overstated, and what the narrative leaves out.

The analysis uses Our World in Data's energy dataset to explore how electricity generation has decarbonized globally between 2000 and 2024, how this compares to the broader energy system (transport, heating, industry, agriculture), and how the choice of fuel being replaced affects the climate impact of that transition.

The dashboard was built as an HTML artifact, initially prototyped in Claude Code and refined iteratively across the energy story, chart selection, color scheme, and layout. The goal was to clearly show the global energy mix over time.


**Dashboard:** _[link to live HTML dashboard — TODO]_
**Screenshot:** _[images/dashboard_preview.png — TODO]_

---

## Questions the Dashboard Answers

1. **How fast is electricity decarbonizing globally?**
   Renewable share of global electricity generation grew from roughly 19% in 2000 to 32% in 2024, with solar and wind providing most of the recent gains.

2. **How does the electricity transition compare to the total energy transition?**
   Electricity is only about 20% of total primary energy (per OWID 2024 data). The remaining 80% (industrial heat, transport, heating, agriculture) has not seen the same gains. The IPCC's AR6 Synthesis Report (2023) identifies these hard-to-electrify sectors as the current priority bottleneck for meeting climate targets.

3. **Within electricity, does the choice of fuel being replaced matter for climate impact?**
   The carbon-intensity view surfaces how emissions intensity varies across countries and fuel mixes, providing context for interpreting where renewable replacement may have the largest impact. Specific magnitudes depend on lifecycle emissions assumptions and local grid conditions.

4. **Which countries are leading the renewable transition?**
   The geographic and country-comparison views surface country-level leaders and laggards on both electricity and total-energy renewable share.

---

## Approach

The project used a three-stage approach: data preparation is done in a Jupyter notebook, then dashboard development using Claude Code, and finally iterative design refinement also using Claude Code.

1. **Data Preparation** — Filter, validate, and enrich the OWID dataset; export a 2,000-row dashboard-ready subset (79 countries + World × 2000–2024).

2. **Dashboard Development** — Prototype dashboard design and build in Claude Code as a self-contained HTML artifact.

3. **Design Refinement** — Iterate on each chart, color choice, and layout decision to answer specific questions and clearly convey the message.

---

## Results

The final dashboard has nine visualizations organized to follow the story arc:

**KPI row** — Five metrics covering renewable share of electricity, breakdowns by source (solar, wind, hydro), with a fifth card showing renewable share of total energy for comparison.

**Geographic view** — Choropleth map of renewable share by country. A selector allows filtering by all renewables, solar, wind, hydro, or nuclear metrics.

**Time-series views** — Two stacked area charts showing electricity mix and total energy mix from 2000 to 2024.

**Country comparison** — Bar chart of electricity mix by source, filtered by selected country.

**Carbon intensity view** — Scatter plot of carbon intensity vs renewable share for all countries in 2024, colored by coal share to surface variation across the global fuel mix.

**Closing comparison** — Two pie charts comparing the 2024 electricity mix to the 2024 total energy mix.

**Story and methodology** — Text block summarizing the three findings, the IPCC reference, and methodology notes.

---

## Limitations

- The dashboard reflects 79 countries with complete reporting on five anchor share metrics across 2000–2024.
- Smaller countries with incomplete coverage are excluded, which means the dashboard represents countries with consistent reporting.
- 2024 data reflects approximately 10% missing country reporting in the OWID release used (199 of 220 countries).
- 2025 data is excluded due to incomplete reporting (~40% of countries).
- Sector-level energy share columns (`*_share_energy`) are uniformly ~64% null in the source data. Only the five anchor share metrics are usable for cross-country comparison.
- "Renewable" follows OWID's classification (hydro, solar, wind, biofuels, geothermal/other). Nuclear is treated separately, not as renewable.
- Primary energy figures use the substitution method, the current OWID standard. This adjusts for thermal efficiency losses in fossil generation, producing a smaller (more conservative) electricity-versus-total-energy gap than the older direct equivalent method would show.
- The dashboard shows electricity-sector decarbonization and overall energy mix but does not break down total energy by sector (transport, heat, industry). The "hard-to-electrify sectors" claim is supported by IPCC AR6 rather than directly visualized in the dataset.

---

## Next Steps

- Rebuild the dashboard in Tableau or Power BI to demonstrate the same story in standard business BI tools, with different design tradeoffs (interactive depth, conventional dashboard patterns).
- Source sector-level energy data from IEA or Climate TRACE to directly visualize the hard-to-electrify sectors claim rather than relying on the IPCC reference.
- Add a country-level "transition speed" view showing percentage-point change in renewable share over rolling 5-year windows, to surface countries with the fastest transitions independent of their starting position.
- Explore adding emissions data alongside renewable share to show absolute emissions reductions rather than just generation mix changes.

---

## Data

- **Source:** Our World in Data — Energy Dataset (`owid-energy-data.csv`, accessed 2026-04-27). Compiled by OWID from Ember (electricity) and the Energy Institute Statistical Review of World Energy (broader energy).
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Coverage:** Country-level annual data, 2000–2024
- **Records:** 79 countries with complete coverage on five anchor share metrics, plus the World aggregate (2,000 rows in the exported subset)
- **Features used:** Identifiers (country, year, iso_code, continent), share metrics (`renewables_share_elec`, `solar_share_elec`, `wind_share_elec`, `hydro_share_elec`, `nuclear_share_elec`, `coal_share_elec`, `gas_share_elec`, `oil_share_elec`, `biofuel_share_elec`, and corresponding `_energy` columns), and `carbon_intensity_elec`
- **Reference framing:** IPCC AR6 Synthesis Report (2023)

---

## Tech Stack

- Python 3.14
- pandas, numpy
- pycountry-convert
- HTML, CSS, JavaScript
- Chart.js (time-series, bar, pie charts)
- D3.js (choropleth map)
- Jupyter

---

## Repository Structure

```
├── data/
│   ├── owid-energy-data.csv                              # Raw OWID dataset
│   ├── owid-energy-codebook.csv                          # Variable definitions
│   └── processed/
│       └── owid_energy_dashboard_subset.csv              # Dashboard-ready subset
├── notebooks/
│   └── 01_exploratory_analysis.ipynb                     # EDA, filtering, continent enrichment, export
├── dashboard/                                            # HTML/CSS/JS dashboard files
│   ├── index.html
│   ├── styles.css
│   └── js/
├── docs/                                                 # Methodology notes, design decisions
├── images/                                               # README figures
└── README.md
```

---

## Reproducibility

- Python 3.14 environment with pinned dependencies
- Notebook executes end-to-end and rewrites the dashboard subset CSV
- Continent enrichment via `pycountry-convert` is deterministic
- Country allow-list is derived from data coverage, not hand-curated
- Dashboard reads directly from the exported CSV with no further transformation

Reproducing the subset:

    python -m nbconvert --to notebook --execute --inplace \
        notebooks/01_exploratory_analysis.ipynb

---

## References

- Our World in Data — Energy Dataset. https://github.com/owid/energy-data
- IPCC (2023). AR6 Synthesis Report: Climate Change 2023. Intergovernmental Panel on Climate Change. https://www.ipcc.ch/report/ar6/syr/

**Kristi Flowers**
GitHub: [KRFlowers](https://github.com/KRFlowers)

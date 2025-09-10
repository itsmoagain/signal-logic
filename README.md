# Signal Logic

Modular signal detection and enrichment logic for use in scientific software validation pipelines. Includes SPI and NDVI-based anomaly detection used to trigger feedback, enrichment, or verification in climate-aligned systems.

## Purpose
This repository explores ways to make anomaly detection logic reusable and composable for:
- AI/ML-assisted reproducibility checks
- Scientific software validation
- Participatory or decentralized enrichment workflows

## Features
- SPI (Standardized Precipitation Index) calculator
- NDVI anomaly detection from time series
- Trigger logic based on threshold logic or rolling averages
- Jupyter Notebooks for exploration
- Plain-text outputs for pipeline integration

## Structure
- `notebooks/` – example workflows and plots
- `src/` – reusable functions (Python)
- `data/` – small example datasets

## Coming Soon
- More indicators (LST, ESI)
- Comparison of anomaly detection methods
- Reproducibility-oriented validation tests

---

**License**: MIT  
Author: Morgan Urich

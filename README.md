### Grid modeling

This repository contains a research code for islanded grid modeling. An astonishing works insired some ideas deserve to be mentioned.

* Bahta, S. T. [“Design and Analyzing of an Off-Grid Hybrid Renewable Energy System to Supply Electricity for Rural Areas : Case Study: Atsbi District, North Ethiopia.” (2013).](https://www.semanticscholar.org/paper/Design-and-Analyzing-of-an-Off-Grid-Hybrid-Energy-%3A-Bahta/7ee0d392cc4e1a5f97c27ddbd858aa89b67938fc)
* Aemro, Yohannes B.; Moura, Pedro; de Almeida, Aníbal T. 2020. ["Design and Modeling of a Standalone DC-Microgrid for Off-Grid Schools in Rural Areas of Developing Countries" Energies 13, no. 23: 6379.](https://www.mdpi.com/1996-1073/13/23/6379)
* Ibrahim, H. & Ilinca, Adrian & Perron, Jean. (2007). [Comparison and Analysis of Different Energy Storage Techniques Based on their Performance Index. 393 - 398. 10.1109/EPC.2007.4520364.](https://www.researchgate.net/publication/4335860_Comparison_and_Analysis_of_Different_Energy_Storage_Techniques_Based_on_their_Performance_Index)
* Urraca, R.; Huld, T.; Gracia Amillo, A.M.; Martinez-de-Pison, F.J.; Kaspar, F.; Sanz-Garcia, A. 2018. ["Evaluation of global horizontal irradiance estimates from ERA5 and COSMO-REA6 reanalyses using ground and satellite-based data". Solar Energy, 164, 339-354.](https://www.sciencedirect.com/science/article/pii/S0038092X18301920)

And many more. All the research in this field is valueable and should be highly appreciated.

#### Repository content

- **models** - a module contains model objects representing grid components. Currently load.py contains models.Consumer object representing a single household load, storage.py contains models.StorageModel object (Battery system model), pv_model.py contains models.PVModel object, a model of solar arrays system.
- **radiance_analysis.ipynb** - a jupyter notebook with exploratory analysis of solar irradience data for areas of interests (Kherson, Ukraine and Schipkau, Germany)
- **load_analysis.ipynb** - a jupyter notebook with exploratory analysis and grid modeling
- **cost_calculation.ipynb** - a jupyter notebook calculating economic indecies and values
- **[research]solar_radiation_prediction.ipynb** - a jupyter notebook with exploration of machine learning approaches for irradiance forecasting (reserved for future development)

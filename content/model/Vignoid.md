+++
title ='Vignoid'
slug = 'vignoid'
disableComments = true
description = 'A Functional-Structural Plant Model (FSPM) to simulate the interactions between a growing grapevine stock and powdery mildew, from organ to canopy levels, describing severity of the disease and dispersed spores'
image = '/images/icons/4977210_l.png'
numero = 2
+++


<!--# Vignoid-->

### Description

Vignoid is an epidemiological model simulating the growth of a single grapevine stock coupled to the dispersal and disease dynamics of the airborne conidia of powdery mildew pathogen *Erysiphe necator*. 
<div style="align: center; width: 60%">
	
  ![Vignoid_model2.jpg](/images/vignoid/model2.jpg)
	
</div>

- representation of basic model processes with host (grapevine stock) and pathogen (*Erysiphe necator*) developments coupled through the spore's dispersal process and the leaves ontogenic resistance

The model **input variables** are either **climatic** (temperature, wind speed and direction) or related to the **pathogen** (location and onset of primary infection). The environmental **input variables dictate plant growth and pathogen development** (latent period, infection I, colony growth, spore production Q and release Qr). Leave’s susceptibility is function of its age (A) at the time of its infection (ontogenic resistance) and on the amount of spore catched by the infected leaf (Qc).
**Input parameters** characterize the **crop production system** (distance between buds, date and height of shoot topping, and vigour), the **growth conditions** (rate of leaves emergence, rate of leaf growth) and the **epidemiological characteristics of the pathogen**.
Output describe, at each time step, **number, age and pattern of healthy and infected organs, infected and infectious leaf area and density of spores released**. 
1.	Vignoid allows to compare epidemic behavior for various contrasting years of crop development, phenological stages and shows the key effect of the date of initial infection on the level of disease severity at flowering and at the end of the season **(Calonnec et al. 2008)**
2.	The plant vigour has an effect through the production of young susceptible leaves **(Burie et al., 2011)**


### Gallery

* Temporal dynamics of the disease evolution according to the phenological stage at the date of inoculation, for two climatic scenarios. The proportion of diseased leaves at the end of the season is highly dependent on the phenological stage at the time of inoculation and can be very different at flowering time, function of the climatic scenario due to difference of grapevine growth.
<div style="align: center; width: 90%">
	
![Vignoid_temporalLDdynamics.jpg](/images/vignoid/temporalLDdynamics.jpg)
	
</div>


* Temporal dynamics of plant growth (primary, secondary and total leaves)
<div style="align: center; width: 70%">

![Vignoid_temporalLdynamic.jpg](/images/vignoid/temporalLdynamic.jpg)
	
</div>

* Temporal dynamics of the spore produced within the vine and exported
<div style="align: center; width: 80%">

![Vignoid_temporalSporesDynamic.jpg](/images/vignoid/temporalSporesDynamic.jpg)
	
</div>

* Simulation of the interaction between the dispersion parameter *cid* and  distance between shoots *d_buds*, 20 days after shoot topping, for the climatic scenario 2010. Percentages indicate either disease incidence or disease severity (in braskets)
<div style="align: center; width: 60%">

![Vignoid_Vignoid-InterP2P6.jpg](/images/vignoid/Vignoid-InterP2P6.jpg)
	
</div>


### Links

[**Tutorial**](https://hydroshoot.readthedocs.io/en/latest/)

[**Code**](https://github.com/openalea/hydroshoot)


### Scientific publications

- Calonnec A, Cartolaro P, Naulin JM, Bailey D, Langlais M (2008) A host-pathogen simulation model: powdery mildew of grapevine. Plant Pathology 57: 493-508.  [:page_facing_up:](https://doi.org/10.1111/j.1365-3059.2007.01783.x)
- Burie JB, Langlais M, Calonnec A (2011) Switching from a mechanistic model to a continuous model to study at different scales the effect of vine growth on the dynamic of a powdery mildew epidemic. Annals of Botany 107: 885-895.  [:page_facing_up:](https://doi.org/10.1093/aob/mcq233)

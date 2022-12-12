+++
title ='Vignoid'
slug = 'vignoid'
disableComments = true
description = 'A Functional-Structural Plant Model (FSPM) to simulate the interactions between a growing grapevine stock and powdery mildew, from organ to canopy levels, describing severity of the disease and dispersed spores'
image = '/images/icons/4977210_l.png'
numero = 2
+++


<!--# Vignoid-->

### Summary

Vignoid is an epidemiological model simulating the growth of a single grapevine stock coupled to the dispersal and disease dynamics of the airborne conidia of powdery mildew pathogen *Erysiphe necator*. 
![Vignoid_model2](/images/vignoid/model2.jpg)
- representation of basic model processes with host and pathogen devlopments coupled through the spore's dispersal process and the leaves ontogenic resistance

The model **input variables** are either **climatic** (temperature, wind speed and direction) or related to the **pathogen** (location and onset of primary infection). The environmental **input variables dictated plant growth and pathogen development** (latent period, infection I, colony growth, conidial spore production Q and release Qr). Leave’s susceptibility is function of its age (A) at the time of its infection (ontogenic resistance) and on the amount of spore catched (Qc).
**Input parameters** characterized the **crop production system** (distance between buds, date and height of shoot topping, and vigour), the **growth conditions** (rate of leaves emergence, rate of leaves growth) and the **epidemiological characteristics of the pathogen**.
Output described, at each time step, **number, age and pattern of healthy and infected organs, infected and infectious leaf area and density of spores released**. 
1.	Vignoid allowed to compare epidemic behavior for various contrasting years of crop development, phenological stages and showed the key effect of the date of initial infection on the level of disease severity at flowering and at the end of the season **(Calonnec et al. 2008)**
2.	The plant vigour has an effect through the production of young susceptible leaves **(Burie et al., 2011)**


### Gallery

* Temporal dynamics of the disease evolution according to the phenological stage at the date of inoculation, for two climatic scenarios 

![Vignoid_temporalLDdynamic](/images/vignoid/temporalLDdynamics.jpg)

* Temporal dynamics of plant growth (primary, secondary and total leaves) 

![Vignoid_temporalLdynamic](/images/vignoid/temporalLdynamic.jpg)

* Temporal dynamics of the spore produced within the vine and exported

![Vignoid_temporalSporesDynamic](/images/vignoid/temporalSporesDynamic.jpg)

* Simulation of the interaction between the dispersion parameter *cid* and  distance between shoots d_buds for the climatic scenario 2010. Percentage indicate disease incidence or severity in brasket

![Vignoid_VignoidInter-P2P6](/images/vignoid/Vignoid-InterP2P6.jpg)




### Links

[**Tutorial**](https://hydroshoot.readthedocs.io/en/latest/)


[**Code**](https://github.com/openalea/hydroshoot)



### Publications

- Calonnec, A., Cartolaro, P., Naulin, J. M., Bailey, D., Langlais, M. (2008). "A host-pathogen simulation model: powdery mildew of grapevine." Plant Pathology 57: 493-508.
- Burie, J. B., Langlais, M., Calonnec, A.(2011). "Switching from a mechanistic model to a continuous model to study at different scales the effect of vine growth on the dynamic of a powdery mildew epidemic." Annals of Botany 107(5): 885-895.
	



+++
title ='Application Scenario'
slug = 'usecases'
description = 'Use cases'
disableComments = true
image = '/images/window/grape-vine-tunnel-archway-passage-garden-autumn-near-douro-river-portugal-93621530.jpg'
+++

## Coupling models

Here is a basic example of the coupling of two models in the GrapeInSilico framework. 

**Hydroshoot:**
HydroShoot simulates the interactions between shoot hydraulic structure, gas-exchange and energy-budget.  
**Virtual Berry:**
Virtual Berry simulates mass and sugar accumulation in a ripening berry.

## Setup

The relevant scripts are found in the folder */scenarios/hyshoot_vberry/* of the project's [github repository](https://github.com/openalea-incubator/GrapeInSilico). At first one must follow the installation instructions of the GrapeInSilico framework (found in the *README.md* file). Then by running *coupling_sim_vb.py* we get a full 4 day simulation and a graphic of the fresh fruit weight during that period.


## Coupling explanation

The script in *hs_wrapper.py* is a modified version of the file *model.py* of hydroshoot, in order to adapt the function run to a scenario where a grape is added to the plant model. The grape is represented by simply marking a particular internode and computing the local water potential at each time step. Indeed, the signature of the function is changed as to include the vertex number corresponding to the internode where the grape is added (*grape_vid*).

The script in *sim_with_preprocessed_inputs.py* is a modified version of the example "potted_grapevine" of hydroshoot, corresponding to the changes we made in the run function. 

Finally, the script *coupling_sim_vb.py* creates inputs for virtual berry, based on the inputs and outputs of hydroshoot, and runs 4 simulations, where a grape is placed on different positions of the shoot architecture : two where we consider the grape to be at the first internode of each of the two shoots of the plant, and two more where we place the grape on the 10th internode if each of the shoots. The simulations have a duration of 4 days, as defined in the file *params.json*, where the daily ψ<sub>soil</sub> is taken from the file *soil.input*.

## Our test

We run those 4 simulations with two different soil potential scenarios. On the first, for the four days of the simulation the soil water potential was constant, at -0.12 MPa. On the second it fluctuated with  0.30, -0.12, -0.89 and -0.20 MPa respectively. Among the numerous outputs that Virtual Berry gives us, we focus on the fresh fruit weight (FFW). As seen in the figures below, the position of the grape along the shoot plays a minor role, where the higher the grape is, the less its FFW. On the other hand the soil water potential plays a major role and notably on the third day of the second simulation there is a major drop in FFW because of the water deficit (induced by the -0.89 MPa water potential).

![Simulation Results](/images/Figure.png)

<!--- ![3D Reconstruction of Plant Architecture](/images/openalea.rtfd.io/doc/tutorials/notebook/images/mtg_plantframe.png){width="30.0%"} 

![L-Systems Simulation](/images/openalea.rtfd.io/doc/tutorials/notebook/images/lpy_lpymagic.png){width="30.0%"}

![Reconstruction and Ecophysiology of Grapevine](/images/openalea.rtfd.io/doc/tutorials/notebook/images/hydroshoot_grapevine.png){width="30.0%"}

![Light Interception](/images/openalea.rtfd.io/doc/tutorials/notebook/images/caribu_crops.png){width="30.0%"}

![Architectural analysis construction & vizualisation of 2D/3D architecture.](/images/openalea.rtfd.io/doc/tutorials/notebook/images/strawberry.png){width="100.0%"})
-->

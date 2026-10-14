Title: PhD Thesis Summary
Date: 2020-02-28 12:00
Tags: EEG, AD, PhD
Author: Raymundo Cassani
Slug: phd-thesis-summary
Thumbnail: eeg_ad_diagnose.png

In November 2018, I performed my PhD defense, this is a summary of it.
The title is "Towards an Automated Portable EEG-based System for Alzheimer’s Disease Diagnosis", and it can be found in its integrity [here](http://espace.inrs.ca/8005/1/Cassani%20Gonzalez%2C%20Raymundo.pdf). The defense slides are available [here](https://www.dropbox.com/s/0cwt4mskm63u6bs/thesis_slides.pdf?dl=0)

[TOC]

<hr>
### Challenges for EEG-based Alzheimer’s disease diagnosis

The term dementia is used to encompass a number of neurodegenerative disorders that have their origin in damage and death of neurons.  In 2015, 46.8 million people were living with dementia and this number is projected to grow to 74.7 million by 2030, and to 131.5 million by 2050, this trend is driven by population growth and demographic ageing. Among the disorders classified as dementia, Alzheimer’s disease (AD) is the most common which accounts for nearly 70% of the cases. Frequently AD is diagnosed with exhaustive neuropsychological examinations, and the diagnosis is supported by biomarkes from cerebospinal fluid and neuroimaging techniques. Unfortunately, these supporting biomarkers are invasive, expensive and geographically confined. In the last two decades, <a href="https://en.wikipedia.org/wiki/Electroencephalography"><abbr title="electroencephalography">EEG</abbr></a>-based biomarkers have emerged as a promising tool in the study of AD, as EEG is non-invasive, less expensive and potentially portable. EEG signals are consists of recording changes in the electrical potential measured at the scalp with electrodes. And their origin is the electrical activity evoked by synchronous activation of thousands of neurons with similar spatial orientation (dipoles). Thus, EEG biomarkers can be used to infer neuronal degeneration and decay in the number of synapses caused by AD progression [[1]](http://downloads.hindawi.com/journals/dm/2018/5174815.pdf).

<center>
	[<img src="/images/eeg.png" style="width: 800px;"/>](/images/eeg.png)  
</center>

However the use of EEG for AD diagnosis presents two major challenges: (i) EEG signals are subject to interference from other signals (artifacts), and (ii) the need for large number of electrodes, often 16+, thus making them hard to transport and expensive to fund, specially for low- and middle-income countries.

### Thesis contributions.
In my doctoral thesis, the steps towards the development of an automated portable and low-cost EEG-based system for AD diagnosis were presented:

**1. Towards automation**  
		Explore the effects of automated artifact handling algorithms in the pre-processing or EEG signals  
**2. Towards portability**  
		Explore the potential of portable devices in EEG signal acquisition  
**3. New modulation-domain features**:  
		Propose new EEG features based on the modulation representation, not-defined with traditional EEG-band limits

<center>
	[<img src="/images/eeg_ad_diagnose.png" style="width: 800px;"/>](/images/eeg_ad_diagnose.png)  
	General structures of an EEG-based AD diagnosis system
</center>
### 1. Towards automation
To remove the need for expert human intervention, we explored the effects of several fully automated artifact handling algorithms on EEG signals and gauge their advantages and disadvantages for automated AD diagnosis. Overall the classification performance obtained using automated artifact handling was in line with the performance obtained with systems based on “artifact-free” EEG data manually selected by human experts. Such findings suggest that manual inspection of the EEG signals can be avoided by using automated artifact removal, thus making faster the process and improving reproducibility [[2]](https://www.frontiersin.org/articles/10.3389/fnagi.2014.00055).

### 2. Exploring Portable
To explore the potential of portable low-density devices, we explored the differences in performance for AD diagnosis obtained with a 20-channel and 7-channel EEG system.

The reduction in the number of electrodes, led to a decrease in AD diagnosis performance. This could be attributed to the fact that a higher density layout presents a broader spatial distribution on the scalp; thus it can register cortical activity from other regions
such as temporal and occipital lobes. In addition, a higher density coverage may be able to pick up spatially broad activities caused by deep brain structures, which are the first-affected by AD progression. However, further exploration is needed regarding the low-density electrode layout, as a limitation in our experiments, was that the layout pre-defined by experimental protocol from a different EEG dataset, thus this may not be optimal for AD diagnosis using resting-state EEG [[3]](https://www.sciencedirect.com/science/article/abs/pii/S174680941630221X).

### 3. Exploring novel features
Lastly, EEG-based AD diagnosis has relied on conventional EEG features. Here, a new class of features derived from the modulation spectrogram from the EEG signal, which aims to characterize the second order periodicity of the signals.

<center>
	[<img src="/images/mod_steps.png" style="width: 800px;"/>](/images/mod_steps.png)  
</center>

In the modulation domain, differences between normal aging subjects and subjects with AD are visible and defined in different regions of the modulation spectrogram. The features from this representation shown to (i) provide improved robustness against artifacts, (ii) potentially bypass the need for a separate artifact removal step, and (iii) provide better discriminatory information not only for AD diagnostic purposes, but also for disease progression monitoring. Results showed that the proposed features can be more reliable for EEG-based AD diagnosis. Also, we explored these new features with a 7-channel EEG layout showing that the obtained performance is in line with the one obtained with 20 channels [[4]](https://ieeexplore.ieee.org/abstract/document/8901227).

<center>
	[<img src="/images/auc_figs.png" style="width: 800px;"/>](/images/auc_figs.png)  
</center>


### Conclusion
Unfortunately, the use of EEG in the clinical practice is not currently part of the routine in the diagnosis and monitoring of AD. In this thesis work we identified, discussed and propose solution to the major challenges of the utilization of EEG for the study of AD.
It is hoped that the innovations presented in the thesis work will boost the research and clinical use of EEG as a non-invasive, less expensive and potentially portable technique for the diagnosis and monitoring of AD.


### References
**[1]** [R. Cassani, M. Estarellas, R. San-Martin, F. J. Fraga, and T. H. Falk, “Systematic Reviewon Resting-State EEG for Alzheimer’s Disease Diagnosis and Progression Assessment,”Disease Markers, vol. 2018, 2018.](http://downloads.hindawi.com/journals/dm/2018/5174815.pdf)  
**[2]** [R. Cassani, T. H. Falk, F. J. Fraga, P. A. M. Kanda, and R. Anghinah, “The effects ofautomated artifact removal algorithms on electroencephalography-based Alzheimer’s diseasediagnosis,”Frontiers in Aging Neuroscience, vol. 6, p. 55, 2014.](https://www.frontiersin.org/articles/10.3389/fnagi.2014.00055)  
**[3]** [R. Cassani, T. H. Falk, F. J. Fraga, M. Cecchi, D. K. Moore, and R. Anghinah, “Towardsautomated electroencephalography-based Alzheimer’s disease diagnosis using portable low-density devices,”Biomedical Signal Processing and Control, vol. 33, pp. 261–271, Mar.2017.](https://www.sciencedirect.com/science/article/abs/pii/S174680941630221X)  
**[4]** [R. Cassaniand T. H. Falk, “Alzheimer’s Disease Diagnosis and Severity Level DetectionBased on Electroencephalography Modulation Spectral ‘Patch’ Features,” inIEEE J. Biomed.Health Inform., pp. 1–1,2019.](https://ieeexplore.ieee.org/abstract/document/8901227)  

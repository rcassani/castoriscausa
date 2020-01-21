Title: Software
Date: 2016-10-22
Slug: software
Author: Ray Cassani
Summary:
Sortorder: 2

This is list of some of the projects I have contributed:

* ### MuSAE Lab EEG Server (MuLES)
**MuLES** is an EEG acquisition and streaming server programmed in LabVIEW. It creates a standard interface for different portable EEG headsets, to accelerate the development of brain-computer interfaces (BCIs) and of general EEG uses in novel contexts. Latest version is compatible with Interaxon Muse, Emotiv EEG, Neuroelectrics Enobio, and OpenBCI devices.  
[https://github.com/MuSAELab/MuLES](https://github.com/MuSAELab/MuLES)

* ### Amplitude Modulation Analysis (AMA) Toolkit
The **AMA toolkit** provides functions to compute forward and inverse transformations between time, frequency, time-frequency and frequency-modulation-frequency domains for single- or multichannel signals. Additionally, a graphical user interface is provided for real-time exploration of the signals and their representations
across different domains. The toolkit is availabe for Python3, Octave and MATLAB.  
[https://github.com/MuSAELab/amplitude-modulation-analysis-module](https://github.com/MuSAELab/amplitude-modulation-analysis-module)

* ### VR and 360 camera
Unity project to live-stream 360° video from a Theta S camera, to a VR headset.  
[https://github.com/rcassani/ThetaWifiStreaming2VRheadset](https://github.com/rcassani/ThetaWifiStreaming2VRheadset).

* ### BLE Toolkit for LabVIEW
The **BLE Toolkit for LabVIEW** is an implementation of the [BGAPI protocol v1.3](http://www.silabs.com/documents/login/reference-manuals/Bluetooth_Smart_Software-BLE-1.3-API-RM.pdf) (by [Silicon Labs](http://www.silabs.com/)). **BGAPI protocol** is a based command and response protocol that allows the Bluetooth
Smart stack (in Silicon Labs BLE devices) to be controlled form an external host and an application over USB/UART. The toolkit has been developed and tested with the [BLE USB dongle BLED112](http://www.silabs.com/products/wireless/bluetooth/bluetooth-low-energy-modules/ble121lr-bluetooth-smart-long-range-module1).  
[https://github.com/MuSAELab/BLE-Toolkit-LabVIEW](https://github.com/MuSAELab/BLE-Toolkit-LabVIEW)

* ### OpenBCI Toolkit for LabVIEW
The **OpenBCI Toolkit for LabVIEW** handles the communication with the **OpenBCI Cyton** board and the **OpenBCI DONGLE**, by implementing the [OpenBCI communication protocol](http://docs.openbci.com/OpenBCI%20Software/04-OpenBCI_Cyton_SDK) in LabVIEW, to write (configuration) and read (configuration, raw EEG data and acceleration data) from the **OpenBCI Cyton** board. This toolkit has been tested in the 32bit version (firmware 2.x or higher) of the OpenBCI Cython board with 8 and 16 channels.  
[https://github.com/rcassani/OpenBCI-Toolkit-LabVIEW](https://github.com/rcassani/OpenBCI-Toolkit-LabVIEW)

* ### LabVIEW Emotiv Toolkit V2
The **LabVIEW Emotiv Toolkit V2** upgrades V1 by adding the capability of acquiring raw EEG data from the Emotiv Epoc (and Epoc+) headset and writing markers to the headset. This toolkit also integrates examples to Plot and Save as CSV files the raw EEG data.  
[https://forums.ni.com/t5/Example-Programs/LabVIEW-Emotiv-Toolkit-V2/ta-p/3493301?profile.language=en](https://forums.ni.com/t5/Example-Programs/LabVIEW-Emotiv-Toolkit-V2/ta-p/3493301?profile.language=en)

* ### neuralDrift
**neuralDrift** is a collaborative multiplayer neurogame based on brain-computer interfaces. The game consists in a LEGO&copy; MINDSTORMS&copy; EV3 robot, an Android device displaying the game state, and requires two EEG devices supported by [MuLES](https://github.com/MuSAELab/MuLES).  
[https://github.com/hubertjb/neuraldrift](https://github.com/hubertjb/neuraldrift)

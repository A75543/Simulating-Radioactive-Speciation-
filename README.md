# Simulating-Radioactive-Speciation-
Simulating the Chemical Speciation of Radioactive Contaminants at Elevated Temperatures //Alberto Rosas, DR. Ruth Tinnacher

Introduction
Thermochemical data is essential for understanding chemical reactions and processes, especially those involving radioactive elements. To conduct effective research in this area, it is crucial to identify reliable data sources, efficiently extract relevant information, and analyze the data comprehensively. This essay outlines the methodical approach I adopted for my research on thermochemical data, focusing on the selection of databases, data extraction, analysis, and simulation preparation.

Identifying Suitable Databases
The first step in my research was to identify suitable databases for obtaining thermochemical data. After a thorough review, I considered two primary databases:

Thermo-Chimie
NEA (Nuclear Energy Agency)
Among these, I selected Thermo-Chimie due to its ease of access and the availability of preformatted PhreeQc data for various reactions at different temperatures. The preformatted data, especially the equilibrium constants at different temperatures (e_DH), made it particularly convenient for my research needs, providing a streamlined pathway for data extraction and analysis.

Data Extraction and Analysis
Elements of Interest
My research focused on the following elements, which are significant in various thermochemical processes and nuclear waste management:

Americium (Am)
Cesium (Cs)
Curium (Cm)
Neptunium (Np)
Plutonium (Pu)
Strontium (St)
Technetium (Tc)
Database Checking
To gather the necessary data, I meticulously checked the Thermo-Chimie database for each of these elements. The primary objective was to identify reactions that had temperature-dependent equilibrium constants, which are crucial for accurate thermochemical simulations.

Python Code for Data Extraction
To facilitate the extraction of data, I wrote a Python script that automates the process of extracting all reactions for a given element from the Thermo-Chimie database in PhreeQc format. The script generates two files for each element:

.dat file: Contains all the reactions in PhreeQc format.
.csv file: Can be transferred to Excel for further analysis.
Here is a simplified version of the Python code used for data extraction:

# Example usage
extract_reactions('Np', 'thermo_chimie_database.txt')
Data Analysis
Categorization of Reactions
Once the data was extracted, I categorized the reactions into two groups:

Usable Reactions: These reactions had temperature-dependent equilibrium constants, making them suitable for detailed simulations.
Not Usable Reactions: These reactions lacked temperature-dependent equilibrium constants.
Analysis Results
For each element, I performed a detailed analysis, focusing on:

The number of usable reactions
The number of not usable reactions
The total number of reactions
The valence/oxidation states of each element
Through this analysis, I found that Neptunium (Np) had the highest number of usable reactions, making it the optimal choice for further simulations. This decision was based on the comprehensive data available, which would allow for more accurate and reliable simulation results.

Simulation Preparation
Having selected Neptunium (Np) for simulations, I proceeded with the following steps:

Educational Preparation: I watched pre-recorded videos on PhreeQc and GLE to deepen my understanding of these tools and their application in thermochemical simulations.
Reviewing Input Files: I thoroughly reviewed the input file format for PhreeQc to ensure that the data I extracted would be correctly formatted and usable in simulations.
Creating Input Files: Based on the extracted and analyzed data, I created input files for PhreeQc, which were then ready for simulation.
Conclusion
Conducting research on thermochemical data involves a systematic approach to identifying reliable data sources, extracting relevant information, and performing thorough analysis. By choosing the Thermo-Chimie database for its ease of access and preformatted data, writing Python code for efficient data extraction, and performing detailed analysis, I was able to prepare accurate and comprehensive input files for simulations. This methodical approach not only ensured the reliability of the data but also laid a solid foundation for future thermochemical research and simulations.

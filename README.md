# ProPep Data Extractor

The <i>ProPep Data Extractor</i> is a script that can extract values of molecular weight, specific impulse, isentropic exponent, total temperature, and characteristic velocity from <a href="http://www.nakka-rocketry.net/th_prope.html">ProPep</a> multiple run output file.

For now, the script only looks for frozen flow parameters and the molecular weight is taken from the Chamber Flow section

The ProPep output file should be saved as <i>"data.txt"</i> and placed in the same folder as the <i>.py</i> file. The result of the script running is generated as a <i>output.csv</i> file in the same directory.



pyinstaller --onefile -w 'ProPep Data Extractor.py'

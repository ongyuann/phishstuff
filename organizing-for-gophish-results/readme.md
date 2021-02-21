these scripts work by targeting only the CSV files and applying themselves to those files.
- add_and_fix_time.py: adds 8 hours (customize the script for any timing you wish)
- whois-ips.py: performs a whois lookup on source IP addresses in the CSV file
- both files - please customize accordingly for any column names not found in the scripts - these assume standard GoPhish CSV outputs

tl;dr: just put the CSV results in the same folder as these scripts, run the scripts, and collect the results!!
  
  
Step 1: Put everything (.csv results, .py scripts) in one folder
  
  
Step 2: Run the scripts
```
python3 add_and_fix_time.py
python3 whois-ips.py
```
Step 3: Collect the results in .TXT files!

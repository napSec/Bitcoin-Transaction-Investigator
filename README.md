# Bitcoin Transaction Investigator
<p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Bitcoin Transaction Investigator </strong></span></span></p>

<p><strong>Developed by NapSec_ - Red Team &amp; Penetration Testing Consultant that moonlights as a Blockchain Investigation SME </strong></p>

<p>&nbsp;</p>

<p>The Bitcoin Transaction Investigator uses the Blockchain.com Explorer AP(free)I to get the input and output addresses for an individual or a list of Bitcoin transaction hashes.</p>

<p>The user has the option to input the transaction hashes manually or read them from a CSV or TXT file.</p>

<p>To use the script, you need to have Python installed on your machine, as well as the <code>requests</code> library which can be installed via pip.</p>

<p>To get started, clone the repository to your local machine.</p>
<p><code> $ git clone https://github.com/napSec/Bitcoin-Transaction-Investigator.git </code></p>

<p><code> $ python3 hashdetails1.py </code></p>

<p>&nbsp;</p>

<p>Select (1) for manually entering the transaction has or (2) to load from a .csv or .txt file The API will time out if your file has a lot of hashes to look up to which I have no control over. sry.</p>

<p>This make a GET request to the Blockchain.com Explorer API for each transaction hash, and will get the input and output addresses for the transaction(s). The script will then print the results to the console and save them to a CSV file in the same directory as the script.</p>

<p>&nbsp;</p>

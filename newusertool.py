import pandas as pd
import sys
import io
title = "Transforming Excel Data with Python in the Browser"
page_message = "Loads pasted excel data into a table"
#url = "https://raw.githubusercontent.com/datasets/airport-codes/master/data/airport-codes.csv"
Element("header-title").element.innerText = title
Element("page-title").element.innerText = title
Element("page-message").element.innerText = page_message
Element("txt-url").element.value = ""

# CCL Code List
ccl_code = [
'; USER RE-ACTIVATION SCRIPT',
'update into prsnl p',
'set p.end_effective_dt_tm = cnvtdatetime("31-DEC-2100")',
', p.updt_dt_tm = cnvtdatetime(curdate,curtime3)',
', p.updt_id = reqinfo->updt_id',
', p.updt_cnt = p.updt_cnt + 1',
'where p.username = "SWAPME123"',
''
]

final_activate_code_string = str('')

df = pd.DataFrame()
def loadFromPasted(*ags, **kws):
    global df
    global final_activate_code_string
    # clear dataframe & output
    df = pd.DataFrame()
    final_activate_code_string = str('')
    Element("pandas-output-inner").element.innerHTML = ""
    
    # Pasted Excel option
    data = js.document.getElementById("txt-url").value
    df = pd.read_csv(io.StringIO(data), sep='\t', header=0)
    #Display
    Element("pandas-output").element.style.display = "block"
    display (df, target="pandas-output-inner", append="False")

    for a_row in ccl_code:
        # REPLACE SWAPME123 with the username in each row of the code slab
        new_row = a_row.replace('SWAPME123', 'to_switch')
        final_activate_code_string = final_activate_code_string + new_row + '\n'

def createAuthenticate(*ags, **kws):
    Element("activate-code").element.style.display = "block"
    display (final_activate_code_string, target="activate-code-inner", append="False")
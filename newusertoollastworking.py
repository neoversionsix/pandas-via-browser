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

df = pd.DataFrame()
def loadFromPasted(*ags, **kws):
	global df
	# clear dataframe & output
	df = pd.DataFrame()
	Element("pandas-output-inner").element.innerHTML = ""
	
	# Pasted Excel option
	data = js.document.getElementById("txt-url").value
	df = pd.read_csv(io.StringIO(data), sep='\t', header=0)
	
	#Element("pandas-repl").element.style.display = "block"
	Element("pandas-output").element.style.display = "block"
	#Element("pandas-dev-console").element.style.display = "block"
	display (df, target="pandas-output-inner", append="False")

def createAuthenticate(*ags, **kws):
    x = 'hello'
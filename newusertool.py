import pandas as pd
from js import document
import datetime
import numpy as np
import io

title = "Transforming Excel Data with Python in the Browser"
page_message = "Loads pasted excel data into a table"

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
# Content Manager Variables
#content_manager_template_json = '{"External Id":{},"External Id Alias Pool":{},"Username":{},"*Last Name":{},"*First Name":{},"Middle Name":{},"Name Full Formatted":{},"Title":{},"Suffix":{},"Position":{},"Begin Date+Time":{},"*End Date+Time":{},"Physician Ind":{},"SSN":{},"SSN Pool":{},"Birthdate":{},"Sex":{},"VIP":{},"Active Ind":{},"Primary Assigned Location":{},"Email":{},"*Prsnl Alias Type":{},"*Prsnl Alias":{},"*Prsnl Alias Pool":{},"Prsnl Alias Active Ind":{},"Prsnl_Alias_End_Dt":{},"*Org Name":{},"Org Confid Level":{},"Org_End_Dt":{},"*Address Type":{},"*Address Type Seq":{},"Address Street 1":{},"Address Street 2":{},"Address Street 3":{},"Address Street 4":{},"City":{},"County":{},"State or Prov":{},"Country":{},"Zip Code":{},"Contact":{},"Comment":{},"District Health UK":{},"Primary Care UK":{},"Address_Delete_Ind":{},"Org Address Reltn Ind":{},"Org Addr Name":{},"Org Addr Type":{},"Org Addr Sequence":{},"*Phone Type":{},"*Phone Type Seq":{},"Phone Number":{},"Phone Extension":{},"Phone Format":{},"Phone Description":{},"Phone Contact":{},"Phone Call Instruction":{},"Phone_Delete_Ind":{},"Org Phone Reln Ind":{},"Org Phone Name":{},"Org Phone Type":{},"Org Phone Seq":{},"*Location Type":{},"*Location Name":{},"Location_Delete_Ind":{},"*Org Group Type":{},"*Org Group Name":{},"Org_Group_Delete_Ind":{},"*Prsnl Group Type":{},"*Prsnl Group Name":{},"*Prsnl Group Class":{},"Prsnl_Group_Delete_Ind":{},"*Clinical Service Display":{},"Clinical Service Default":{},"Clinical Service Org Name":{},"Clin_Serv_Delete_Ind":{}}'
header_row = ['*Last Name', '*First Name', 'Middle Name', 'Username', 'External Id', 'External Id Alias Pool', 'Name Full Formatted', 'Title', 'Suffix', 'Position', 'Begin Date+Time', '*End Date+Time', 'Physician Ind', 'SSN', 'SSN Pool', 'Birthdate', 'Sex', 'VIP', 'Active Ind', 'Primary Assigned Location', 'Email', '*Prsnl Alias Type', '*Prsnl Alias', '*Prsnl Alias Pool', 'Prsnl Alias Active Ind', 'Prsnl_Alias_End_Dt', '*Org Name', 'Org Confid Level', 'Org_End_Dt', '*Address Type', '*Address Type Seq', 'Address Street 1', 'Address Street 2', 'Address Street 3', 'Address Street 4', 'City', 'County', 'State or Prov', 'Country', 'Zip Code', 'Contact', 'Comment', 'District Health UK', 'Primary Care UK', 'Address_Delete_Ind', 'Org Address Reltn Ind', 'Org Addr Name', 'Org Addr Type', 'Org Addr Sequence', '*Phone Type', '*Phone Type Seq', 'Phone Number', 'Phone Extension', 'Phone Format', 'Phone Description', 'Phone Contact', 'Phone Call Instruction', 'Phone_Delete_Ind', 'Org Phone Reln Ind', 'Org Phone Name', 'Org Phone Type', 'Org Phone Seq', '*Location Type', '*Location Name', 'Location_Delete_Ind', '*Org Group Type', '*Org Group Name', 'Org_Group_Delete_Ind', '*Prsnl Group Type', '*Prsnl Group Name', '*Prsnl Group Class', 'Prsnl_Group_Delete_Ind', '*Clinical Service Display', 'Clinical Service Default', 'Clinical Service Org Name', 'Clin_Serv_Delete_Ind']

end_date = r"30/12/2100"
alias_pool = 'External ID'
today = datetime.date.today()
d1 = today.strftime("%d/%m/%Y")
begin_date = d1 + ' 00:00'
end_date = '31/12/2100 00:00'
act_ind = '1'
org_g_type = 'SECURITY'
org_g_name = 'Western Health'

# Create Content manager Template
#df_cm = pd.read_json(content_manager_template_json, orient='index')
df_cm = pd.DataFrame(columns=header_row)

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

    for index, row in df.iterrows():
        # Column that has the usernames to put in the code
        to_switch = row['USERNAME'].upper()
        #Write to file
        for a_row in ccl_code:
            # REPLACE SWAPME123 with the username in each row of the code slab
            new_row = a_row.replace('SWAPME123', to_switch)
            final_activate_code_string = final_activate_code_string + new_row + '\n'

    #Content Manager Dataframe
    row_number = 0
    for index, row in df.iterrows():
        # Column that has the usernames to put in the code
        a_user = row['USERNAME'].upper()
        a_credential = str(row['CREDENTIAL'])
        # Set credential to blank rather than 'nan' if it's not filled out
        if a_credential == 'nan':
            a_credential = ''
        a_fname = row['FIRST']
        a_lname = row['LAST']
        a_fullname = a_lname + ', ' + a_fname + ' - ' + a_credential
        a_position = row['POSITION']
        a_extid = 'WHS' + a_user
        physician_ind = '0'
        if a_position == 'Medical Officer':
            physician_ind = '1'
        if a_position == 'Medical Officer P1':
            physician_ind = '1'
        # Edit Sheet
        df_cm.loc[row_number,'Username'] = a_user
        df_cm.loc[row_number,'External Id'] = a_extid
        df_cm.loc[row_number,'External Id Alias Pool'] = alias_pool
        df_cm.loc[row_number,'*Last Name'] = a_lname
        df_cm.loc[row_number,'*First Name'] = a_fname
        df_cm.loc[row_number,'Name Full Formatted'] = a_fullname
        df_cm.loc[row_number,'Position'] = a_position
        df_cm.loc[row_number,'Begin Date+Time'] = begin_date
        df_cm.loc[row_number,'*End Date+Time'] = end_date
        df_cm.loc[row_number,'Physician Ind'] = physician_ind
        df_cm.loc[row_number,'Active Ind'] = act_ind
        df_cm.loc[row_number,'*Org Group Type'] = org_g_type
        df_cm.loc[row_number,'*Org Group Name'] = org_g_name
        row_number+=1
    

def createAuthenticate(*ags, **kws):
    Element("activate-code").element.style.display = "block"
    display (final_activate_code_string, target="activate-code-inner", append="False")

def createContentManagerFile(*ags, **kws):
    Element("content-manager").element.style.display = "block"
    #display (df_cm, target="content-manager-inner", append="False")
    html_table = df_cm.to_html(index=False)
    display(html_table, target="content-manager-inner", append=False)
    document.getElementById("content-manager-inner").innerHTML = html_table;
#end
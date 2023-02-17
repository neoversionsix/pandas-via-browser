# ACTIVATE CODE


def loadActivateCode(*ags, **kws):
    # WRITE CODE TO STRING
    final_activate_code_string = str('')
    for index, row in df.iterrows():
        # Column that has the usernames to put in the code
        to_switch = row['USERNAME'].upper()
        #Write to file
        for a_row in ccl_code:
            # REPLACE SWAPME123 with the username in each row of the code slab
            new_row = a_row.replace('SWAPME123', to_switch)
            final_activate_code_string = final_activate_code_string + new_row + '\n'
    Element("activate-code").element.style.display = "block"
    #Element("pandas-dev-console").element.style.display = "block"
    display (final_activate_code_string, target="activate-code-inner", append="False")
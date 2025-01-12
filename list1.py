
string23="Engineering & Management Mastermind | Data Analyst| Diagnostics| OTA| Telematics| Infotainment| Data Analyst Consultant| Agile Project /Product Manager | Lead| Selenium Test Engineer"

string43=string23.replace("|", '').replace("/","")
print (string43)

def replace_func(string_new):
    if string_new == "":
        return None
    else:
        for i in string_new:
            string_new1 = string_new.replace("|","")

        return string_new1

print(replace_func(string23))




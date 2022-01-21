
import pathlib

def sumstats(Data,stats,file_name,rounding=3,float_f="{:,.3f}".format):
    
    float_f = "{:,." + str(rounding) + "f}"
    float_f = float_f.format
    
    pctiles = [k for k in stats if "%" in k]
    stats_dict = {'count':'N',
                  'mean':'Mean',
                  'std':'Std. Dev.',
                  'min':'Min',
                  'max':'Max',
                  '5%':'5th',
                  '10%':'10th',
                  '25%':'25th',
                  '50%':'Median',
                  '75%':'75th',
                  '90%':'90th',
                  '95%':'95th'}
    
    pctile_dict = {'5%':0.05,'10%':0.1,
                   '25%':0.25,'50%':0.5,
                   '75%':0.75,'90%':0.9,'95%':0.95}
    
    pctile_dict2 = {k: pctile_dict[k] for k in pctiles}
    desc_pctiles = list(pctile_dict2.values())
    
    
    table = round(Data.describe(percentiles = desc_pctiles).T[stats],rounding)
    table.rename(columns = stats_dict,inplace=True)
    
    stats2 = [ stats_dict.get(item,item) for item in stats ]
    
    
    var_cols = "l"+"c"*len(table.columns)
    a = table.to_latex(column_format = var_cols,float_format = float_f)
    a = a.replace("\\toprule","")
    a = a.replace("\\midrule","")
    a = a.replace("\\bottomrule","")
    a = a.replace(".0 "," ")
    a = a.replace(".00 "," ")
    a = a.replace(".000 "," ")
    begin  = "\\begin{{tabular}}{{{}}}".format(var_cols)
    begin2 = begin+"\n \\hline "
    end  = "\\end{tabular}"
    end2 = "\n \\hline \\\\ \n"+end
    final_stat = stats2[len(stats2)-1]
    final_stat2 = final_stat + "\n \\\\ \\hline \n"
    a = a.replace(begin,begin2)
    a = a.replace(end,end2)
    a = a.replace(final_stat,final_stat2)
    pathlib.Path("{}".format(file_name)).write_text(a)
    
    
def table(Data,file_name,rounding=3,float_f="{:,.3f}".format,keep_index=True):
    
        
    float_f = "{:,." + str(rounding) + "f}"
    float_f = float_f.format
    table = round(Data,rounding)    
    
    lastcol = table.columns.tolist()[len(table.columns.tolist())-1].replace("%","\%")
    
    var_cols = "l"+"c"*len(table.columns)
    a = table.to_latex(column_format = var_cols,escape=False,index = keep_index,float_format = float_f)
    a = a.replace("\\toprule","")
    a = a.replace("\\midrule","")
    a = a.replace("\\bottomrule","")
    a = a.replace(".0 "," ")
    a = a.replace(".00 "," ")
    a = a.replace(".000 "," ")
    a = a.replace("%","\%")
    begin  = "\\begin{{tabular}}{{{}}}".format(var_cols)
    begin2 = begin+"\n \\hline "
    end  = "\\end{tabular}"
    end2 = "\n \\hline \\\\ \n"+end
    final_var = "&    "+table.columns[len(table.columns)-1]
    
    final_var2 = final_var + "\n \\\\ \\hline \n"
    a = a.replace(begin,begin2)
    a = a.replace(end,end2)
    a = a.replace("NaN","")
    #a = a.replace("_","\\_")
    a = a.replace("{} \\\\".format(lastcol),"{} \\\\ \\hline\\\\".format(lastcol))
    #if final_var.strip() != '&':
     #   a = a.replace(final_var,final_var2)
    pathlib.Path("{}".format(file_name)).write_text(a)


def table_return_text(Data,file_name,rounding=3,float_f="{:,.3f}".format,keep_index=True):
    
        
    float_f = "{:,." + str(rounding) + "f}"
    float_f = float_f.format
    table = round(Data,rounding)    
    
    lastcol = table.columns.tolist()[len(table.columns.tolist())-1].replace("%","\%")
    
    var_cols = "l"+"c"*len(table.columns)
    a = table.to_latex(column_format = var_cols,escape=False,index = keep_index,float_format = float_f)
    a = a.replace("\\toprule","")
    a = a.replace("\\midrule","")
    a = a.replace("\\bottomrule","")
    a = a.replace(".0 "," ")
    a = a.replace(".00 "," ")
    a = a.replace(".000 "," ")
    a = a.replace("%","\%")
    begin  = "\\begin{{tabular}}{{{}}}".format(var_cols)
    begin2 = begin+"\n \\hline "
    end  = "\\end{tabular}"
    end2 = "\n \\hline \\\\ \n"+end
    final_var = "&    "+table.columns[len(table.columns)-1]
    
    final_var2 = final_var + "\n \\\\ \\hline \n"
    a = a.replace(begin,begin2)
    a = a.replace(end,end2)
    a = a.replace("NaN","")
    #a = a.replace("_","\\_")
    a = a.replace("{} \\\\".format(lastcol),"{} \\\\ \\hline\\\\".format(lastcol))
    #if final_var.strip() != '&':
     #   a = a.replace(final_var,final_var2)
    pathlib.Path("{}".format(file_name)).write_text(a)
    return a
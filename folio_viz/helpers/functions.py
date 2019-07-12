import locale


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') 

def cleanFinancialStatement(financialStatement):
    statement = []
    for value in financialStatement.items():
            for k, v in value[1].items():
                if v is None:
                    value[1][k] = '-'
            
                try:
                    if len(v) >= 12:
                        v = float(v)
                        value[1][k] = int(v / 1000000)
                        value[1][k] = f'{value[1][k]:n}'
                    else:
                        v = float(v)
                        value[1][k] = round(v / 1000000, 3)
                        
                except:
                        continue    

                    
                       
            statement.append(value)  
    return statement
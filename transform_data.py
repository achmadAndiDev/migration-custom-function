import random
import string

class TransformData :
    def replace_privacy_columns(privacy_columns, table, row) :
        
        if table not in privacy_columns :
            return row
        
        for column in privacy_columns[table] :
            value = privacy_columns[table][column]

            if value in row :
                value = row[value]

            if value == "random()::text" :
                letters = string.ascii_lowercase
                value = ( ''.join(random.choice(letters) for i in range(10)) )

            row[column] = value
                
        return row
    
__version__ = '1.0'

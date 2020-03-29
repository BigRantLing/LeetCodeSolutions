recorded_error = []
error_counters = {}

while True:
    try:
        line = input()
        splited_line = line.split()
        row=splited_line[1]
        file_errorline = '_'.join(splited_line)

        if  file_errorline not in recorded_error:
            recorded_error.appen(file_errorline)
            error_counters[file_errorline] = 1
        else:
            error_counters[file_errorline] += 1
    
    except Exception e:
        sorted_keys = sorted(error_counters, key = lambda x:error_counters[x], reverse=True)
        index = 0 
        if index >= 8:
            break
        for key in sorted_keys:
            errors = error_counters.get(key)
            line = key.split('_')[-1]
            file = key.split('_')[0].split('\\')[-1]

            if len(file) > 16:
                file = file[0 : 16]
            
            print(file+' '+line+' '+errors)
            index += 1

            raise e
            
        break
    
    
# improved version
def parse_values(vs,value_type='simple'):
    # debug parsing value strings per Seshat Code book
    # takes a string and returns a list of value lists
    global vn_location,line_number,options,unique_values
    try:
        note = ''
        if vs == '':
            return [[value_type,vs,None,None,note]] # empty value
        vs = vs.replace('–','-') # unicode dash to plain dash
        vs_orig = copy.copy(vs)
        err_location = '' if options.nl else '%d: ' % line_number

        values = []
        while len(vs) > 0:
            vs = vs.lstrip()
            if len(vs) == 0:
                break
            
            if vs[0] == '{':
                vss,vs = extract_between(vs,'{','}',return_remainder=True)
                dvalues = parse_values(vss,'disputed')
                if len(dvalues) == 1:
                    pass # dvalues[0][3] = warning!!
                values.extend(dvalues)
                vs = vs.strip()
                if len(vs) > 0:
                    pass # report error and ignore trailing stuff
            elif vs[0] == '[':
                vss,vs = extract_between(vs,'[',']',return_remainder=True)
                uvalues = parse_values(vss,'uncertain')
                if len(uvalues) == 1:
                    pass # uvalues[0][3] = warning!!
                values.extend(uvalues)
                vs = vs.strip()
                if len(vs) > 0:
                    pass # report error and ignore trailing stuff
            else:
                # a set of stock values with optional dates
                for vss in vs.split(';'):
                    # restart note?
                    vss,date = vs.split(':')
                    if len(date) > 0:
                        date = date.strip()
                        date = date.upper() # canonically BCE or CE
                        date = date.replace(' ','') # no spaces
                        if options.u:
                            try:
                                unique_values[date]
                            except KeyError:
                                unique_values[date] = line_number # save the parsed date

                        # BUG date could be -400-300 BCE which is really 400BCE-300BCE
                        if len(date) > 0:
                            if date[0] == '-':
                                note += '%sIll-formed date %s; ' % (err_location,date)
                                date = date[1:]
                            if date.find('C') < 0:
                                # note += '%sMissing CE/BCE %s; ' % (err_location,date)
                                pass
                            dash_i = date.find('-') # Assume we never get -400 - -300BCE
                            # NOTE we don't check for BCE vs. BC, e.g., -400 BC - 149 CE -> 400BC,149CE
                            if dash_i >= 0:
                                from_date = date[0:dash_i]
                                to_date = date[dash_i+1:]
                                if from_date.find('C') < 0: # does first value have a (B)CE?
                                    if to_date.find('C') >= 0: # No, so copy from 
                                        if to_date.find('B') >= 0:
                                            from_date += 'BCE'
                                        else:
                                            from_date += 'CE'
                                    else:
                                        to_date += 'CE'
                                        from_date += 'CE'
                            else:
                                from_date = date
                                if from_date.find('C') < 0:
                                    from_date += 'CE'
                                to_date = None
                    else:
                        date_from = None
                        date_to = None
                    # clean the value
                    vss = vss.strip()
                    # eliminate any commas and save the string
                    # if it is a number it will look like a number when stripped
                    vss = vss.replace(',','') # eliminate commas in values
                    if options.u:
                        try:
                            unique_values[vss]
                        except KeyError:
                            unique_values[vss] = line_number # save the cleaned value
                    values = [value_type,vss,date_from,date_to,note]
                    values.append(value)
        return values
    except:
        note = 'ERROR: Unable to parse some value %s for %s %d' % (vs, vn_location,line_number)
        return [['simple',vs,None,None,note]]



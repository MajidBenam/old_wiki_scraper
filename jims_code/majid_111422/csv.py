#  /Users/jsb/PsychoHistory/Turchin/Seshat/stripper_scrapper/ss_vars2.py, Tue Mar  3 20:59:16 2020, Edit by jsb

# This code takes an xml file and keeps track of sections and for each variable, emits a csv line
# There are variable, value and section names that contain commas so deal with those by elimination.
# Same with '#' in variable names

# To make an equinox: strip with ss_vars2, then create a csv w/o line numbers
# python3 ../py3/ss_vars2.py -u  EQUINOX_seshat.info-20210327034806.xml > EQUINOX_seshat.info-20210327034806.txt
# python3 ../py3/csv.py  -d '|' -u -nl EQUINOX_seshat.info-20210327034806_stripped.xml > EQUINOX_seshat.info-20210327034806_stripped.txt

import sys
import traceback
import os
import os.path
import pprint
import copy
import re
import numpy as np
import argparse
options = None

polid_to_NGA = {} # for -N
unique_values = {} # value -> first line
line_number = 0
vn_location = ''
expand_values_format = '%s,%s,%s,%s,%s,%s,%s,%s'

recognized_top_sections = [
    #DEAD 'Main Variables',
    #DEAD 'Main Variables (Polity)',
    #DEAD'Main Variables (polity-based)',
    'Phase I Variables (polity-based)',
    'Phase II Variables (polity-based)',
    'References',
    'General Approach', # Code book but dropped
    'Agriculture, Economy, and Population Variables (NGA-based)',
    'Economy and Technology variables (NGA-Level)',
    'Agriculture',
    'Population',
    ]
variables = None

def parse_values(vs):
    # debug parsing value strings per Seshat Code book
    # takes a string and returns a list of value lists
    global vn_location,line_number,options,unique_values
    try:
        note = ''
        if vs == '':
            return [['simple',vs,None,None,note]]
        vs = vs.replace('–','-') # unicode dash to plain dash
        vs_orig = copy.copy(vs)
        err_location = '' if options.nl else '%d: ' % line_number
        def clean_value(v):
            global vn_location,line_number,options,unique_values
            v = v.strip()
            if v.find(',') >= 0:
                if False:
                    # possible number
                    vn = v.replace(',','')
                    try:
                        if vs.find('.') >= 0:
                            v = float(vn) # assume float
                        else:
                            v = int(vn) # assume integer
                            v = str(v) # back to a (stripped) string
                    except ValueError:
                        # BUG: there is a comma in the string value but it isn't a number
                        # Add to the note and fix!
                        # note += 'Eliminating comma in value' # note is not seen as a variable in this functions local scope
                        v = v.replace(',','') # eliminate it
                else:
                    # Alternatively, just eliminate the commas and save the string
                    # if it is a number it will look like a number when stripped
                    v = v.replace(',','') # eliminate commas in values

            if options.u:
                try:
                    unique_values[v]
                except KeyError:
                    unique_values[v] = line_number # save the cleaned value
            return v

        values = []
        while len(vs) > 0:
            vs = vs.lstrip()
            if vs[0] == '{':
                vss,vs = extract_between(vs,'{','}',return_remainder=True)
                # what about {300,000: 1710 CE; 130,000: 1714 CE; 150,000: 1746 CE}?
                # we don't parse the values and the dates
                # here we assume plain values without dates
                # why not call parse_value recursively?
                vsss = vss.split(';')
                for i in range(len(vsss)):
                    vsx = clean_value(vsss[i])
                    vsss[i] = vsx
                    dash_i = vsx.find('-')
                    if dash_i >= 0:
                        vdash = vsx.split('-')
                        try:
                            x = float(vdash[0])
                            x = float(vdash[1])
                            # if we get here we have two numbers and it should probably be 'vdash[0];vdash[1]'
                            # :'''♠ Duration ♣ {12-72} ♥'''  -> 
                            # Middle Yellow River Valley,CnMing*,Warfare variables,Most dysphoric collective ritual,Duration,12-72,,,,simple,disputed
                            # Should really be {12;72}
                            note += '%sWarning - Surrounding a range %s in disputed brackets; ' % (err_location,vsx)
                        except ValueError:
                            # '''♠ Degree of centralization ♣ {quasi-polity; confederated state} ♥
                            pass
                if len(vsss) == 1:
                    # TODO see if , is in vss, likely should have been ;
                    note += '%sWarning - Surrounding a simple value in disputed brackets: %s; ' % (err_location,vs_orig)
                value = ['disputed',vsss,None,None,note]
            elif vs[0] == '[':
                vss,vs = extract_between(vs,'[',']',return_remainder=True)
                dash_i = vss.find('-')
                if dash_i >= 0:
                    vsss = vss.split('-')
                    for i in range(len(vsss)):
                        vsss[i] = clean_value(vsss[i])
                    value = ['range',vsss,None,None,note]
                else:
                    vsss = vss.split(';')
                    for i in range(len(vsss)):
                        vsss[i] = clean_value(vsss[i])
                    if len(vsss) == 1:
                        # TODO see if , is in vss, likely should have been ;
                        #  :''' ♠ Long walls ♣ [7200] ♥ ''' km.
                        note += '%sWarning - Surrounding a simple value in uncertain brackets: %s; ' % (err_location,vs_orig)
                    value = ['uncertain',vsss,None,None,note]
            else:
                # stock value then optional date ; gets another
                # cannot use split() because you could have a mix of values and dates, e.g.,
                # a:d;b,c:d or a,b:d,c etc
                colon_i = vs.find(':')
                semi_i = vs.find(';')
                if colon_i >= 0:
                    if semi_i >= 0:
                        if colon_i < semi_i:
                            # V:date;...
                            vss = vs[0:colon_i]
                            vs = vs[colon_i:]
                        else:
                            # V; ...:...
                            vss = vs[0:semi_i]
                            vs = vs[semi_i]
                    else:
                        # V:date
                        vss = vs[0:colon_i]
                        vs = vs[colon_i:]
                else:
                    # no date
                    if semi_i >= 0:
                        vss = vs[0:semi_i]
                        vs = vs[semi_i:]
                    else:
                        vss = vs
                        vs = ''
                value = ['simple',clean_value(vss),None,None,note]
            values.append(value)
            vs = vs.lstrip()
            if len(vs) > 0 and vs[0] == ':':
                vs = vs[1:] # eat :
                # parse date til end or ;
                semi_i = vs.find(';')
                if semi_i >= 0:
                    date = vs[0:semi_i]
                    vs = vs[semi_i:] # point at the ;
                else:
                    date = vs
                    vs = ''
                # parse the date
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
                    value[2] = from_date
                    value[3] = to_date
                else:
                    # BUG malformed: '284-311ce: inferred absent; 312-397ce:'
                    value[4] += '%sMal-formed date %s; ' % (err_location,vs_orig)

            if len(vs) > 0 and vs[0] == ';':
                vs = vs[1:] # eat ;
                # continue
        return values
    except:
        note = 'ERROR: Unable to parse some value %s for %s %d' % (vs, vn_location,line_number)
        return [['simple',vs,None,None,note]]
    

def expand_values(values):
    # <prefix>,Value From,Value To,Date From,Date To,Fact Type,Value Note,Date Note,Comment
    strings = []
    global vn_location,line_number,expand_values_format
    def compose_value(fact_type,value_struct,override_value_note=None):
        global vn_location,line_number
        value_note,value,from_date,to_date,note = value_struct
        if override_value_note is not None:
            value_note = override_value_note
        date_note = ''
        if from_date is None:
            from_date = ''
            to_date = ''
        else:
            datep_note = 'simple'
            if to_date is None:
                to_date = ''
            else:
                date_note = 'range'
        # if there are multiple values, spread on separate lines unless range
        if value_note == 'range':
            from_value = value[0]
            to_value = value[1]
            if note != '':
                print('%d: %s: %s' % (line_number,vn_location,note))
            strings.append(expand_values_format % (from_value,to_value,from_date,to_date,fact_type,value_note,date_note,note))
        elif value_note in ['simple','list']:
            if note != '':
                print('%d: %s: %s' % (line_number,vn_location,note))
            strings.append(expand_values_format % (value,'',from_date,to_date,fact_type,value_note,date_note,note))
        else:
            for v in value:
                if note != '':
                    print('%d: %s: %s' % (line_number,vn_location,note))
                strings.append(expand_values_format % (v,'',from_date,to_date,fact_type,value_note,date_note,note))
        
    if len(values) > 1:
        complex_i = [vs for vs in values if vs[0] in ['disputed','uncertain','range']]
        value_note = 'list'
        if len(complex_i) > 0:
            value_note = None
        for value_struct in values:
            compose_value('complex',value_struct,override_value_note=value_note)
    else:
        compose_value('simple',values[0])
    return strings

# TOOD implement an alternative version that takes a compiled regexp instead
def extract_between(raw_line,start_tag,end_tag,startswith=False,return_remainder=False):
    if startswith:
        if False: # This is a mistake since lstrip gets rid of '  =' etc.
            raw_line = copy.copy(raw_line)
            raw_line.lstrip()
        start_i = raw_line.startswith(start_tag);
    else:
        start_i = raw_line.find(start_tag);
    if start_i >= 0:
        raw_line = raw_line[start_i + len(start_tag):]
        end_i = raw_line.find(end_tag);
        if end_i >= 0:
            if return_remainder:
                return (raw_line[0:end_i],raw_line[end_i+1:])
            else:
                return raw_line[0:end_i]
    if return_remainder:
        return (None,raw_line)
    else:
        return None


def xml_csv_file(xml_filename):
    global options, line_number, vn_location, expand_values_format, unique_values, variables, polid_to_NGA
    directory,basename = os.path.split(xml_filename)
    basename,ext = os.path.splitext(basename)
    try:
        xml_file = open(xml_filename, "r")
    except IOError:
        print("ERROR: Could not open %s for reading." %  xml_filename)
        return

    csv_filename = os.path.join(directory,basename + '.csv')
    try:
        csv_file = open(csv_filename, "w")
    except IOError:
        print("ERROR: Could not open %s for writing." %  csv_filename)
        return
    print('Generating %s from %s' % (csv_filename,xml_filename))
    max_line_size = 0
    missing_NGAs = []
    # heading
    hdr = 'NGA,Polity,Section,Subsection,Variable,Value.From,Value.To,Date.From,Date.To,Fact.Type,Value.Note,Date.Note,Error.Note'
    if options.D:
        hdr += ',Comment'
    hdr += '\n'
    # Convert commas between values to our chosen delimiter (even if the same)
    hdr = hdr.replace(',',options.d)
    csv_file.write(hdr)
    prefix_format = '%s,%s,%s,%s'
    prefix_format = prefix_format.replace(',',options.d)
    vn_location_format = '%s,%s'
    vn_location_format = vn_location_format.replace(',',options.d)
    vs_format = '%s,%s%s'
    vs_format = vs_format.replace(',',options.d)
    expand_values_format = expand_values_format.replace(',',options.d)

    line_number = 0;
    current_title = None # the prevailing page (from <title>); nothing yet

    sections = [None,None,None,None]
    sections_reset = copy.copy(sections)
    prefix = prefix_format % ('NGA',None,sections[1],sections[2]) # default 'prefix'
    skip_variable = False
    emit_end_text = False
    emit_section_text = False

    unique_values = {} # reset
    
    ### main parsing loop
    while True:
        raw_line = xml_file.readline()
        if not raw_line:
            break
        line_number += 1

        # End of a page; reset all section logic
        if raw_line.find('<sha1>') >= 0:
            emit_section_text = False
            sections = copy.copy(sections_reset)

        # import re
        # match = re.search(r'<title>(.*?)</title>.*',rawLine)
        # if match: title = match.groups(0)
        title = extract_between(raw_line,'<title>','</title>')
        if title is not None:
            current_title = title
            sections = copy.copy(sections_reset)
            prefix = prefix_format % ('NGA',current_title,sections[1],sections[2]) # reset default 'prefix'
            emit_section_text = False
            if options.S:
                print('Page: %s' % current_title) # so we can find which page to edit

        for entry in [('====',' >>>>',3),
                      ('===', ' >>>', 2),
                      ('==',  ' >>',  1),
                      # embedded URL references look like toplevel sections w/o startswith
                      # http://books.google.co.uk/books?id=T5tic2VunRoC&amp;dq=languages+roman+empire&amp;source=gbs_navlinks_s
                      # <text xml:space="preserve" bytes="3022">=IrAchae Conflicts (Achaemenid-Scythian, 511 BCE)=
                      # Also avoid startswith since we have lines like this, which should be 2 separate lines
                      #       <text xml:space="preserve" bytes="3022">=IrAchae Conflicts (Achaemenid-Scythian, 511 BCE)=
                      # NOTE that the re matching below would find 'preserve" bytes'!! 
                      ('=', ' >',   0),
                      # import re
                      # match = re.search(r'=(.*?)=.*',raw_line) # add ^ ?
                      # if match: section = match.groups()[0]
                      # NOTE ==foo== matches as well so definitely do it in longest to shortest order
                      ]: 
            section_tag,structure_tag,index = entry
            section = extract_between(raw_line,section_tag,section_tag,startswith=False)
            if section is not None and len(section) > 0:
                if index == 0 and section not in recognized_top_sections:
                    continue # Not a recognized toplevel section (lots of things seem to match =foo=)
                # reset any remaining subsections
                for idx in range(index,3+1):
                    sections[idx] = None
                section = section.replace(',','') # Gotta eliminate , in section names
                sections[index] = section
                polity = current_title
                NGA = 'NGA' # if you drop this, change the heading too
                if options.N:
                    try:
                        NGA = polid_to_NGA[polity]
                    except KeyError:
                        # go with 'NGA'
                        if polity not in missing_NGAs:
                            print('WARN: Unable to find NGA for %s!' % polity)
                            missing_NGAs.append(polity) # report this problem once
                section = sections[1]
                subsection = sections[2]
                subsection = subsection if subsection is not None else ''
                prefix = prefix_format % (NGA,polity,section,subsection)
                emit_section_text = True # will fallthrough and print below if needed
                break

        # See if we should drop a variable from this (and subsequent) lines
        vn = extract_between(raw_line,"♠","♣")
        if vn is not None:
            emit_section_text = False
            vn = vn.strip() # there is a variable + value on this line
            if variables:
                if vn not in variables:
                    continue
            # Must eliminate special characters in variable names
            vn = vn.replace(',','').replace('#','')
            vn_location = vn_location_format % (prefix,vn)
            vv = extract_between(raw_line,"♣","♥")
            if vv is None:
                print("%d: %s: Found variable but no terminated value" % (line_number, vn_location))
            else:
                vv = vv.strip()
                if vv != '' or options.e: # drop empty values unless keeping
                    descr = None
                    if options.D:
                        d_start_i = raw_line.find("♥")
                        raw_line = raw_line[d_start_i+1:] # lose the heart
                        descr = options.d # pre-pend our choosen delimiter as separator
                        sepr = ''
                        while True:
                            if raw_line.find(options.d) > 0:
                                break # raw line contains our delimiter so skip adding it (but delimit it!)
                            else:
                                raw_line = raw_line.strip()
                                raw_line = raw_line.replace("'''",'') # separator
                                raw_line = raw_line.replace("''",'"') # quote character
                                raw_line = raw_line.replace('&quot;','"') # quote character
                                raw_line = raw_line.replace('&lt;ref&gt;','<ref>')
                                raw_line = raw_line.replace('&lt;/ref&gt;','</ref>')
                                descr += raw_line # pre-pend our choosen delimiter as separator
                                descr += sepr
                                sepr = ' ' # Not!! \n How about <nl>?
                                if options.X:
                                    fpos = xml_file.tell()
                                    raw_line = xml_file.readline()
                                    if raw_line.find("♣") >= 0 or raw_line.find('=') == 0:
                                        # end of descrition; back up
                                        xml_file.seek(fpos)
                                        break
                                    line_number += 1
                                else:
                                    break # single line description only
                                
                    try:
                        unique_values[vv]
                    except KeyError:
                        unique_values[vv] = line_number # save the whole value line
                    values = parse_values(vv)
                    for vs in expand_values(values):
                        vs = vs_format % (vn_location,vs,'' if options.nl else ' %d' % line_number)
                        # Then add descr (already delimited) to the end
                        if descr:
                            vs += descr
                        vs += '\n'
                        max_line_size = max(max_line_size,len(vs))
                        csv_file.write(vs)
        else:
            if options.S and emit_section_text and len(raw_line) > 1:
                print(raw_line.strip())
        

    xml_file.close()
    csv_file.close()
    print('Max line size: %d' % max_line_size)
    if options.u:
        uv = sorted(list(unique_values.keys()))
        print('\nUnique values:')
        for v in uv:
            print("%6d '%s'" % (unique_values[v],v))
    return

def parse_file_values(filename):
    values = []
    if filename:
        try:
            value_file = open(filename, "r")
        except IOError:
            raise RuntimeError("ERROR: Could not open %s for reading." %  filename)
        for raw_line in value_file:
            comment_i = raw_line.find('#')
            if comment_i >= 0:
                raw_line = raw_line[0:comment_i]
            raw_line = raw_line.strip()
            if len(raw_line) == 0:
                continue
            values.append(raw_line)
        value_file.close()
    return values
    
    
if __name__ == "__main__":
    retval = 1

    def main():
        global options, variables,polid_to_NGA
        options = argparse.ArgumentParser(prog=sys.argv[0],
                                          description='Prepare a Seshat csv files from an xml file')
        options.add_argument('filename',help='The xml file', default=None)
        options.add_argument('-d',metavar='quoted character',help='Alternate delimiter character',default='|') # -d ','
        options.add_argument('-e', action='store_true', help='Emit empty variables',default=False)    
        options.add_argument('-u',  action='store_true', help='Report unique values',default=False)    
        options.add_argument('-S',  action='store_true', help='Report section/subsection strings',default=False)    
        options.add_argument('-nl', action='store_true', help='Do not report line numbers in csv',default=False)    
        options.add_argument('-N',  action='store_true', help='Lookup NGAs',default=False)    
        options.add_argument('-D',  action='store_true', help='Include descriptions',default=False)    
        options.add_argument('-X',  action='store_true', help='Include multi-line descriptions',default=False)    
        options.add_argument('-V',metavar='variables file',help='File with variable names',default=None)
        options = options.parse_args()
        if options.X:
            options.D = True
        if options.D:
            options.d = '|' # we embed commas
        if options.N:
            seshat_dir = '/Users/jsb/PsychoHistory/Turchin/Seshat'
            # this is converted from csv file to use | and keep only the first two columns
            # since the rest uses characters that can't be decoded using bytes or UTF8?!
            polvars_file = 'SeshatPolsVars.txt'; delimiter='|'; NGA_i = 0; polid_i = 1;
            polvars_file = '!SeshatPolsVars_02feb2021.txt'; delimiter='|'; NGA_i = 0; polid_i = 2;
            polvars = np.genfromtxt(os.path.join(os.path.abspath(seshat_dir), polvars_file),delimiter=delimiter, skip_header=1,dtype=None,encoding='UTF8')
            for entry in polvars:
                polid_to_NGA[entry[polid_i]] = entry[NGA_i]

        variables = parse_file_values(options.V)
        if len(variables):
            print('Filtering using %d variables from %s' % (len(variables),options.V))
            pprint.pprint(variables)
            
        if options.filename:
            xml_csv_file(options.filename)
        return 0

    try:
        retval = main() # in case we decide to profile this puppy
    except SystemExit:
        pass # be quiet...someone just wants to leave like parse_args()
    except:
        print("Unexpected error:", traceback.format_exc())

    sys.exit(retval)

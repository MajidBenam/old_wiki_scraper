#  /Users/jsb/PsychoHistory/Turchin/Seshat/stripper_scrapper/ss_vars2.py, Tue Mar  3 20:59:16 2020, Edit by jsb

# This code takes a categorized export file from the main Seshat wiki and strips it only
# producing a stripped file.  It can report variables but it doesn't store them
# This version deals with stripping variables and their following comments but can also require keeping variables by context

import sys
import traceback
import os
import os.path
import pprint
import copy
import re
import argparse
options = None

drop_lines = [
    '<timestamp>', # remove this so it creates a new version when imported into the browser wiki
    'File:', # we don't export files so drop these lines; but see HACK to deal with http://seshat.info/File:foo below!
    ]
keep_lines = [
    'http://www.mediawiki.org/xml/export-0.9', # head of the file
    '<namespace ', # these have = in them
    'info/File:', # keep these lines before we drop it due to File: above
    ]

top_sections_to_keep = [ # if matching top =Foo= sections they must have these tags or they are likely some URL fragment
    #DEAD 'Main Variables',
    #DEAD 'Main Variables (Polity)',
    #DEAD'Main Variables (polity-based)',
    'Phase I Variables (polity-based)',
    'Phase II Variables (polity-based)',
    'References',
    ]

recognized_top_sections = copy.copy(top_sections_to_keep)
# Add other top sections you want to find but may not want to keep
recognized_top_sections.extend([
    'General Approach', # Code book but dropped
    'Agriculture, Economy, and Population Variables (NGA-based)',
    'Economy and Technology variables (NGA-Level)',
    'Agriculture',
    'Population',
    ]) 

# We aren't exporting the NGA pages for general use
# There will be other ways of accessing the individual polity pages.
NGA_sections_to_skip = [ # DEAD
    # Main page
    'Beyond the World Sample-30',

    # NGA sections
    'Additional Polity Data',
    'Economy and Technology Variables (NGA-level)',
    'Resources, Agriculture, and Population (NGA-level)','Resources, Agriculture, and Population',
    'Workspace'
    'Wars, Battles and Sieges',
    # "Warfare (NGA-level)' see Crete add (NGA-level)
    # Aegean Conflict Coding see Crete
    'Old Versions of Resource, Agriculture, and Population Coded Sheets', # Middle_Yellow_River_Valley
    'Questions for Experts', # Middle_Yellow_River_Valley
    ]

# These need to be sections in the mediawiki sense: they use '=' to distinguish them
sections_to_skip = [
    # Polity page sections
    'Polity variables', 'Economy variables', 'Society variables', # These are only in FrCarlE!!
    'Macrostate Variables', # DH wanted these removed
    # under Social Complexity variables
    'Map',
    'The most impressive/costly building(s)',
    # Under Information drop measurement subsection once converted
    'Measurement System',
    # Per Peter 3/15/20 'Bureaucracy characteristics',
    # Under Military Technologies section
    # keep 'Military Technologies',
    'Military Organization',
    'Other technologies',
    'Legal (formal) limits',
    'Legal (formal) freedoms',
    'Limits on executive power imposed by religious agents',
    'General Characteristics of Warfare', 
    'List of Wars',
    'Individual Conflicts',
    'Warfare coding template', # includes several subsections
    'Ritual variables', # includes several subsections
    # Under Institutional Variables
    'Customary (informal) checks on executive', # faux
    'Central Bureaucracy',
    'Local-level officials (provincial, regional, civic administration)',
    'Mechanisms of Power Transfer (from one head of state to the next)',
    'Legal System', #should include Procedures of Legal System, Informal Justice, Property Rights, Inheritance System 
    'Equity', # includes several subsections
    # Under Status
    'Slavery',
    # Under Religion and Normative Ideology
    'Description of Religious or Normative Ideology System',
    # keep deification of rulers? and equity/prosociality
    'Normative Ideological Aspects of Slavery',
    'Normative Ideological Aspects of Human Sacrifice',
    # keep (insert) MSP
    'Normative Ideological precepts concerning morality/supernatural beings',
    'Well-Being', # includes several subsections
    'Economy variables (polity-level)', # includes several subsections

    # Whole sections (see top_level stuff above)
    # 'Agriculture, Economy, and Population Variables (NGA-based)',
    # 'Economy and Technology variables (NGA-Level)',
    # 'Agriculture',
    # 'Population',
    'Estimated Carrying Capacity',

    # Other random sections
    'HPI Variables',
    'LHF Priorities','LHF priorities','LHF priority',
    'Other Polities', #DH: I think we can skip this
    'Notes',
    'Expanded Content Pages',
     ]

    
# These are un-restricted variables: keep them regardless of context because of their unique names
keep_variables = [
    #
    # NGA variables (eliminate these variables, which are duplicated in other sections)
    #
    # 'Alternative names for the region',
    # 'Area',
    # 'Cities',
    # 'Coders',
    # 'Name of the natural historical region',
    # 'Name',
    # 'UTM zone',
    # 'World Region',
    
    #
    # Polity variables 1Mar20
    #
    'Administrative levels',
    # 'Alternate Religion',
    # 'Alternate Religion Family',
    # 'Alternate Religion Genus',
    'Alternative names',
    # Do not transfer per Peter 3/2/20: 'Other', # really Warfare variables,Military Technologies,Other will become 'Animal Other'
    'Articles',
    'Atlatl',
    'Battle axes',
    'Breastplates',
    'Bridges',
    'Bronze',
    'Calendar',
    'Camels',
    'Canals',
    'Capital',
    'Chainmail',
    'Complex fortifications',
    'Composite bow',
    'Constraint on executive by government',
    'Constraint on executive by non-government',
    'Copper',
    'Couriers',
    'Courts',
    'Crossbow',
    'Daggers',
    'Degree of centralization',
    'Ditch',
    'Dogs',
    'Donkeys',
    'Duration',
    'Earth ramparts',
    'Elephants',
    'Examination system',
    # 'Expert',
    'Fiction',
    'Foreign coins',
    'Formal legal code',
    'Fortified camps',
    'Full-time bureaucrats',
    'General postal service',
    'Gunpowder siege artillery',
    'Handheld firearms',
    'Helmets',
    'History',
    'Horses',
    'Ideological reinforcement of equality',
    'Ideological thought equates elites and commoners',
    'Ideological thought equates rulers and commoners',
    'Ideology reinforces prosociality',
    'Impeachment',
    'Indigenous coins',
    'Iron',
    'Javelins',
    'Judges',
    'Laminar armor',
    # TODO convert Language faux section to subsection
    'Language',
    # 'Linguistic Family', # capitalization!
    # 'Language Genus',
    'Leather, cloth', # note comma!!
    'Limb protection',
    'Lists, tables, and classifications', # be careful of commas!!
    'Long walls',
    'Merchant ships pressed into service',
    'Merit promotion',
    'Military levels',
    'Mines or quarries',
    'Mnemonic devices',
    'Moat',
    'Modern fortifications',
    'Moral concern is primary',
    'Moralizing enforcement in afterlife',
    'Moralizing enforcement in this life',
    'Moralizing enforcement is agentic',
    'Moralizing enforcement is certain',
    'Moralizing enforcement is targeted',
    'Moralizing enforcement of rulers',
    'Moralizing norms are broad',
    'Moralizing religion adopted by commoners',
    'Moralizing religion adopted by elites',
    'Non-phonetic writing',
    'Nonwritten records',
    'Original name',
    'Paper currency',
    'Peak Date',
    'Philosophy',
    'Phonetic alphabetic writing',
    'Plate armor',
    'Polearms',
    'Polity Population',
    'Polity territory',
    'Population of the largest settlement',
    'Ports',
    'Postal stations',
    'Practical literature',
    'Precious metals',
    'Professional Lawyers',
    'Professional military officers',
    'Professional priesthood',
    'Professional soldiers',
    'RA',
    # TODO convert Religion faux section to subsection
    # 'Religion',
    # 'Religion Family',
    # 'Religion Family', # spelling
    # 'Religious Tradition',
    # 'Religion Genus',
    # 'Religion Sect',
    'Religious levels',
    'Religious literature',
    'Roads',
    'Rulers are gods',
    'Rulers are legitimated by gods',
    'Sacred Texts',
    'Scaled armor',
    'Scientific literature',
    'Script',
    'Self bow',
    'Settlement hierarchy',
    'Settlements in a defensive position',
    'Shields',
    'Sling siege engines',
    'Slings',
    'Small vessels (canoes etc)', 'Small vessels (canoes, etc)', # commas
    'Spears',
    'Specialized government buildings',
    'Specialized military vessels',
    'Steel',
    'Stone walls (mortared)',
    'Stone walls (non-mortared)',
    'Supra-polity relations',
    'Supracultural entity',
    'Swords',
    'Tension siege engines',
    'Tokens',
    # 'Utilitarian public buildings',
    'War clubs',
    'Wood, bark, etc', # Note commas!!
    'Wooden palisades',
    'Written records',
    'drinking water supply systems',
    'elite status is hereditary',
    'food storage sites',
    'irrigation systems',
    'markets',
    'preceding (quasi)polity',
    'production of public goods',
    'relationship to preceding (quasi)polity',
    'scale of supra-cultural interaction',
    'succeeding (quasi)polity',
    ]

keep_variables_in_sections = {
    # 'Other': ['Military Technologies'],
    }

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

line_number = 0
emitted_line_number = 0
xml_stripped = None
def strip_xml_file(xml_filename):
    global options, line_number,emitted_line_number, xml_stripped
    directory,basename = os.path.split(xml_filename)
    basename,ext = os.path.splitext(basename)
    try:
        xml_file = open(xml_filename, "r")
    except IOError:
        print("ERROR: Could not open %s for reading." %  xml_filename)
        return

    xml_stripped_filename = os.path.join(directory,basename + '_stripped' + ext)
    try:
        xml_stripped = open(xml_stripped_filename, "w")
    except IOError:
        print("ERROR: Could not open %s for writing." %  xml_stripped_filename)
        return
    print('Stripping %s to %s' % (xml_filename,xml_stripped_filename))
    
    unique_variables = []
    unique_values = []
    current_title = None # the prevailing page (from <title>); nothing yet
    # Start out copying everything...
    skip = [False,False,False,False] # section, subsection, sub-subsection, sub-sub-subsection
    sections = [None,None,None,None]
    skip_reset = copy.copy(skip)
    sections_reset = copy.copy(sections)
    skip_variable = False
    emit_end_text = False

    def emit_line(raw_line):
        global options, line_number,emitted_line_number, xml_stripped
        emitted_line_number += 1
        if options.l:
            xml_stripped.write('%d:%d: %s' % (line_number, emitted_line_number, raw_line))
        else:
            xml_stripped.write(raw_line)
        
    ### main parsing loop
    for raw_line in xml_file:
        line_number += 1
        if emit_end_text:
            emit_line('</text>\n')
            emit_end_text = False

        # test unconditional emit of line
        drop_line = True
        for kl in keep_lines:
            if raw_line.find(kl) >= 0:
                drop_line = False
                break
        if not drop_line:
            emit_line(raw_line)
            continue
            
        drop_line = False
        for dl in drop_lines:
            # TODO if it starts with $ then use startswith
            # if (dl[0] == '$' and raw_line.startswith(dl[1:]) >= 0) or raw_line.find(dl) >= 0:
            if raw_line.find(dl) >= 0:
                drop_line = True
                break
        if drop_line:
            continue # skip this line

        # End of a page; reset all skip logic
        if raw_line.find('<sha1>') >= 0:
            skip_variable = False # reset
            skip = copy.copy(skip_reset) # reset
            sections = copy.copy(sections_reset)

        # import re
        # match = re.search(r'<title>(.*?)</title>.*',rawLine)
        # if match: title = match.groups(0)
        title = extract_between(raw_line,'<title>','</title>')
        if title is not None:
            current_title = title
            if options.s:
                print('<<%s>>:' % current_title)
            skip_variable = False # reset
            skip = copy.copy(skip_reset) # reset
            sections = copy.copy(sections_reset)

        # Deal with <text xml:space="preserve" bytes="111884">=Main Variables (Polity)=
        # by dealing with prefix and suffix separately
        text_start = raw_line.find('<text ')
        if text_start >= 0:
            text_end = raw_line.find('>')
            if text_end >= 0:
                text_end += 1
                emit_line(raw_line[0:text_end])
                raw_line = raw_line[text_end:]

        # Deal with stuff before </text> and emit that token separately on the next line
        text_end = raw_line.find('</text>')
        if text_end >= 0:
            # '''♠ Other wealth distribution ♣ ♥'''</text>
            raw_line = raw_line[0:text_end]
            emit_end_text = True
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
                # seems a legit sectiopn/subsection...decide whether to split
                skip_variable = False # reset
                # reset any remaining skip instructions for subsections below this one
                for idx in range(index,3+1):
                    skip[idx] = False
                    sections[idx] = None
                # Now do we skip this section's contents?
                if index == 0:
                    skip[index] = section not in top_sections_to_keep # or section in sections_to_keep?
                else:
                    skip[index] = section in sections_to_skip
                sections[index] = section
                if options.s:
                    skipping = ' <skip>' if any(skip) else ''
                    print('%s %s%s' % (structure_tag,section,skipping))
                break

        if any(skip):
            continue
        # See if we should drop a variable from this (and subsequent) lines
        vn = extract_between(raw_line,"♠","♣")
        if vn is not None:
            vn = vn.strip() # there is a variable + value on this line
            skip_variable = True # Assume the worst -- that we are dropping this line and its comments
            keeping_variable = vn in keep_variables
            if not keeping_variable:
                try:
                    ok_sections = keep_variables_in_sections[vn]
                    for section in ok_sections:
                        if section in sections:
                            keeping_variable = True
                            break
                except KeyError:
                    pass # skip it
                    
            if keeping_variable:
                skip_variable = False # keep this and all the lines following
                vv = extract_between(raw_line,"♣","♥")
                if vv is None:
                    print("ERROR: Found variable '%s' but no terminated value %s on line %d!" % (vn,sections,line_number))
                else:
                    vv = vv.strip()
                    # TODO parse it here and emit with prevailing NGA,polity,section,subsection only if NGA and section is not None
                    # Must parse NGA structure first
                    if options.v: # move this test to the print below
                        ss_tag = ''
                        if options.p:
                            polity = sections[0]
                            section = sections[1]
                            subsection = sections[2]
                            if section is not None:
                                subsection = subsection if subsection is not None else ''
                                ss_tag = '%s/%s/%s ' % (polity,section,subsection)
                        if True:
                            print('    %s♠%s♣%s♥' % (ss_tag,vn,vv))
                        else:
                            values = parse_values(vv)
                            for vs in expand_values(values):
                                print('   %5d: %s,%s,%s' % (line_number,ss_tag,vn,vs))
                    if options.u:
                        if vn not in unique_variables:
                            unique_variables.append(vn)
                        if vv not in unique_values:
                            unique_values.append(vv)
            else:
                if options.v:
                    print('    DROP ♠%s♣' % vn) # DEBUG

        if skip_variable:
            continue
        # Copy the line if we get here
        if options.x:
            st_span_i = raw_line.find('&lt;span style')
            if st_span_i >= 0:
                ed_span = '&lt;/span&gt'
                ed_span_i = raw_line.find(ed_span)
                if ed_span_i >= 0:
                    raw_line = raw_line[0:st_span_i] + raw_line[ed_span_i+len(ed_span)+1:]
                else:
                    print('WARNING: unbalanced span skipped %d' % line_number)
        emit_line(raw_line)

    xml_file.close()
    xml_stripped.close()
    if options.u:
        unique_variables.sort()
        print('\nUnique variable names:')
        pprint.pprint(unique_variables)
        unique_values.sort()
        print('\nUnique variable values:')
        pprint.pprint(unique_values)
    return

    
if __name__ == "__main__":
    retval = 1

    def main():
        global options
        options = argparse.ArgumentParser(prog=sys.argv[0],
                                          description='Strip a Seshat xml file')
        options.add_argument('xml_filename',help='The xml file to strip', default=None)
        options.add_argument('-s', action='store_true', help='Report structure',default=False)    
        options.add_argument('-p', action='store_true', help='Report variable sections',default=False)    
        options.add_argument('-v', action='store_true', help='Report variables',default=False)    
        options.add_argument('-u', action='store_true', help='Report unique values',default=False)    
        options.add_argument('-l', action='store_true', help='Report line numbers',default=False)    
        options.add_argument('-x', action='store_true', help='Strip <span> styles',default=False)    
        options = options.parse_args()

        if options.v:
            options.s = True
        if options.u:
            options.v = True
            options.s = True

        if options.xml_filename:
            strip_xml_file(options.xml_filename)
        return 0

    try:
        retval = main() # in case we decide to profile this puppy
    except SystemExit:
        pass # be quiet...someone just wants to leave like parse_args()
    except:
        print("Unexpected error:", traceback.format_exc())

    sys.exit(retval)

import os
import configparser

def genhhp(ini_file, hhp_file):
    cp = configparser.ConfigParser()
    cp.read(ini_file)
    FileName = cp.get("CHMGEN", "FileName")
    Title = cp.get("CHMGEN", "Title")
    
    if len(FileName) == 0:
        FileName = "main.chm"
        
    if len(Title) == 0:
        Title = "Help"
    
    with open(hhp_file, "w") as f:
        f.write("[OPTIONS]\n")
        f.write("Compatibility=1.1 or later\n")
        f.write("Compiled file="+FileName+"\n")
        f.write("Contents file=main.hhc\n")
        f.write("Create CHI file=Yes\n")
        #f.write("Default Window=a\n")
        f.write("Default topic=index.html\n")
        f.write("Display compile notes=No\n")
        f.write("Display compile progress=No\n")
        f.write("Full-text search=Yes\n")
        f.write("Index file=main.hhk\n")
        f.write("Language=0x409 English (United States)\n")
        f.write("Title="+Title+"\n")

        #f.write("\n[WINDOWS]\n")
        #f.write("a=,\"main.hhc\",\"main.hhk\",\"index.html\",,,,,,0x23520,,0x3006,,,,,,,,0\n")
        
        f.write("\n[INFOTYPES]\n");

def writeHead(f):
    f.write("<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML//EN\">\n");
    f.write("<HTML>\n");
    f.write("<HEAD>\n");
    #f.write("<meta name=\"GENERATOR\" content=\"Microsoft&reg; HTML Help Workshop 4.1\">\n");
    f.write("<!-- Sitemap 1.0 -->\n");
    f.write("</HEAD><BODY>\n");

def writeFoot(f):
    f.write("</BODY></HTML>\n");
    
def level(s):
    v = 0
    for ch in s:
        if ch == ' ':
            v += 1
        elif ch == '\t':
            v += 4
        else:
            break
    return int(v/4)

def indentPrint(f, indent, string):
    while indent > 0:
        f.write("\t")
        indent = indent - 1
    f.write(string)

def genchm(ini_file):
    genhhp(ini_file, "main.hhp")
    
    hhc = open("main.hhc", "w")
    hhk = open("main.hhk", "w")
    writeHead(hhc)
    writeHead(hhk)
    hhk.write("<UL>\n")

    CurrentLevel = -1
    is_content = False
    f = open(ini_file)
    line = f.readline()
    while line:
        s = line.rstrip()
        if is_content:
            Level = level(s)
            s = s.strip()
            if len(s) > 0:
                #print(s)
                key,value = s.split('=', 1)
                print(key + "   " + value)
                if Level > CurrentLevel:
                    assert Level == CurrentLevel + 1
                    indentPrint(hhc, Level, "<UL>\n")
                elif Level < CurrentLevel:
                    i = CurrentLevel;
                    while Level < i:
                        indentPrint(hhc, i, "</UL>\n")
                        i = i - 1

                CurrentLevel = Level;
                
                if len(value) > 0:
                    hhk.write("<LI> <OBJECT type=\"text/sitemap\">\n")
                    hhk.write("<param name=\"Name\" value=\""+key+"\">\n")
                    hhk.write("<param name=\"Name\" value=\""+key+"\">\n")
                    hhk.write("<param name=\"Local\" value=\""+value+"\">\n")
                    hhk.write("</OBJECT>\n")

                indentPrint(hhc, Level, "<LI> <OBJECT type=\"text/sitemap\">\n")
                indentPrint(hhc, Level+1, "<param name=\"Name\" value=\""+key+"\">\n")
                if len(value) > 0:
                    indentPrint(hhc, Level+1, "<param name=\"Local\" value=\""+value+"\">\n")
                indentPrint(hhc, Level+1, "</OBJECT>\n")
            
        else:
            is_content = (s == "[CONTENT]")
        line = f.readline()
    f.close()
    
    while CurrentLevel >= 0:
        indentPrint(hhc, CurrentLevel, "</UL>\n")
        CurrentLevel = CurrentLevel - 1
        
    hhk.write("</UL>\n")
    writeFoot(hhk)
    writeFoot(hhc)
    hhk.close()
    hhc.close()

genchm("content.ini")

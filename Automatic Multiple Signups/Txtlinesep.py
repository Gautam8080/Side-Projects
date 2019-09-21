fr  = open("testfile.txt", "r")
fw  = open("emailinline.txt", "w")
email = 0
while (email < 200):
    c = fr.read(1)
    fw.write(c)
    if c=='@':
        c = fr.read(1)
        fw.write(c)
        if c=='g':
            c = fr.read(1)
            fw.write(c)
            if c=='m':
                c = fr.read(1)
                fw.write(c)
                if c=='a':
                    c = fr.read(1)
                    fw.write(c)
                    if c=='i':
                        c = fr.read(1)
                        fw.write(c)
                        if c=='l':
                            c = fr.read(1)
                            fw.write(c)
                            if c=='.':
                                c = fr.read(1)
                                fw.write(c)
                                if c=='c':
                                    c = fr.read(1)
                                    fw.write(c)
                                    if c=='o':
                                        c = fr.read(1)
                                        fw.write(c)
                                        if c=='m':
                                            fw.write('')
                                            email = email + 1
                                            
fr.close()
fw.close()

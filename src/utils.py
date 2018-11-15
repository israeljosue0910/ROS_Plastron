def to_text(template,name):
    # Function that writes templates to a python file

    name = name[1:-1]
    f = open( name + '.py', 'w')
    for line in template:
        f.write("%s\n" % line)
    f.close()
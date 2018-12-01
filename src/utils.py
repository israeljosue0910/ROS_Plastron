def to_text(template,name):
    # Function that writes templates to a python file

    name = name.replace("'", "")
    f = open(r'C:/Users/israe/Documents/ROS_Plastron/test/' + name + '.py', 'w')
    for line in template:
        f.write("%s\n" % line)
    f.close()
def to_text(template):
    f = open(r'C:/Users/israe/Documents/ROS_Plastron/test/out.py', 'w')
    for line in template:
        f.write("%s\n" % line)
    f.close()
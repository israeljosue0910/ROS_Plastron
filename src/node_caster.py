def isSubscriber1(fileName):
    return 'sub1' in fileName


def isSubscriber2(fileName):
    return 'sub2' in fileName


def isPublisher(fileName):
    return 'pub' in fileName


def isServer(fileName):
    return 'server' in fileName


def isClient(fileName):
    return 'client' in fileName

def toLines(fileName):
    f = open(r'C:/Users/israe/Documents/ROS_Plastron/load_test/' + fileName, 'r')
    f.seek(0)
    lines = f.readlines()
    f.close()
    return lines

def getName(lines, fileName): #return string
    prevWord = "rospy.init_node("
    for line in lines:
        if prevWord in line:
            if isClient(fileName):
                name = line[16:-2]
            else:
                name = line[20:-2]
            return name


def getServiceParameters(lines, fileName): #returns list

    if not isClient(fileName):
        return "Not a valid node type for this function"
    counter = 1
    counter_2 = 1
    counter_3 = 1
    prevWord = "service_param" + str(counter)
    serv_var = "service" + str(counter_2)
    serv_var_2 = "service" + str(counter_3)
    lineNumber = 0
    service_init = 'ServiceProxy'
    service_var_serv = {}
    var_name_value = {}
    listOfParams = {}
    for line in lines:
        if service_init in line:
            list_of_line = lines[lineNumber].split()
            fullName = list_of_line[2]
            name = fullName[19:-1]
            service_var_serv[serv_var] = name
            counter_2 += 1
            serv_var = "service" + str(counter_2)
        if prevWord in line:
            list_of_line = lines[lineNumber].split()
            name = list_of_line[list_of_line.index(prevWord) + 2]
            var_name_value[prevWord] = name
            counter += 1
            prevWord = "service_param" + str(counter)
        if "serv_req" in line:
            if serv_var_2 in line:
                temp_list = []
                for key in var_name_value:
                    if key in line:
                        temp_list.append(var_name_value.get(key))
                if not temp_list:
                        temp_list.append('none')
                listOfParams[service_var_serv.get(serv_var_2)] = temp_list
                counter_3 += 1
                serv_var_2 = "service" + str(counter_3)
        lineNumber+=1

    return listOfParams


def getServiceNameAndType(lines, fileName): #returns a list of two lists
    lineNumber = 0
    listServNames = []
    listServTypes = []
    listOfBoth = {}
    prevWord = ''

    if isServer(fileName):
        prevWord = "rospy.Service("
    elif isClient(fileName):
        prevWord = "rospy.ServiceProxy("
    else:
        return "Not a valid node type for this function"
    for line in lines:
        if prevWord in line:
            list_of_line = lines[lineNumber].split()
            fullName = list_of_line[2]
            if isServer(fileName):
                name = fullName[14:-1]
            else:
                name = fullName[19:-1]
            servType = list_of_line[3][:-1]
            listOfBoth[name] = servType
        lineNumber+=1

    return listOfBoth


def getTopicNameAndType(lines, fileName): #returns a list of two lists
    lineNumber = 0
    listTopicNames = []
    listTopicTypes = []
    listOfBoth = {}
    prevWord = ''
    if isSubscriber1(fileName) or isSubscriber2(fileName):
        prevWord = "rospy.Subscriber("
    elif isPublisher(fileName):
        prevWord = "rospy.Publisher("
    else:
        return "Not a valid node type for this function"
    for line in lines:
        if prevWord in line:
            list_of_line = lines[lineNumber].split()
            fullName = list_of_line[2]
            if isSubscriber1(fileName) or isSubscriber2(fileName):
                name = fullName[17:-1]
            else:
                name = fullName[16:-1]
            topicType = list_of_line[3][:-1]
            listOfBoth[name] = topicType
        lineNumber+=1

    return listOfBoth


def getMessageObjects(lines, fileName): #returns a dictionary, the key is the object, the value is the list of values
    if not isPublisher(fileName):
        return "Not a valid node type for this function"
    counter = 1
    checker = 0
    lineNumber = 0
    prevWord = "msg" + str(counter) + " ="
    tempList = []
    tempList2 = []
    msgDict = {}
    for line in lines:
        if prevWord in line:
            list_of_line = lines[lineNumber].split()
            fullName = list_of_line[2]
            fullName = fullName[:-2]
            msgDict[fullName] = []
            tempList.append(fullName)
            counter += 1
            prevWord = "msg" + str(counter) + " ="
        lineNumber+=1
    lineNumber = 0
    counter = 1
    prevWord = "msg" + str(counter) + "."
    nextPrevWord = "msg" + str(counter + 1) + "."
    for line in lines:
        if prevWord in line:
            list_of_line = lines[lineNumber].split()
            fullName = list_of_line[1]
            tempList2.append(fullName)
            checker = 1
        elif nextPrevWord in line:
            list_of_line = lines[lineNumber].split()
            fullName = list_of_line[1]
            msgDict[tempList[counter - 1]] = tempList2[:]
            tempList2.clear()
            counter += 1
            prevWord = "msg" + str(counter) + "."
            nextPrevWord = "msg" + str(counter + 1) + "."
            tempList2.append(fullName)
        lineNumber += 1
    msgDict[tempList[counter - 1]] = tempList2[:]
    return msgDict

def main():
    fileName = "node1_pub.py"
    lines = toLines(fileName)

    print(getMessageObjects(lines, fileName))

if __name__ == '__main__':
    main()

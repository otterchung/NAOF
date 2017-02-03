def convert(story):
    num_r = story.count("[")
    print num_r

    i = 0
    prev = 0
    while i < num_r:
        begin = story.find("[", prev)
        end = story.find("]", prev) + 1
        prev = end + 2

        component = story[begin:end]
        middle = component.find(",")

        grammar_c = component[1:middle]
        realWord = component[middle+1:len(component)-1]

        story = story.replace(component, textbox(grammar_c, i))
        i = i + 1
        print i
    story = story + """<br><input type="submit">"""   
    return story

def reConvert(story):
    num_r = story.count("[")
    print num_r

    i = 0
    prev = 0
    while i < num_r:
        begin = story.find("[", prev)
        end = story.find("]", prev) + 1
        prev = end + 2

        component = story[begin:end]
        middle = component.find(",")

        grammar_c = component[1:middle]
        realWord = component[middle+1:len(component)-1]

        story = story.replace(component, "<i>" + self.request.get(i) + "</i>")
        i = i + 1
        print i
    story = story + """<br><input type="submit">"""   
    return story

def textbox(grammar,count):
    textbox = """
            <input type="text" name="numToReplace" value="grammar">
        """
    textbox = textbox.replace("grammar",grammar)
    textbox = textbox.replace("numToReplace",str(count))
    return textbox

def create_btn(theType, name, value):
    textbox = """
            <input type="theType" name="theName" value="theValue">
        """
    textbox = textbox.replace("theName",name).replace("theValue",value).replace("theType",theType)
    return textbox

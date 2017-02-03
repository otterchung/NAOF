#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2


#-------------- stories
execfile("stories.py")

#------------------- defines
execfile("defines.py")

#------------ page_handling
execfile("page_format.py")

class MainPage(T_Handler):

    body = """
        <form action="/AdLib" method="post">
        """

    for i in storyDb:
        body = body + create_btn("radio", "story", str(i)) + str(i).replace("_", " ") + "<br>"
        #    <input type="radio" name="story" value="Tortoise_and_the_Hair" checked="checked">Tortoise and the Hair
        #    <input type="radio" name="story" value="Not_a_Story">Not a Story<br><br>
        #
    body = body + """<br><input type="submit"></form>"""
        
    
    def post(self):
        self.write_html()

    def get(self):
        self.write_html()


class AdLib(T_Handler):
    # a 'story' is passed into this class.

    def get(self):        

        self.write_html()

    def post(self):
        self.body = """<form action="/AdLib2" method="post">"""

        
        whichStory = self.request.get("story")
        theStory = storyDb[whichStory]
        convertStory = convert(theStory)

        self.body = self.body + """<input name="story" value=\"""" + whichStory + """\"><br><br><br>"""
        self.body = self.body + convertStory
        
        self.write_html()

class AdLib2(T_Handler):

    def get(self):
        self.write_html()
        
    def post(self):
        self.body = """<form action="/AdLib2" method="post">"""
        
        whichStory = self.request.get("story")
        theStory = storyDb[whichStory]        
        story = theStory
        #reConvertStory = reConvert(theStory)
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

            story = story.replace(component, "<i>" + self.request.get(str(i)) + "</i>" + " (" + realWord + ")")
            i = i + 1
            print i
        #reConvertStory //end
        story = story + """<br>""" + """<br><br><a href = "/">Main Page of AdLibs</a>"""
        self.body = self.body + story
            
        self.write_html()       

        
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/AdLib', AdLib),
    ('/AdLib2', AdLib2)
], debug=True)


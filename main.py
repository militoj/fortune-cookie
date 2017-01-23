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
import random

def getRandomFortune():
    # list of possible fortunes
    fortunes = [
        "Man who want pretty nurse, must be patient",
        "Man who run in front of bus get tired, man who run behind bus get exhausted",
        "Wise man never play leapfrog with unicorn"
    ]

    #randomly select one of the fortunes
    index = random.randint(0, 2)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        fortune_pargraph = "<p>" + fortune_sentence + "</p>"

        lucky_number = "<strong>" + str(random.randint(1, 100)) + "</strong>"
        number_sentence = 'Your lucky number: ' + lucky_number
        number_paragraph = "<p>" + number_sentence + "</p>"

        cookie_button = "<a href='.'><button>Cookies! Nom nom nom</button></a>"

        content = header + fortune_pargraph + number_paragraph + cookie_button
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

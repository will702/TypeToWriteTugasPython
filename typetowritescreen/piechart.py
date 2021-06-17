from akivymd.uix.piechart import AKPieChart

from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
import math

class Piechart(MDScreen):
    items = [{'None': 100}]
    def __init__(self, **kw):
        super().__init__(**kw)

    def make_piechart(self):

        self.piechart = AKPieChart(
            items=self.items,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=[None, None],
            size=(dp(500), dp(380)),

        )
        self.ids.chart_box.add_widget(self.piechart)

    def update_chart(self):

        try:
            with open('data/date.json', 'r') as f:
                import json

                attempts = json.load(f)

                if len(attempts) > 0:
                    values = attempts.values()
                    tot = sum(values)



                    for i in attempts.copy().keys():
                        try:

                            attempts[i[5:10]] = attempts[i]
                            del attempts[i]

                        except:
                            pass
                    for i in attempts.copy():
                        value = attempts[i]

                        attempts.pop(i)
                        attempts.update({f'{i} :\n{value}': value})
                    for i in attempts.keys():

                        attempts[i] = math.floor(((attempts[i]) * 100) / tot)



                    while sum(attempts.values()) < 100:
                        for i in attempts.keys():
                            if sum(attempts.values()) == 100:
                                break
                            attempts[i] += 1



                else:
                    attempts = {'None':100}

                items = [attempts]

                self.piechart.items = items


        except:
            pass

    def remove_chart(self):
        self.ids.chart_box.remove_widget(self.piechart)




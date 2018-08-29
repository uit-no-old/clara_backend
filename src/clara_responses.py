from functools import reduce

class ClaraResponses:
    def item_calculate_score(self, response):
        """
        Calculate average score of each main_scale for one item
        """
        try:
            self._calculare_score(response)
        except TypeError:
            pass

    def resource_calculate_score(self, response):
        """
        Calculate average score of each main_scale for the whole resource
        """
        try:
            for clara_items in response['_items']:
                self._calculare_score(clara_items)
        except TypeError:
            pass

    def _calculare_score(self, clara_items):
        clara_items['score'] = {}
        for clara_item in clara_items['clara_items']:
            try:
                clara_items['score'][clara_item['clara_item']['main_scale']].append(clara_item['response_option']['response_number'])
            except KeyError:
                clara_items['score'].update({clara_item['clara_item']['main_scale']: []})
                clara_items['score'][clara_item['clara_item']['main_scale']].append(clara_item['response_option']['response_number'])

        for main_scale in clara_items['score']:
            average = reduce(lambda x, y: x + y, clara_items['score'][main_scale]) / len(clara_items['score'][main_scale])
            clara_items['score'][main_scale] = average

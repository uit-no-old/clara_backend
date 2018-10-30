from functools import reduce

class ClaraResponses:
    def item_calculate_score(self, response):
        """
        Calculate average score of each main_scale for one item
        """
        self._is_embedded(response)

    def resource_calculate_score(self, response):
        """
        Calculate average score of each main_scale for the whole resource
        """
        for clara_items in response['_items']:
            self._is_embedded(clara_items)

    def _is_embedded(self, clara_items):
        """
        If some fields are not embedded we dont have all the data we need to
        calculate the score
        """
        try:
            self._calculare_score(clara_items)
        except TypeError:
            clara_items['score'] = {'ERROR': 'Have you embedded student_classes, clara_items.clara_item and clara_items.response_option?'}

    def _calculare_score(self, clara_items):
        clara_items['score'] = {}
        for clara_item in clara_items['clara_items']:
            try:
                clara_items['score'][clara_item['clara_item']['main_scale']].append(clara_item['response_option']['response_value'])
            except KeyError:
                clara_items['score'].update({clara_item['clara_item']['main_scale']: []})
                clara_items['score'][clara_item['clara_item']['main_scale']].append(clara_item['response_option']['response_value'])

        for main_scale in clara_items['score']:
            average = reduce(lambda x, y: x + y, clara_items['score'][main_scale]) / len(clara_items['score'][main_scale])
            clara_items['score'][main_scale] = average

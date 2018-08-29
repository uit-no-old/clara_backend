from eve import Eve
from src.clara_responses import ClaraResponses

clara_responses = ClaraResponses()
app = Eve()
# Callback when someone is accessing one item from clara_responses
app.on_fetched_item_clara_responses += clara_responses.item_calculate_score
app.on_fetched_resource_clara_responses += clara_responses.resource_calculate_score

if __name__ == '__main__':
    app.run(host='0.0.0.0')

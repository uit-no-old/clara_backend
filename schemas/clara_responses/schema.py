# import schemas.clara_items.schema as clara_items_schema
# import schemas.response_options.schema as response_options_schema
import schemas.student_classes.schema as student_classes_schema

schema = {
    'student_classes': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'student_classes',
            'field': '_id',
            'embeddable': True
        }
    },
    'clara_items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'clara_item': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'clara_items',
                        'field': '_id',
                        'embeddable': True
                    }
                },
                'response_option': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'response_options',
                        'field': '_id',
                        'embeddable': True
                    }
                }
            }
        }
    }
}

# ,
# 'score': {
#     'type': 'list',
#     'readonly': True,
#     'schema': {
#         'type': 'dict',
#         'schema': {
#             'main_scale': {'type': 'string', 'readonly': True},
#             'scale_score': {'type': 'integer', 'readonly': True}
#         }
#     }
# }

clara_responses = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    # 'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    # 'additional_lookup': {
    #     'url': 'regex("[\w]+")',
    #     'field': 'language'
    # },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # Embed by default
    'embedded_fields': ['student_classes', 'clara_items.clara_item', 'clara_items.response_option'],

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

schema = {
    # Schema definition, of the CLARA items.
    'main_scale': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'required': True
    },
    'itembank_id': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 4,
        'required': True
    },
    'presenting_order': {
        'type': 'integer',
        'required': True
    },
    'clara_item': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': True
    },
    'language': {
        'type': 'string',
        'minlength': 2,
        'maxlength': 2,
        'required': True
    },
}

clara_items = {
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

    # most global settings can be overridden at resource level
    'resource_methods': ['GET'],

    'schema': schema
}

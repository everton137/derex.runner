SEARCH_ENGINE = "search.elastic.ElasticSearchEngine"
SEARCH_FILTER_GENERATOR = (
    "lms.lib.courseware_search.lms_filter_generator.LmsSearchFilterGenerator"
)
SEARCH_INITIALIZER = (
    "lms.lib.courseware_search.lms_search_initializer.LmsSearchInitializer"
)
SEARCH_RESULT_PROCESSOR = (
    "lms.lib.courseware_search.lms_result_processor.LmsSearchResultProcessor"
)
SEARCH_SKIP_ENROLLMENT_START_DATE_FILTERING = True
ELASTIC_SEARCH_CONFIG = [{u"host": u"elasticsearch", u"port": 9200}]

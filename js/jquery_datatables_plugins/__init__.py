from fanstatic import Library, Resource
from js.jquery_datatables import jquery_datatables_js

library = Library('jquery_datatables_plugins', 'resources')

column_filter = Resource(
    library, 'columnfilter/media/js/jquery.dataTables.columnFilter.js',
    depends=[jquery_datatables_js],
    minified='columnfilter/media/js/jquery.dataTables.columnFilter.min.js')

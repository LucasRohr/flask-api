def validate_page_size(request, page_size):
    if 'page_size' in request.args:

        if int(request.args.get('page_size')) >= 1:
            page_size = int(request.args.get('page_size'))

        return page_size

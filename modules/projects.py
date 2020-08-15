def carousel_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
    return lst


def get_project_by_slug(slug, projects_list):
    for project in projects_list:
       if project['slug'] == slug:
           return project

    return None

def get_row_size(count):
    if count % 3 == 0:
        return 3

    return 2


def get_featured_column_classname(count):
    if count % 3 == 0:
        return "govuk-grid-column-one-third"

    if count % 2 == 0:
        return "govuk-grid-column-one-half"

    return "govuk-grid-column-full"


def convert_list_to_matrix(items, row_length=3):
    child_groups_for_layout = []
    row = []
    offset = 0

    for item in items:
        row.append(item)
        offset += 1

        if offset % row_length == 0:
            child_groups_for_layout.append(row)
            row = []

    if len(row):
        child_groups_for_layout.append(row)

    return child_groups_for_layout


def get_featured_data(child_class, parent_instance):

    child_categories = child_class.objects.live().child_of(parent_instance).order_by("title")

    row_width = get_row_size(len(child_categories))
    child_categories_matrix = convert_list_to_matrix(child_categories, row_width)

    featured_column_classname = get_featured_column_classname(len(child_categories))

    return featured_column_classname, child_categories_matrix

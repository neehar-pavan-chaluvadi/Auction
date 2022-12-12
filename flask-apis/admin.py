from flask_admin.contrib.sqla import ModelView

class ProductViews(ModelView):

    form_columns = ['id', 'name', 'description', 'image_link', 'base_price',
                    'auction_start_date', 'auction_end_date'
                    ]
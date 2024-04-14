from django.shortcuts import render
from django.db import connections
from .models import OnlineStudents
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin')
def index(request):
    try:
        wordpress_db_connection = connections['wordpress']

        sql_query = """
            SELECT
            c.username AS name,
            oi.order_item_name AS course_ordered,
            os.date_paid,
            os.date_completed,
            os.net_total AS amount_paid,
            os.order_id,
            os.customer_id AS userid,
            os.status AS order_status,
            c.email
            FROM
            wpsl_wc_order_stats os
            JOIN
            wpsl_wc_customer_lookup c ON os.customer_id = c.customer_id
            JOIN
            wpsl_woocommerce_order_items oi ON os.order_id = oi.order_id
            WHERE
            os.status = 'wc-completed';
        """

        with wordpress_db_connection.cursor() as cursor:
            cursor.execute(sql_query)
            wordpress_data = cursor.fetchall()

        new_records = []
        for row in wordpress_data:
            if not OnlineStudents.objects.filter(order_id=row[5], user_id=row[6]).exists():
                OnlineStudents.objects.create(
                    name=row[0],
                    course_ordered=row[1],
                    date_paid=row[2],
                    date_completed=row[3],
                    amount_paid=row[4],
                    order_id=row[5],
                    user_id=row[6],
                    order_status=row[7],
                    email = row[8]
                )
                new_records.append(row)

        if new_records:
            notification = f"{len(new_records)} new record(s) fetched and saved."
        else:
            notification = f"{len(new_records)} new record(s) fetched"

        return render(request, 'index.html', {'notification': notification})

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'index.html', {'error_message': error_message})

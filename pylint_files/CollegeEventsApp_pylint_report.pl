************* Module CollegeEventsApp.urls
W:  7, 0: Unused include imported from django.conf.urls (unused-import)
W:  8, 0: Unused admin imported from django.contrib (unused-import)
************* Module CollegeEventsApp.views
W:  3, 0: Wildcard import models (wildcard-import)
W: 61,12: Redefining name 'profile' from outer scope (line 97) (redefined-outer-name)
W:101,12: Redefining name 'profile' from outer scope (line 97) (redefined-outer-name)
W:135,12: Redefining name 'profile' from outer scope (line 97) (redefined-outer-name)
W:164,20: Unused variable 'editFin' (unused-variable)
W:163,20: Unused variable 'confirm' (unused-variable)
R:146, 0: Too many return statements (8/6) (too-many-return-statements)
R:146, 0: Too many branches (15/12) (too-many-branches)
W:202,12: Redefining name 'profile' from outer scope (line 97) (redefined-outer-name)
W:211,16: Unused variable 'editFin' (unused-variable)
W:210,16: Unused variable 'confirm' (unused-variable)
W:268,12: Redefining name 'profile' from outer scope (line 97) (redefined-outer-name)
W:282, 8: No exception type(s) specified (bare-except)
W:304, 8: No exception type(s) specified (bare-except)
W:  3, 0: Unused import models from wildcard import (unused-wildcard-import)
W:  4, 0: Unused render imported from django.shortcuts (unused-import)
W:  5, 0: Unused redirect imported from django.shortcuts (unused-import)
W:  8, 0: Unused csrf_exempt imported from django.views.decorators.csrf (unused-import)
W: 13, 0: Unused connections imported from django.db (unused-import)


Report
======
272 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |8      |8          |=          |75.00       |12.50    |
+---------+-------+-----------+-----------+------------+---------+
|class    |3      |3          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|method   |3      |3          |=          |66.67       |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |13     |13         |=          |0.00        |23.08    |
+---------+-------+-----------+-----------+------------+---------+



External dependencies
---------------------
::

    CollegeEventsApp 
      \-views (CollegeEventsApp.urls)
    django 
      \-conf (CollegeEventsApp.migrations.0001_initial)
      | \-urls (CollegeEventsApp.urls)
      \-contrib 
      | \-admin (CollegeEventsApp.urls)
      | \-auth (CollegeEventsApp.views)
      |   \-decorators (CollegeEventsApp.views)
      |   \-models (CollegeEventsApp.models,CollegeEventsApp.views)
      \-core 
      | \-exceptions (CollegeEventsApp.views)
      \-db (CollegeEventsApp.views)
      | \-migrations (CollegeEventsApp.migrations.0001_initial)
      | \-models (CollegeEventsApp.models,CollegeEventsApp.migrations.0001_initial)
      \-http (CollegeEventsApp.views)
      \-shortcuts (CollegeEventsApp.views)
      \-template (CollegeEventsApp.views)
      \-views 
        \-decorators 
          \-csrf (CollegeEventsApp.views)



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |378    |90.65 |378      |=          |
+----------+-------+------+---------+-----------+
|docstring |8      |1.92  |8        |=          |
+----------+-------+------+---------+-----------+
|comment   |15     |3.60  |15       |=          |
+----------+-------+------+---------+-----------+
|empty     |16     |3.84  |16       |=          |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |0      |0        |=          |
+-----------+-------+---------+-----------+
|refactor   |2      |2        |=          |
+-----------+-------+---------+-----------+
|warning    |19     |19       |=          |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+



% errors / warnings by module
-----------------------------

+-----------------------+------+--------+---------+-----------+
|module                 |error |warning |refactor |convention |
+=======================+======+========+=========+===========+
|CollegeEventsApp.views |0.00  |89.47   |100.00   |0.00       |
+-----------------------+------+--------+---------+-----------+
|CollegeEventsApp.urls  |0.00  |10.53   |0.00     |0.00       |
+-----------------------+------+--------+---------+-----------+



Messages
--------

+---------------------------+------------+
|message id                 |occurrences |
+===========================+============+
|unused-import              |6           |
+---------------------------+------------+
|redefined-outer-name       |5           |
+---------------------------+------------+
|unused-variable            |4           |
+---------------------------+------------+
|bare-except                |2           |
+---------------------------+------------+
|wildcard-import            |1           |
+---------------------------+------------+
|unused-wildcard-import     |1           |
+---------------------------+------------+
|too-many-return-statements |1           |
+---------------------------+------------+
|too-many-branches          |1           |
+---------------------------+------------+



Global evaluation
-----------------
Your code has been rated at 9.23/10 (previous run: 9.11/10, +0.12)


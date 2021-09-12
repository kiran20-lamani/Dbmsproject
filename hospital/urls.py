"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns=[
				path('', views.login_form),
				path('submit_form/', views.submit_form),
				path('go/',views.go, name='go'),
				path('invoice/',views.invoice),
				path('main/',views.main, name='main'),
				path('log/',views.log, name='log'),

				path('ins',views.ins, name='ins'),
				path('show',views.show, name='show'),
				path('edit/<int:inst_id>',views.edit), 
				path('update/<int:inst_id>',views.update),
				path('delete/<int:inst_id>',views.delete),

				path('dep',views.dep),
				path('show1',views.show1),
				path('edit1/<int:dept_id>',views.edit1), 
				path('update1/<int:dept_id>',views.update1),
				path('delete1/<int:dept_id>',views.delete1),

				path('con',views.con),
				path('show2',views.show2),
				path('delete2/<int:con_id>',views.delete2),

				path('ord',views.ord),
				path('show3',views.show3),
				path('delete3/<int:ord_id>',views.delete3),

				path('sto',views.sto),
				path('show4',views.show4),
				path('delete4/<int:st_id>',views.delete4),
]

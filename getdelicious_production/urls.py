from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin






urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'products.views.home', name='home'),
    url(r'^s/$', 'products.views.search', name='search'),
    # url(r'^products/$', 'products.views.all', name='products'),
    
    url(r'^cart/checkout/add_address/$', 'accounts.views.add_address', name='add_address'),
    url(r'^cart/checkout/$', 'orders.views.checkout', name='checkout'),
    url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),
    url(r'^cart/$', 'carts.views.view', name='cart'),
    
    url(r'^orders/$', 'orders.views.orders', name='user_orders'),
    url(r'^ajax/dismiss_marketing_message/$', 'marketing.views.dismiss_marketing_message', name='dismiss_marketing_message'),
    url(r'^ajax/email_signup/$', 'marketing.views.email_signup', name='ajax_email_signup'),
    

    #footerpages
    url(r'^about/$', 'footerpages.views.about_us', name='about_us'),
    url(r'^faq/$', 'footerpages.views.faq', name='faq'),
    url(r'^privacy/$', 'footerpages.views.privacy', name='privacy'),
    url(r'^terms/$', 'footerpages.views.terms', name='terms'),

    #states
    url(r'^victoria/$', 'products.views.victoria', name='victoria'),
    url(r'^new-south-wales/$', 'products.views.new_south_wales', name='new_south_wales'),
    url(r'^south-australia/$', 'products.views.south_australia', name='south_australia'),
    url(r'^queensland/$', 'products.views.queensland', name='queensland'),
    url(r'^western_australia/$', 'products.views.western_australia', name='western_australia'),   

    #contact us
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    
    # url(r'^blog/', include('blog.urls')),
    #(?P<all_items>.*)
    #(?P<id>\d+)
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'accounts.views.logout_view', name='auth_logout'),
    url(r'^login/$', 'accounts.views.login_view', name='auth_login'),
    url(r'^register/$', 'accounts.views.registration_view', name='auth_register'),
    url(r'^support/$', 'accounts.views.support', name='support'),
    url(r'^profile/$', 'accounts.views.profile', name='profile'),
    url(r'^profile/add/$', 'accounts.views.profile_add', name='profile_add'),
    url(r'^profile/edit/$', 'accounts.views.profile_edit', name='profile_edit'),
    url(r'^packages/$', 'accounts.views.packages', name='packages'),
    url(r'^packages/edit/(?P<variation_id>\d+)/$', 'accounts.views.packages_edit', name='packages_edit'),
    url(r'^packages/delete/(?P<variation_id>\d+)/$', 'accounts.views.packages_delete', name='packages_delete'),
    url(r'^packages/add/$', 'accounts.views.packages_add', name='packages_add'),
    # url(r'^accounts/address/add/$', 'accounts.views.add_address', name='add_address'),
    url(r'^activate/(?P<activation_key>\w+)/$', 'accounts.views.activation_view', name='activation_view'),

    url(r'^(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),

    
    url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
) 




    
if settings.DEBUG:
    handler404 = 'views.custom_404'
    handler500 = 'views.custom_500'
#     urlpatterns += patterns('',
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.STATIC_ROOT,
#         }),
# )
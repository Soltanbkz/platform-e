from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.views.static import serve

admin.site.site_header = "Your Company"

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")
    ),  # Django JET dashboard URLS
    path("", include("core.urls")),
    path("accounts/", include("accounts.urls")),
    path("programs/", include("course.urls")),
    path("result/", include("result.urls")),
    path("search/", include("search.urls")),
    path("quiz/", include("quiz.urls")),
    path("payments/", include("payments.urls")),
    path("accounts/api/", include("accounts.api.urls", namespace="accounts-api")),
    path("admin/", admin.site.urls),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]


urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
                re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
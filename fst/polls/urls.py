from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'game/$', views.gameindex, name='gameindex'),
   url(r'Blog/$',views.blog,name='blog'),
   url(r'blogsid/(?P<pid>[a-zA-Z0-9]+)/$',views.blogsid,name='blogsid'),
   url(r'addcomplist/$',views.addcomplist,name='addcomplist'),
   url(r'complist/$',views.complist,name='complist'),
   url(r'tbrand/findsimilar/(?P<category>[a-zA-Z_ ]+)/$',views.tbrand,name='tbrand'),
   url(r'tbrand/(?P<category>[a-zA-Z_ ]+)/$',views.tbrand1,name='tbrand1'),
   url(r'getprice/(?P<pid>[a-zA-Z0-9]+)/$',views.getprice,name='getprice'),
   url(r'pdct/(?P<pdctid>[a-z0-9]+)/$',views.productdetail,name='productdetail'),
   url(r'livesearch/(?P<searchquery>[a-z]+)/$',views.lsearch,name='lsearch'),
   url(r'tbrand/(?P<category>[a-zA-Z_ ]+)/(?P<brand>[a-zA-Z0-9 _&]+)/$',views.catebrand1,name='catebrand1'),
   url(r'tprice/(?P<category>[a-zA-Z_ ]+)/(?P<p1>[0-9]+)/(?P<p2>[0-9]+)/$',views.tprice,name='tprice'),
url(r'tbrand/findsimilar/(?P<category>[a-zA-Z_ ]+)/(?P<brand>[a-zA-Z0-9 _&]+)/$',views.catebrand,name='catebrand'),
url(r'tbrandc/(?P<category>[a-zA-Z_ ]+)/(?P<brand>[a-zA-Z _&]+)/(?P<colr>[a-z]+)/$',views.catebrandc,name='catebrandc'),
   url(r'tcolor/(?P<category>[a-zA-Z_ ]+)/$',views.tcolor,name='tcolor'),
   url(r'tcolor/(?P<category>[a-zA-Z_ ]+)/(?P<color>[a-zA-Z/ &]+)/$',views.catecolor,name='catecolor'),
   url(r'loadmoreall/(?P<category>[a-zA-Z_ ]+)/(?P<pgn>[0-9]+)/(?P<col>[0-9]+)/$',views.loadmoreall,name='loadmoreall'),
   url(r'mlall/(?P<category>[a-zA-Z_ ]+)/(?P<pgn>[0-9]+)/(?P<col>[0-9]+)/$',views.mloadmoreall,name='mloadmoreall'),
   url(r'loadmoretour/(?P<category>[a-zA-Z_ ]+)/(?P<block>[0-9]+)/$',views.loadmoretour,name='loadmoretour'),
  url(r'^findsimilar/(?P<category>[a-zA-Z_ ]+)/$',views.findsimilar,name='findsimilar'),
 url(r'^sbcate/(?P<category>[a-zA-Z_ ]+)/(?P<sbcat>[0-9]+)/$',views.sbcate,name='sbcate'),
url(r'^addtocat/(?P<onsource>[a-z]+)/(?P<pid>[a-z0-9]+)/(?P<catval>[0-9]+)/$',views.addtocat,name='addtocat'),
   url(r'^blockthis/(?P<onsource>[a-z]+)/(?P<pid>[a-z0-9]+)/$',views.blockthis,name='blockthis'),
  url(r'^blockbrand/(?P<brand>[[a-zA-Z_ ]+)/$',views.blockbrand,name='blockbrand'),
   url(r'^matchsimilar/(?P<onsource>[a-z]+)/(?P<pid>[a-z0-9]+)/(?P<spid>[a-z0-9]+)/$',views.matchsimilar,name='matchsimilar'),
    url(r'^(?P<category>[a-zA-Z_ ]+)/$',views.tours,name='tours'),
   url(r'^sbcat/(?P<category>[0-9]+)/(?P<ccategory>[a-zA-Z_ ]+)/$',views.sbtour,name='sbtour'),
   url(r'^sbsbcat/(?P<ctype>[a-z]+)/(?P<cval>[a-zA-Z_0-9 ]+)/(?P<category>[0-9]+)/(?P<ccategory>[a-zA-Z_ ]+)/$',views.sbsbtour,name='sbsbtour'),
    url(r'^(?P<qid>[0-9]+)/(?P<category>[a-zA-Z_ ]+)/$',views.retcategory,name='retcategory'),
url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


]
